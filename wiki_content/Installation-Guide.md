# Installation Guide

This guide will walk you through installing Vision Text Extractor and setting up all the AI providers.

## 📋 **Prerequisites**

### **System Requirements**
- **Operating System**: Linux, macOS, or Windows
- **Python**: 3.10+ (managed automatically by Pixi)
- **Memory**: 4GB RAM minimum, 8GB+ recommended for local models
- **Storage**: 3GB+ free space for all models
- **Internet**: Required for initial setup and cloud providers

### **Install Pixi**
Pixi is our dependency manager that makes installation seamless.

**Linux/macOS:**
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows (PowerShell):**
```powershell
iwr -useb https://pixi.sh/install.ps1 | iex
```

**Alternative methods**: See [pixi.sh](https://pixi.sh/latest/#installation)

## 🚀 **Quick Installation**

### **Step 1: Clone Repository**
```bash
git clone https://github.com/udit-asopa/vision-text-extractor.git
cd vision-text-extractor
```

### **Step 2: Install Dependencies**
```bash
pixi install
```

### **Step 3: Environment Setup**
```bash
# Copy environment template
pixi run setup-env

# Edit with your API keys (optional for local models)
nano .env  # or use your preferred editor
```

### **Step 4: Validate Installation**
```bash
pixi run test-setup
```

## 🤖 **AI Provider Setup**

### **Option 1: Hugging Face SmolVLM (Recommended for Beginners)**
- ✅ **Completely local** - no API keys needed
- ✅ **Privacy-focused** - data never leaves your machine
- ✅ **Free to use** - no usage limits

```bash
# Download SmolVLM model (~2GB)
pixi run setup-smolvlm

# Test it works
pixi run demo-ocr-huggingface
```

### **Option 2: Ollama LLaVA (Local Alternative)**
- ✅ **Local model** - privacy-focused
- ✅ **Different architecture** - good for comparison
- ✅ **Free to use**

```bash
# Install Ollama and LLaVA model
pixi run setup-ollama

# Test it works
pixi run demo-ocr-ollama
```

### **Option 3: OpenAI GPT-4o (Cloud-based)**
- ✅ **Highest accuracy** - state-of-the-art performance
- ❌ **Requires API key** - costs money per request
- ❌ **Internet required** - data sent to OpenAI

```bash
# Get API key from https://platform.openai.com/api-keys
# Add to .env file:
echo "OPENAI_API_KEY=your_key_here" >> .env

# Test it works
pixi run demo-ocr-openai
```

## ✅ **Verification**

### **Test All Components**
```bash
# Check dependencies
pixi run test-imports

# Test individual components
pixi run test-components

# Complete setup verification
pixi run setup
```

### **Quick Functionality Test**
```bash
# Test with sample image
pixi run demo-ocr-huggingface

# Test with your own image
python main.py path/to/your/image.jpg
```

## 🔧 **Advanced Installation**

### **Development Environment**
```bash
# Enter development mode with Jupyter
pixi shell -e dev
jupyter lab
```

### **GPU Acceleration (Optional)**
For faster SmolVLM processing with CUDA-compatible GPUs:

1. Ensure NVIDIA drivers are installed
2. CUDA will be automatically detected
3. Model will run on GPU if available

### **Custom Model Locations**
```bash
# Set custom Hugging Face cache directory
export HF_HOME=/path/to/custom/cache
pixi run setup-smolvlm
```

## 🚨 **Troubleshooting**

### **Common Issues**

**Pixi not found:**
```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export PATH="$HOME/.pixi/bin:$PATH"
source ~/.bashrc  # or restart terminal
```

**Permission errors:**
```bash
# On Linux/macOS, ensure execute permissions
chmod +x ~/.pixi/bin/pixi
```

**Out of memory with SmolVLM:**
```bash
# Use smaller batch size or switch to Ollama
pixi run demo-ocr-ollama
```

**OpenAI API errors:**
- Check API key is correct in `.env`
- Verify billing is set up on OpenAI account
- Check rate limits

### **Getting Help**
- Check [Troubleshooting](Troubleshooting) page
- Review [GitHub Issues](https://github.com/udit-asopa/vision-text-extractor/issues)
- Create new issue if problem persists

## ➡️ **Next Steps**

After successful installation:
1. 📖 Read [Quick Start Tutorial](Quick-Start-Tutorial)
2. 🎯 Try [Basic Usage](Basic-Usage) examples
3. 🔍 Explore [Use Case Tutorials](Document-Processing-Tutorial)

---

*Installation complete! Ready to extract text from images.* 🎉
