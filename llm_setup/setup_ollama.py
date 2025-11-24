#!/usr/bin/env python3
"""
Setup script for Ollama with vision models (moondream, llava, etc.).
Checks if Ollama is running and the model is available, downloads if needed.
Prioritizes moondream as the default efficient vision model.
"""

import subprocess
import sys
import time
import requests
import json
from pathlib import Path

# Note about model choices:
# - SmolVLM: Hugging Face model (not available in Ollama)
# - moondream: 1.8B parameter vision model (efficient, but NO tool support)
# - llava:7b: Vision model with function calling/tool support (REQUIRED for OCR agent)
# - bakllava:7b: Alternative LLaVA implementation with tool support
# We prioritize models that support function calling since our OCR agent uses tools

def check_ollama_running():
    """Check if Ollama service is running."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def start_ollama():
    """Start Ollama service."""
    print("🚀 Starting Ollama service...")
    try:
        # Try to start ollama serve in background
        process = subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            start_new_session=True
        )
        
        # Wait a bit for the service to start
        time.sleep(3)
        
        # Check if it's running
        if check_ollama_running():
            print("✅ Ollama service started successfully")
            return True
        else:
            print("❌ Failed to start Ollama service")
            return False
            
    except FileNotFoundError:
        print("❌ Ollama not found.")
        
        # Try to install on Linux
        import platform
        if platform.system().lower() == "linux":
            print("🤔 Would you like me to try installing Ollama? (y/n): ", end="")
            try:
                response = input().lower().strip()
                if response in ['y', 'yes']:
                    if quick_install_linux():
                        print("🔄 Retrying to start Ollama...")
                        return start_ollama()  # Recursive call after installation
                    else:
                        install_ollama_instructions()
                        return False
                else:
                    install_ollama_instructions()
                    return False
            except (EOFError, KeyboardInterrupt):
                print("\n⚠️  Installation cancelled")
                install_ollama_instructions()
                return False
        else:
            install_ollama_instructions()
            return False
    except Exception as e:
        print(f"❌ Error starting Ollama: {e}")
        return False

def list_ollama_models():
    """List available Ollama models."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=10)
        if response.status_code == 200:
            models = response.json().get("models", [])
            return [model["name"] for model in models]
        return []
    except Exception as e:
        print(f"❌ Error listing models: {e}")
        return []

def pull_model(model_name):
    """Pull/download a model using Ollama."""
    print(f"📥 Downloading model: {model_name}")
    print("   This may take several minutes...")
    
    try:
        # Use ollama pull command
        result = subprocess.run(
            ["ollama", "pull", model_name],
            capture_output=True,
            text=True,
            timeout=600  # 10 minutes timeout
        )
        
        if result.returncode == 0:
            print(f"✅ Model {model_name} downloaded successfully")
            return True
        else:
            print(f"❌ Failed to download model {model_name}")
            print(f"   Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"❌ Timeout downloading model {model_name}")
        return False
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        return False

def setup_ollama_with_model(model_name="llava:7b"):
    """Main setup function for Ollama with specified model."""
    print(f"🔧 Setting up Ollama with {model_name} model")
    print("=" * 50)
    
    # Step 1: Check if Ollama is running
    if not check_ollama_running():
        print("⚠️  Ollama service not running")
        if not start_ollama():
            return False
    else:
        print("✅ Ollama service is running")
    
    # Step 2: List available models
    print("\n📋 Checking available models...")
    available_models = list_ollama_models()
    
    # Check if our target model is available
    model_available = any(model_name in model for model in available_models)
    
    if model_available:
        print(f"✅ Model {model_name} is already available")
        print("   Available models:", ", ".join(available_models))
        return True
    else:
        print(f"⚠️  Model {model_name} not found locally")
        if available_models:
            print("   Available models:", ", ".join(available_models))
        else:
            print("   No models available locally")
        
        # Step 3: Download the model
        if pull_model(model_name):
            print(f"\n🎉 Setup complete! Model {model_name} is ready to use")
            return True
        else:
            return False

def test_model(model_name="llava:7b"):
    """Test the model with a simple prompt."""
    print(f"\n🧪 Testing model {model_name}...")
    
    try:
        # Simple test using requests
        payload = {
            "model": model_name,
            "prompt": "Say hello in one word.",
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Model test successful!")
            print(f"   Response: {result.get('response', 'No response')}")
            return True
        else:
            print(f"❌ Model test failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Model test error: {e}")
        return False

def install_ollama_instructions():
    """Provide instructions for installing Ollama."""
    print("\n📋 Ollama Installation Instructions:")
    print("=" * 40)
    print("🐧 Linux (Ubuntu/Debian):")
    print("   curl -fsSL https://ollama.ai/install.sh | sh")
    print()
    print("🍎 macOS:")
    print("   brew install ollama")
    print("   # or download from https://ollama.ai/download")
    print()
    print("🪟 Windows:")
    print("   Download from https://ollama.ai/download")
    print()
    print("📦 After installation:")
    print("   1. Open a new terminal")
    print("   2. Run: ollama serve")
    print("   3. Run this script again")
    print()

def quick_install_linux():
    """Attempt to install Ollama on Linux."""
    print("🚀 Attempting to install Ollama on Linux...")
    try:
        # Try to install Ollama using the official installer
        result = subprocess.run([
            "curl", "-fsSL", "https://ollama.ai/install.sh"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Pipe to shell
            install_result = subprocess.run([
                "sh"
            ], input=result.stdout, text=True, capture_output=True)
            
            if install_result.returncode == 0:
                print("✅ Ollama installed successfully!")
                return True
            else:
                print(f"❌ Installation failed: {install_result.stderr}")
                return False
        else:
            print(f"❌ Failed to download installer: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Installation error: {e}")
        return False

def main():
    """Main function."""
    # Use available Ollama vision models that support tools
    # Note: moondream doesn't support function calling/tools, so we prioritize LLaVA
    possible_models = [
        "llava:7b",       # LLaVA 7B model (supports tools)
        "bakllava:7b",    # BakLLaVA model (supports tools)
        "llava:13b",      # Larger LLaVA model (fallback)
        "moondream",      # Small model but no tool support
    ]
    
    model_name = possible_models[0]  # Start with llava:7b (supports tools)
    
    print("🤖 Ollama Setup Script")
    print(f"   Target model: {model_name} (Vision model with tool support for OCR)")
    print("   Note: Prioritizing models that support function calling/tools")
    print("   Fallback models available if needed")
    print("=" * 50)
    
    # Setup Ollama and model
    possible_models = [
        "llava:7b",       # LLaVA 7B model (supports tools)
        "bakllava:7b",    # BakLLaVA model (supports tools) 
        "llava:13b",      # Larger LLaVA model (fallback)
        "moondream",      # Small model but no tool support
    ]
    
    success = False
    used_model = None
    
    for model in possible_models:
        print(f"\n🔄 Trying model: {model}")
        if setup_ollama_with_model(model):
            # Test the model
            if test_model(model):
                print(f"\n🎉 Ollama setup completed successfully with {model}!")
                print(f"💡 You can now use: --provider ollama --model {model}")
                used_model = model
                success = True
                break
            else:
                print(f"\n⚠️  Model {model} downloaded but test failed, trying next...")
        else:
            print(f"\n❌ Failed to setup {model}, trying next...")
    
    if success:
        print(f"\n✅ Final model selected: {used_model}")
        # Update the default model in main.py if different from llava:7b
        if used_model != "llava:7b":
            print(f"💡 Consider updating DEFAULT_OLLAMA_MODEL to '{used_model}' in main.py")
        return True
    else:
        print("\n❌ All model attempts failed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
