#!/usr/bin/env python3
"""
OCR LLM Agent - Multi-provider image text extraction tool.

Supports OpenAI GPT-4o, Ollama LLaVA, and Hugging Face SmolVLM for
extracting text from images (local files or URLs).
"""

import os
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Annotated, Any, Dict, List, Optional, TypedDict, Union

import typer
from dotenv import load_dotenv
from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from agent.tools import extract_text

load_dotenv()

# Constants
DEFAULT_MODELS = {
    "openai": "gpt-4o",
    "ollama": "llava:7b",
    "huggingface": "HuggingFaceTB/SmolVLM-Instruct"
}

VALID_IMAGE_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'
}

DOWNLOAD_TIMEOUT = 30
MAX_TOKENS = 1000

# Type definitions
class AgentState(TypedDict):
    """State structure for the LangGraph agent."""
    input_file: Optional[str]
    messages: Annotated[List[AnyMessage], add_messages]


# Initialize Typer app
app = typer.Typer(
    help="OCR LLM Agent - Extract text from images using AI"
)

# Available tools
tools = [extract_text]


def get_llm_with_tools(
    model_provider: str, 
    model_name: str
) -> Union[str, ChatOpenAI, ChatOllama]:
    """
    Get LLM with tools based on provider and model name.
    
    Args:
        model_provider: The AI provider ('openai', 'ollama', 'huggingface')
        model_name: Specific model name to use
        
    Returns:
        Configured LLM instance or placeholder for huggingface
        
    Raises:
        ValueError: If provider is unsupported or dependencies missing
    """
    provider = model_provider.lower()
    
    if provider == "openai":
        llm = ChatOpenAI(model=model_name)
        return llm.bind_tools(tools, parallel_tool_calls=False)
    elif provider == "ollama":
        llm = ChatOllama(model=model_name, temperature=0.7)
        return llm.bind_tools(tools)
    elif provider == "huggingface":
        # SmolVLM needs special handling, return placeholder
        return "huggingface_placeholder"
    else:
        supported = "', '".join(DEFAULT_MODELS.keys())
        raise ValueError(f"Unsupported provider: {provider}. "
                        f"Use: '{supported}'")


def assistant(state: AgentState, llm_with_tools) -> Dict[str, Any]:
    """
    Assistant function for the LangGraph agent.
    
    Args:
        state: Current agent state
        llm_with_tools: Configured LLM instance
        
    Returns:
        Updated state with response
    """
    tool_description = """
    def extract_text(img_path: str) -> str:
        Extracts text from an image specified by its file path.
        
        Args:
            img_path: Path to the image file
            
        Returns:
            Extracted text content or empty string on error
    """
    
    image = state["input_file"]
    sys_msg = SystemMessage(content=(
        "You are a helpful assistant that can analyze documents "
        f"with provided tools:\n{tool_description}\n\n"
        f"Currently loaded image: {image}"
    ))

    response = llm_with_tools.invoke([sys_msg] + state["messages"])
    return {
        "messages": [response],
        "input_file": state["input_file"]
    }


def create_graph(llm_with_tools) -> StateGraph:
    """
    Create the state graph with the specified LLM.
    
    Args:
        llm_with_tools: Configured LLM instance
        
    Returns:
        Compiled StateGraph ready for execution
    """
    def assistant_with_llm(state: AgentState) -> Dict[str, Any]:
        return assistant(state, llm_with_tools)
    
    builder = StateGraph(AgentState)
    builder.add_node("assistant", assistant_with_llm)
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_edge("tools", "assistant")
    return builder.compile()


def is_url(string: str) -> bool:
    """
    Check if a string is a valid URL.
    
    Args:
        string: String to validate
        
    Returns:
        True if string is a valid URL, False otherwise
    """
    try:
        result = urllib.parse.urlparse(string)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def get_image_extension(
    url: str, 
    content_type: str = ""
) -> str:
    """
    Determine image extension from URL or content type.
    
    Args:
        url: Image URL
        content_type: HTTP content-type header
        
    Returns:
        File extension (e.g., '.jpg', '.png')
    """
    # Check content type first
    if 'jpeg' in content_type or 'jpg' in content_type:
        return '.jpg'
    elif 'png' in content_type:
        return '.png'
    elif 'gif' in content_type:
        return '.gif'
    elif 'webp' in content_type:
        return '.webp'
    
    # Fall back to URL path extension
    parsed_url = urllib.parse.urlparse(url)
    path_ext = Path(parsed_url.path).suffix.lower()
    
    if path_ext in VALID_IMAGE_EXTENSIONS:
        return path_ext
    
    return '.jpg'  # Default fallback


