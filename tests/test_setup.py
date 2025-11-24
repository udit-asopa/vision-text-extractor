#!/usr/bin/env python3
"""
Simple test script to verify the OCR LLM Agent dependencies are working.
"""

import sys
import traceback

def test_imports():
    """Test all required imports for the OCR LLM Agent."""
    
    print("🔍 Testing OCR LLM Agent dependencies...")
    
    try:
        print("  ✅ Standard library imports...")
        import os
        import base64
        import tempfile
        from typing import TypedDict, Optional, Annotated
        
        print("  ✅ Core data science imports...")
        import numpy as np
        import cv2
        
        print("  ✅ Environment management...")
        from dotenv import load_dotenv
        
        print("  ✅ LangChain Core...")
        from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage
        from langchain_core.tools import tool
        
        print("  ✅ LangChain LLM providers...")
        from langchain_openai import ChatOpenAI
        from langchain_ollama import ChatOllama
        
        print("  ✅ LangGraph...")
        from langgraph.graph import StateGraph, START
        from langgraph.graph.message import add_messages
        from langgraph.prebuilt import ToolNode, tools_condition
        
        print("\n🎉 All dependencies imported successfully!")
        print("🚀 Your OCR LLM Agent is ready to run!")
        
        return True
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("🔧 Try running: pixi install")
        return False
        
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        traceback.print_exc()
        return False

def show_environment_info():
    """Show environment configuration info."""
    print("\n📋 Environment Information:")
    print("=" * 50)
    
    # Check Python version
    print(f"🐍 Python: {sys.version.split()[0]}")
    
    # Check OpenCV version
    try:
        import cv2
        print(f"👁️  OpenCV: {cv2.__version__}")
    except:
        print("❌ OpenCV: Not available")
    
    # Check if environment variables are set
    import os
    openai_key = "✅ Set" if os.getenv("OPENAI_API_KEY") else "❌ Not set"
    print(f"🔑 OPENAI_API_KEY: {openai_key}")
    
    print("\n💡 Next steps:")
    if not os.getenv("OPENAI_API_KEY"):
        print("   1. Copy .env.example to .env")
        print("   2. Add your OpenAI API key to .env")
        print("   3. Run: pixi run ocr_llm")
    else:
        print("   Ready to run: pixi run ocr_llm")

if __name__ == "__main__":
    if test_imports():
        show_environment_info()
    else:
        sys.exit(1)
