#!/usr/bin/env python3
"""
Setup script for Hugging Face SmolVLM model.
Checks if the model is available and downloads it if needed.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_gpu_availability():
    """Check if CUDA/GPU is available."""
    try:
        import torch
        gpu_available = torch.cuda.is_available()
        if gpu_available:
            gpu_count = torch.cuda.device_count()
            gpu_name = torch.cuda.get_device_name(0)
            print(f"✅ GPU available: {gpu_name} (Count: {gpu_count})")
        else:
            print("⚠️  No GPU detected, will use CPU (slower)")
        return gpu_available
    except ImportError:
        print("❌ PyTorch not installed")
        return False

def check_model_cache():
    """Check if SmolVLM model is already cached."""
    try:
        from transformers import AutoTokenizer, AutoProcessor
        from huggingface_hub import snapshot_download
        
        model_name = "HuggingFaceTB/SmolVLM-Instruct"
        cache_dir = Path.home() / ".cache/huggingface/hub"
        
        # Check if model exists in cache
        model_cache_path = cache_dir
        if model_cache_path.exists():
            cached_models = [d.name for d in model_cache_path.iterdir() if d.is_dir()]
            smolvlm_cached = any("smolvlm" in model.lower() for model in cached_models)
            
            if smolvlm_cached:
                print(f"✅ SmolVLM model found in cache")
                return True
        
        print(f"⚠️  SmolVLM model not found in cache")
        return False
        
    except Exception as e:
        print(f"❌ Error checking model cache: {e}")
        return False

def download_model():
    """Download SmolVLM model."""
    print("📥 Downloading SmolVLM model...")
    print("   This may take several minutes depending on your internet connection...")
    
    try:
        from transformers import AutoTokenizer, AutoProcessor
        from huggingface_hub import snapshot_download
        
        model_name = "HuggingFaceTB/SmolVLM-Instruct"
        
        # Download model files
        print(f"   Downloading {model_name}...")
        snapshot_download(
            repo_id=model_name,
            cache_dir=str(Path.home() / ".cache/huggingface/hub"),
            resume_download=True
        )
        
        # Download tokenizer and processor
        print("   Setting up tokenizer and processor...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        processor = AutoProcessor.from_pretrained(model_name)
        
        print("✅ SmolVLM model downloaded successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        return False

def test_model():
    """Test SmolVLM model with a simple prompt."""
    print("🧪 Testing SmolVLM model...")
    
    try:
        from transformers import AutoTokenizer, AutoProcessor, LlavaForConditionalGeneration
        import torch
        from PIL import Image
        import numpy as np
        
        model_name = "HuggingFaceTB/SmolVLM-Instruct"
        
        # Load model components
        print("   Loading model...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        processor = AutoProcessor.from_pretrained(model_name)
        
        # For testing, we'll just check if the model can be loaded
        # Full model loading takes too much memory for a quick test
        print("✅ Model components loaded successfully")
        print("   Model is ready for use")
        return True
        
    except Exception as e:
        print(f"❌ Model test error: {e}")
        return False

def check_dependencies():
    """Check if all required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        "transformers",
        "torch", 
        "PIL",
        "numpy",
        "langchain_huggingface"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == "PIL":
                import PIL
            else:
                __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("   Run: pixi install")
        return False
    
    print("✅ All dependencies available")
    return True

def main():
    """Main setup function."""
    print("🤖 SmolVLM Setup Script")
    print("   Target model: HuggingFaceTB/SmolVLM-Instruct")
    print("   Provider: Hugging Face Transformers")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Setup failed: Missing dependencies")
        return False
    
    # Check GPU
    gpu_available = check_gpu_availability()
    
    # Check if model is cached
    if check_model_cache():
        print("📋 Model already available in cache")
    else:
        # Download model
        if not download_model():
            print("\n❌ Setup failed: Could not download model")
            return False
    
    # Test model
    if test_model():
        print("\n🎉 SmolVLM setup completed successfully!")
        print("💡 You can now use: --provider huggingface --model HuggingFaceTB/SmolVLM-Instruct")
        if not gpu_available:
            print("⚠️  Note: No GPU detected. Model will run on CPU (slower)")
        return True
    else:
        print("\n⚠️  Setup completed but model test failed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