def download_image_from_url(url: str) -> str:
    """
    Download an image from a URL and save it to a temporary file.
    
    Args:
        url: The URL of the image to download
        
    Returns:
        Path to the downloaded temporary file
        
    Raises:
        Exception: If download fails
    """
    typer.echo("📥 Downloading image from URL...")
    
    # Headers to mimic browser request
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36')
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT) as response:
            content_type = response.headers.get('content-type', '')
            ext = get_image_extension(url, content_type)
            
            # Create temporary file
            temp_fd, temp_path = tempfile.mkstemp(
                suffix=ext, 
                prefix='ocr_image_'
            )
            
            try:
                with os.fdopen(temp_fd, 'wb') as temp_file:
                    temp_file.write(response.read())
                
                typer.echo(f"✅ Image downloaded: {Path(temp_path).name}")
                return temp_path
                
            except Exception:
                Path(temp_path).unlink(missing_ok=True)
                raise
                
    except urllib.error.HTTPError as e:
        raise Exception(f"HTTP error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise Exception(f"URL error: {e.reason}")
    except Exception as e:
        raise Exception(f"Download failed: {str(e)}")


def cleanup_temp_file(file_path: str) -> None:
    """
    Clean up temporary file if it exists.
    
    Args:
        file_path: Path to temporary file
    """
    try:
        path = Path(file_path)
        temp_dir = Path(tempfile.gettempdir())
        
        if file_path and path.exists() and temp_dir in path.parents:
            path.unlink()
    except Exception:
        pass  # Silent cleanup failure


def process_huggingface_model(
    image_path: str, 
    prompt: str, 
    model: str
) -> None:
    """
    Process image using Hugging Face SmolVLM model.
    
    Args:
        image_path: Path to image file
        prompt: User prompt for processing
        model: Model name to use
    """
    typer.echo("🔄 Loading SmolVLM vision model...")
    
    try:
        from PIL import Image
        from transformers import AutoProcessor, Idefics3ForConditionalGeneration
        import torch
        
        # Load model and processor
        processor = AutoProcessor.from_pretrained(model)
        vision_model = Idefics3ForConditionalGeneration.from_pretrained(
            model,
            dtype=(torch.float16 if torch.cuda.is_available() 
                   else torch.float32),
            device_map="auto" if torch.cuda.is_available() else "cpu",
            trust_remote_code=True
        )
        
        # Load and process image
        image = Image.open(image_path)
        
        # Create prompt for vision model
        messages = [{
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", 
                 "text": f"{prompt}\n\nPlease extract and transcribe "
                        "all text visible in this image."}
            ]
        }]
        
        # Process inputs
        text_input = processor.apply_chat_template(
            messages, 
            add_generation_prompt=True
        )
        inputs = processor(
            text=text_input,
            images=[image],
            return_tensors="pt",
            padding=True
        )
        
        # Move to device if GPU available
        if torch.cuda.is_available():
            inputs = {k: v.to(vision_model.device) for k, v in inputs.items()}
        
        # Generate response
        with torch.no_grad():
            generated_ids = vision_model.generate(
                **inputs,
                max_new_tokens=MAX_TOKENS,
                do_sample=False
            )
        
        # Decode response
        generated_text = processor.batch_decode(
            generated_ids[:, inputs["input_ids"].shape[1]:],
            skip_special_tokens=True
        )[0]
        
        # Display result
        typer.echo("\n🎉 Text extraction completed!")
        typer.echo("=" * 50)
        typer.echo(generated_text.strip())
        typer.echo("=" * 50)
        
    except ImportError as e:
        raise Exception(f"Hugging Face dependencies missing: {e}")


def process_with_tools(
    image_path: str, 
    prompt: str, 
    llm_with_tools
) -> None:
    """
    Process image using tool-based approach (OpenAI/Ollama).
    
    Args:
        image_path: Path to image file
        prompt: User prompt for processing
        llm_with_tools: Configured LLM with tools
    """
    react_graph = create_graph(llm_with_tools)
    
    messages = [HumanMessage(content=prompt)]
    result = react_graph.invoke({
        "messages": messages,
        "input_file": image_path
    })
    
    # Display result
    if result and "messages" in result and result["messages"]:
        final_message = result["messages"][-1]
        if hasattr(final_message, 'content'):
            typer.echo("\n🎉 Text extraction completed!")
            typer.echo("=" * 50)
            typer.echo(final_message.content)
            typer.echo("=" * 50)
        else:
            typer.echo("✅ Processing completed but no text content returned")
    else:
        typer.echo("⚠️  No response received from the AI model")


def validate_image_file(image_path: str) -> None:
    """
    Validate that the image file exists and has valid extension.
    
    Args:
        image_path: Path to image file
        
    Raises:
        typer.Exit: If file doesn't exist or user cancels
    """
    # Check if file exists
    if not Path(image_path).exists():
        typer.echo(f"❌ Error: Image file not found: {image_path}", err=True)
        typer.echo("💡 Please check the file path and try again", err=True)
        raise typer.Exit(1)
    
    # Check file extension
    if Path(image_path).suffix.lower() not in VALID_IMAGE_EXTENSIONS:
        typer.echo(f"⚠️  Warning: '{image_path}' may not be a valid "
                  "image file", err=True)
        if not typer.confirm("Continue anyway?"):
            raise typer.Exit(1)


