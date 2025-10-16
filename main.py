from typing import TypedDict, Optional, Annotated

from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from dotenv import load_dotenv

from agent.tools import (
    extract_text,
)

load_dotenv()

class AgentState(TypedDict):
    input_file: Optional[str]
    messages: Annotated[list[AnyMessage], add_messages]

tools = [
    extract_text,
]

llm = ChatOpenAI(model = "gpt-4o")
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

# llm = ChatOllama(model="qwen3:8b", temperature=0.7)
# llm_with_tools = llm.bind_tools(tools)

def assistant(state: AgentState):
    textual_description_of_tools = """
    def extract_text(img_path: str) -> str:
        Extracts text from an image specified by its file path. This function reads the
        image file, encodes the image data as base64, sends the image content to a
        vision-capable language model to extract text, and returns the resulting text
        content.
    
        :param img_path: The file path of the image from which text is to be extracted.
        :type img_path: str
        :return: Extracted text from the image, or an empty string if an error occurs
            during the process.
        :rtype: str
        :raises Exception: If any error occurs during image reading, encoding,
            or processing the response from the model.
    """

    image = state["input_file"]
    sys_msg = SystemMessage(content = f"""
    You are a helpful assistant. You can analyse documents with provided tools:\n{textual_description_of_tools}.
    
    You have access to some optional images. Currently the loaded image is: {image}""")

    return {
        "messages": [llm_with_tools.invoke([sys_msg] + state["messages"])],
        "input_file": state["input_file"]
    }

builder = StateGraph(AgentState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    tools_condition
)
builder.add_edge("tools", "assistant")
react_graph = builder.compile()

if __name__ == "__main__":
    user_prompt = "Please transcribe the provided image."

    messages = [HumanMessage(content=user_prompt)]
    messages = react_graph.invoke(({
        "messages": messages,
        "input_file": "images/chocolate_cake_recipe.png"
    }))