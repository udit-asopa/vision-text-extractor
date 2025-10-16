#!/usr/bin/env python3
"""
Setup and validation script for OCR LLM Agent with proper .env loading.
"""

import os
import sys
import shutil
from pathlib import Path

def setup_env_file():
    """Create .env file from template if it doesn't exist."""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists() and env_example.exists():
        print("📝 Creating .env file from template...")
        shutil.copy(env_example, env_file)
        print("✅ .env file created! Please edit it with your API keys.")
        return True
    elif env_file.exists():
        print("✅ .env file already exists")
        return True
    else:
        print("❌ No .env.example file found to copy from")
        return False

def load_and_check_env():
    """Load .env file and check environment variables."""
    try:
        from dotenv import load_dotenv
        
        # Load .env file
        load_dotenv()
        
        print("\n🔑 Environment Variables:")
        print("=" * 30)
        
        # Check OpenAI API key
        openai_key = os.getenv("OPENAI_API_KEY")
        if openai_key:
            print(f"✅ OPENAI_API_KEY: Set (length: {len(openai_key)})")
        else:
            print("❌ OPENAI_API_KEY: Not set")
            print("💡 Add your OpenAI API key to .env file")
        
        # Check Ollama URL
        ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        print(f"🔗 OLLAMA_BASE_URL: {ollama_url}")
        
        return openai_key is not None
        
    except ImportError:
        print("❌ python-dotenv not installed")
        return False

def test_imports():
    """Test all required imports."""
    print("\n🔍 Testing dependencies...")
    
    try:
        # Standard library
        import base64, tempfile, os
        from typing import TypedDict, Optional, Annotated
        print("  ✅ Standard library")
        
        # Data science
        import numpy as np
        import cv2
        print("  ✅ NumPy & OpenCV")
        
        # Environment
        from dotenv import load_dotenv
        print("  ✅ python-dotenv")
        
        # LangChain
        from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage
        from langchain_core.tools import tool
        from langchain_openai import ChatOpenAI
        from langchain_ollama import ChatOllama
        print("  ✅ LangChain packages")
        
        # LangGraph
        from langgraph.graph import StateGraph, START
        from langgraph.graph.message import add_messages
        from langgraph.prebuilt import ToolNode, tools_condition
        print("  ✅ LangGraph")
        
        print("\n🎉 All dependencies imported successfully!")
        return True
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        return False

def show_next_steps(env_loaded):
    """Show next steps based on setup status."""
    print("\n🚀 Next Steps:")
    print("=" * 30)
    
    if not env_loaded:
        print("1. Edit .env file and add your OpenAI API key:")
        print("   OPENAI_API_KEY=your_key_here")
        print("2. Test the setup: pixi run check-env")
        print("3. Run the agent: pixi run ocr_llm")
    else:
        print("✅ Setup complete! You can now:")
        print("   • pixi run ocr_llm      - Run the OCR agent")
        print("   • pixi run test-setup   - Run this setup test again")
        print("   • pixi run check-env    - Check environment variables")
        print("   • pixi shell            - Enter the pixi environment")

def main():
    """Main setup and validation function."""
    print("🔧 OCR LLM Agent Setup & Validation")
    print("=" * 40)
    
    # Setup environment file
    setup_success = setup_env_file()
    
    # Test imports
    imports_success = test_imports()
    
    # Load and check environment
    env_success = load_and_check_env()
    
    # Show next steps
    show_next_steps(env_success)
    
    # Return overall success
    return setup_success and imports_success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
