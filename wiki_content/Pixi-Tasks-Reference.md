# Pixi Tasks Reference

Complete reference for all available Pixi tasks in Vision Text Extractor. These tasks provide convenient shortcuts for common operations.

## 🚀 **Quick Task Overview**

```bash
# List all available tasks
pixi task list

# Get help for any task
pixi run <task-name> --help
```

## 📋 **Task Categories**

### **🔧 Setup & Installation**
- [`setup`](#setup) - Complete system validation
- [`setup-ollama`](#setup-ollama) - Install Ollama and LLaVA
- [`setup-smolvlm`](#setup-smolvlm) - Download SmolVLM model
- [`setup-env`](#setup-env) - Create environment file
- [`install-deps`](#install-deps) - Install dependencies

### **🤖 OCR Processing**
- [`ocr_llm`](#ocr_llm) - General purpose OCR (flexible)
- [`ocr_ollama`](#ocr_ollama) - Ollama LLaVA OCR (flexible)
- [`ocr_smolvlm`](#ocr_smolvlm) - SmolVLM OCR (flexible)
- [`ocr_url_example`](#ocr_url_example) - Test with online image

### **🎯 Demo Commands**
- [`demo-ocr-huggingface`](#demo-ocr-huggingface) - SmolVLM demo
- [`demo-ocr-ollama`](#demo-ocr-ollama) - Ollama demo
- [`demo-ocr-openai`](#demo-ocr-openai) - OpenAI demo

### **✅ Testing & Validation**
- [`test-setup`](#test-setup) - Validate dependencies
- [`test-components`](#test-components) - Test functionality
- [`test-imports`](#test-imports) - Check imports
- [`check-env`](#check-env) - Verify environment variables

### **🔄 Utility Tasks**
- [`clean`](#clean) - Clean cache and temporary files

## 📖 **Detailed Task Reference**

---

### **Setup & Installation Tasks**

#### `setup`
**Purpose**: Complete system validation and setup
```bash
pixi run setup
```
- ✅ Validates all dependencies
- ✅ Tests all AI providers
- ✅ Checks environment configuration
- ✅ Provides setup recommendations

**Dependencies**: None  
**Time**: 30-60 seconds  

---

#### `setup-ollama`
**Purpose**: Install Ollama and download LLaVA model
```bash
pixi run setup-ollama
```
- 📥 Downloads and installs Ollama
- 📥 Pulls LLaVA 7B model (~4GB)
- ✅ Configures Ollama service
- ✅ Tests model functionality

**Dependencies**: Internet connection  
**Time**: 5-15 minutes (depending on internet speed)  
**Disk Space**: ~4GB

---

#### `setup-smolvlm`
**Purpose**: Download Hugging Face SmolVLM model
```bash
pixi run setup-smolvlm
```
- 📥 Downloads SmolVLM-Instruct model (~2GB)
- ✅ Configures Hugging Face cache
- ✅ Tests model loading
- ✅ Validates CUDA availability (if applicable)

**Dependencies**: Internet connection  
**Time**: 3-10 minutes  
**Disk Space**: ~2GB

---

#### `setup-env`
**Purpose**: Create environment configuration file
```bash
pixi run setup-env
```
- 📄 Copies `.env.example` to `.env`
- ⚠️ Won't overwrite existing `.env`
- 📝 You must manually edit API keys

**Dependencies**: None  
**Time**: < 1 second

---

#### `install-deps`
**Purpose**: Install or refresh all dependencies
```bash
pixi run install-deps
```
- 📦 Equivalent to `pixi install`
- 🔄 Useful for refreshing dependencies
- ✅ Validates environment

**Dependencies**: Internet connection  
**Time**: 1-5 minutes

---

### **OCR Processing Tasks**

#### `ocr_llm`
**Purpose**: Flexible OCR using SmolVLM (requires image argument)
```bash
pixi run ocr_llm "path/to/image.jpg"
pixi run ocr_llm "https://example.com/image.png"
```
- 🤖 Uses Hugging Face SmolVLM by default
- 📁 Accepts local files or URLs
- ⚙️ Requires prior `setup-smolvlm`

**Arguments**: Image path (required)  
**Dependencies**: `setup-smolvlm`

---

#### `ocr_ollama`
**Purpose**: Flexible OCR using Ollama LLaVA (requires image argument)
```bash
pixi run ocr_ollama "path/to/image.jpg"
```
- 🤖 Uses Ollama LLaVA model
- 📁 Accepts local files or URLs
- ⚙️ Add `--provider ollama --model llava:7b` for explicit control

**Arguments**: Image path (required)  
**Dependencies**: Manual Ollama setup or `setup-ollama`

---

#### `ocr_smolvlm`
**Purpose**: Explicit SmolVLM OCR (requires image argument)
```bash
pixi run ocr_smolvlm "path/to/image.jpg"
```
- 🤖 Explicitly uses SmolVLM provider
- 📁 Accepts local files or URLs
- ⚙️ Identical to `ocr_llm` but more explicit

**Arguments**: Image path (required)  
**Dependencies**: `setup-smolvlm`

---

#### `ocr_url_example`
**Purpose**: Test OCR with a fixed online image
```bash
pixi run ocr_url_example
```
- 🌐 Uses fixed recipe image URL
- ✅ Good for testing URL functionality
- 🔍 No arguments needed

**Arguments**: None  
**Dependencies**: `setup-smolvlm`, Internet connection

---

### **Demo Commands**

#### `demo-ocr-huggingface`
**Purpose**: Quick SmolVLM demo with sample image
```bash
pixi run demo-ocr-huggingface
```
- 🖼️ Uses `images/chocolate_cake_recipe.png`
- 🤖 Hugging Face SmolVLM provider
- ✅ Perfect for testing after installation

**Arguments**: None  
**Dependencies**: `setup-smolvlm`

---

#### `demo-ocr-ollama`
**Purpose**: Quick Ollama demo with sample image
```bash
pixi run demo-ocr-ollama
```
- 🖼️ Uses `images/chocolate_cake_recipe.png`
- 🤖 Ollama LLaVA 7B model
- ✅ Good for comparing with SmolVLM

**Arguments**: None  
**Dependencies**: `setup-ollama`

---

#### `demo-ocr-openai`
**Purpose**: Quick OpenAI demo with sample image
```bash
pixi run demo-ocr-openai
```
- 🖼️ Uses `images/chocolate_cake_recipe.png`
- 🤖 OpenAI GPT-4o model
- 🔑 Requires valid API key in `.env`

**Arguments**: None  
**Dependencies**: OpenAI API key in `.env`

---

### **Testing & Validation Tasks**

#### `test-setup`
**Purpose**: Validate all dependencies are working
```bash
pixi run test-setup
```
- ✅ Tests Python imports
- ✅ Validates core libraries
- ✅ Checks environment setup
- 📊 Provides detailed status report

**Arguments**: None  
**Dependencies**: None

---

#### `test-components`
**Purpose**: Test actual functionality without API calls
```bash
pixi run test-components
```
- 🖼️ Tests image loading
- 📁 Validates file paths
- 🔧 Tests component integration
- ⚠️ No actual AI model calls

**Arguments**: None  
**Dependencies**: None

---

#### `test-imports`
**Purpose**: Quick import validation
```bash
pixi run test-imports
```
- ⚡ Fast dependency check
- 📦 Tests critical imports only
- ✅ Good for CI/CD pipelines

**Arguments**: None  
**Dependencies**: None

---

#### `check-env`
**Purpose**: Verify environment variables
```bash
pixi run check-env
```
- 🔑 Checks OpenAI API key status
- 📄 Validates `.env` file
- ⚠️ Shows which keys are set/missing

**Arguments**: None  
**Dependencies**: None

---

### **Utility Tasks**

#### `clean`
**Purpose**: Clean cache and temporary files
```bash
pixi run clean
```
- 🧹 Removes `.pixi` cache
- 🗑️ Cleans Python `__pycache__` directories
- 💾 Frees up disk space
- ⚠️ Safe to run anytime

**Arguments**: None  
**Dependencies**: None

---

## 🔄 **Task Workflows**

### **First-Time Setup**
```bash
# Complete installation and setup
pixi install
pixi run setup-env          # Create .env file
pixi run setup-smolvlm      # Download SmolVLM (recommended)
pixi run test-setup         # Validate everything
pixi run demo-ocr-huggingface  # Test with sample
```

### **Daily Usage**
```bash
# Process your images
pixi run ocr_llm "my-document.pdf"
pixi run ocr_ollama "receipt.jpg"

# Compare providers
pixi run demo-ocr-huggingface
pixi run demo-ocr-ollama
pixi run demo-ocr-openai
```

### **Troubleshooting**
```bash
# Diagnose issues
pixi run test-imports       # Check dependencies
pixi run test-components    # Test functionality
pixi run check-env          # Verify API keys
pixi run clean             # Clear cache if needed
```

### **Development**
```bash
# Enter development environment
pixi shell -e dev
jupyter lab

# Test changes
pixi run test-setup
pixi run test-components
```

## 💡 **Pro Tips**

### **Task Chaining**
```bash
# Run multiple tasks in sequence
pixi run setup-smolvlm && pixi run demo-ocr-huggingface

# Conditional execution
pixi run test-setup && pixi run ocr_llm "image.jpg"
```

### **Custom Arguments**
```bash
# Most tasks accept additional arguments
pixi run ocr_llm "image.jpg" --prompt "Extract specific data"
pixi run demo-ocr-huggingface --prompt "Focus on ingredients only"
```

### **Environment Variables**
```bash
# Set custom cache locations
HF_HOME=/custom/path pixi run setup-smolvlm
OLLAMA_MODELS=/custom/path pixi run setup-ollama
```

---

*This reference covers all available Pixi tasks. Use these shortcuts to streamline your Vision Text Extractor workflow!*