def get_default_model(provider: str) -> str:
    """
    Get default model for the specified provider.
    
    Args:
        provider: AI provider name
        
    Returns:
        Default model name for the provider
        
    Raises:
        typer.Exit: If provider is unsupported
    """
    provider_lower = provider.lower()
    
    if provider_lower in DEFAULT_MODELS:
        return DEFAULT_MODELS[provider_lower]
    
    supported = "', '".join(DEFAULT_MODELS.keys())
    typer.echo(f"❌ Error: Unsupported provider '{provider}'. "
              f"Use: '{supported}'", err=True)
    raise typer.Exit(1)


def handle_processing_error(error: Exception, provider: str) -> None:
    """
    Handle and display appropriate error messages.
    
    Args:
        error: The exception that occurred
        provider: AI provider being used
    """
    error_str = str(error).lower()
    
    typer.echo(f"❌ Error during processing: {str(error)}", err=False)
    
    if "quota" in error_str or "429" in error_str:
        typer.echo("💡 API quota/billing issue", err=True)
        typer.echo("💡 Check your OpenAI account or try Ollama/SmolVLM", 
                  err=True)
    elif "connection" in error_str and provider.lower() == "ollama":
        typer.echo("💡 Make sure Ollama is running: 'ollama serve'", err=True)
        typer.echo("💡 And model is available: 'ollama pull llava:7b'", 
                  err=True)
    elif (provider.lower() == "huggingface" and 
          ("memory" in error_str or "cuda" in error_str)):
        typer.echo("💡 Model may need more memory or GPU", err=True)
        typer.echo("💡 Try: pixi run setup-smolvlm", err=True)
    elif provider.lower() == "huggingface":
        typer.echo("💡 Make sure dependencies are installed", err=True)
        typer.echo("💡 Run: pixi run setup-smolvlm", err=True)


@app.command()
def main_command(
    image_input: str = typer.Argument(
        ..., 
        help="Path to local image file or URL to image online"
    ),
    prompt: str = typer.Option(
        "Please transcribe the provided image.", 
        "--prompt", "-p",
        help="Custom prompt for the AI model"
    ),
    provider: str = typer.Option(
        "huggingface", 
        "--provider", "-m",
        help="Model provider: 'huggingface', 'ollama', or 'openai'"
    ),
    model: Optional[str] = typer.Option(
        None, 
        "--model",
        help="Specific model name (e.g., 'gpt-4o', 'llava:7b')"
    )
) -> None:
    """
    Extract text from an image using AI-powered OCR.
    
    This command processes an image file and extracts any text content using
    a vision-capable language model.
    
    Examples:
        # Local files with SmolVLM (default)
        python main.py image.png
        
        # Online images with URLs
        python main.py https://example.com/recipe.jpg
        python main.py https://example.com/doc.png --provider ollama
        
        # Different providers
        python main.py image.png --provider ollama --model llava:7b
        python main.py image.png --provider openai --model gpt-4o
        
        # Custom prompts with URLs
        python main.py https://example.com/receipt.jpg \\
            --prompt "Extract all prices"
    """
    extract_text_from_image(image_input, prompt, provider, model)


def extract_text_from_image(
    image_input: str, 
    prompt: str, 
    provider: str, 
    model: Optional[str]
) -> None:
    """
    Core function to extract text from image (local file or URL).
    
    Args:
        image_input: Path to local file or URL
        prompt: User prompt for processing
        provider: AI provider to use
        model: Specific model name (optional)
    """
    temp_file_path: Optional[str] = None
    
    try:
        # Handle URL input
        if is_url(image_input):
            typer.echo(f"🌐 Processing image from URL: {image_input}")
            temp_file_path = download_image_from_url(image_input)
            image_path = temp_file_path
        else:
            # Handle local file input
            image_path = image_input
            validate_image_file(image_path)
        
        # Set default model if not specified
        if model is None:
            model = get_default_model(provider)
        
        # Display processing info
        typer.echo(f"🔍 Processing image: {image_path}")
        typer.echo(f"💬 Using prompt: {prompt}")
        typer.echo(f"🤖 Model provider: {provider}")
        typer.echo(f"🧠 Model: {model}")
        
        # Process based on provider
        if provider.lower() == "huggingface":
            process_huggingface_model(image_path, prompt, model)
        else:
            # Get LLM and process with tools
            llm_with_tools = get_llm_with_tools(provider, model)
            process_with_tools(image_path, prompt, llm_with_tools)
            
    except Exception as e:
        handle_processing_error(e, provider)
        raise typer.Exit(1)
    
    finally:
        # Clean up temporary file if downloaded from URL
        if temp_file_path:
            cleanup_temp_file(temp_file_path)


if __name__ == "__main__":
    app()
