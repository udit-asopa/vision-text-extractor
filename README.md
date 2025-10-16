# OCR LLM Agent

A multi-provider OCR agent that extracts text from images using 
vision-capable AI models. Supports both local files and online URLs 
with three AI provider options for maximum flexibility.

## ⚠️ Security Notice

**IMPORTANT**: Your `.env` file contains sensitive API keys and should 
**NEVER** be committed to version control.

- ✅ The `.env` file is already included in `.gitignore`
- ✅ Only `.env.example` (with placeholder values) should be committed
- ✅ Always use placeholder values in `.env.example`
- ❌ Never share your actual API keys in public repositories

## Features

- **Multi-Provider OCR** with three AI options:
  - **Hugging Face SmolVLM** - Local vision model, privacy-focused (default)
  - **Ollama LLaVA** - Local model, no API key needed
  - **OpenAI GPT-4o** - Cloud-based, high accuracy (requires API key)
- **URL Support** - Process images directly from web URLs
- **Image preprocessing** with OpenCV (threshold, deskew operations)
- **Unit conversions** for cooking and measurements
- **Flexible CLI** with Typer for easy command-line usage
- **Type-safe** codebase with comprehensive type hints

## Project Structure

```
ocr-llm-agent/
├── agent/                          # Core agent functionality
│   └── tools.py                    # OCR text extraction tools
├── additions/                      # Additional tools (optional)
│   ├── additions_1_opencv.py       # Image preprocessing tools
│   ├── additions_2_temperature.py  # Temperature conversion
│   └── additions_3_unit_conversions.py # Unit conversion tools
├── images/                         # Sample test images
│   └── chocolate_cake_recipe.png   # Default test image
├── llm_setup/                      # AI model setup scripts
│   ├── setup_ollama.py            # Ollama installation & setup
│   ├── setup_smolvlm.py           # SmolVLM download & setup
│   └── setup_and_test.py          # Combined setup script
├── tests/                          # Test and validation scripts
│   ├── test_setup.py               # Dependency validation
│   └── test_components.py          # Component testing
├── main.py                         # Main CLI application
├── pixi.toml                       # Pixi dependency management
├── pixi.lock                       # Locked dependencies
├── setup.sh                        # Interactive setup script
├── .env.example                    # Environment template
├── .env                           # Your API keys (git-ignored)
└── README.md                       # This file
```

## Setup with Pixi

This project uses [pixi](https://pixi.sh) for dependency management.

### Prerequisites

1. Install pixi: https://pixi.sh/latest/#installation
2. Clone this repository

### Installation

1. **Install dependencies:**
   ```bash
   pixi install
   ```

2. **Set up environment variables:**
   ```bash
   # Copy the environment template
   pixi run setup-env
   
   # Edit .env with your API keys
   nano .env  # or use your preferred editor
   ```

3. **Test the installation:**
   ```bash
   pixi run setup
   ```

### Usage

#### Quick setup and test:
```bash
pixi run setup
```

#### Run the OCR agent with different AI providers:

**Hugging Face SmolVLM (local, no API key needed, default):**
```bash
# Default provider - uses Hugging Face SmolVLM
pixi run ocr_llm images/chocolate_cake_recipe.png
# Or use the demo command
pixi run demo-ocr-huggingface
python main.py myimage.png  # Uses SmolVLM by default
python main.py myimage.png --provider huggingface --model HuggingFaceTB/SmolVLM-Instruct
```

**Ollama LLaVA (local, no API key needed):**
```bash
# Setup Ollama first (one-time)
pixi run setup-ollama

# Use Ollama LLaVA
pixi run ocr_ollama images/chocolate_cake_recipe.png --provider ollama --model llava:7b
# Or use the demo command
pixi run demo-ocr-ollama
python main.py myimage.png --provider ollama --model llava:7b
```

**OpenAI GPT-4o (requires API key):**
```bash
# Use OpenAI GPT-4o
pixi run demo-ocr-openai  # Uses sample image
python main.py myimage.png --provider openai --model gpt-4o
```

**Custom prompts and options:**
```bash
# Use custom prompts with any provider
python main.py receipt.jpg --prompt "Extract all prices and items" --provider smolvlm
python main.py document.png -p "Summarize the main points" --provider ollama

# Get help and see all options
python main.py --help
```

#### Check environment setup:
```bash
pixi run check-env
```

#### Development mode (with Jupyter):
```bash
pixi shell -e dev
jupyter lab
```

### Available Tasks

**Setup Commands:**
- `pixi run setup` - Complete setup validation
- `pixi run setup-ollama` - Install Ollama + LLaVA model
- `pixi run setup-smolvlm` - Download SmolVLM model (~2GB)
- `pixi run test-setup` - Validate all dependencies

**OCR Commands (flexible - accept file arguments):**
- `pixi run ocr_llm [image_path]` - SmolVLM OCR (requires image argument)
- `pixi run ocr_ollama [image_path]` - Ollama LLaVA OCR (requires image argument)
- `pixi run ocr_smolvlm [image_path]` - SmolVLM OCR explicit (requires image argument)
- `pixi run ocr_url_example` - Test with online image (fixed URL)

**Demo Commands (with sample image):**
- `pixi run demo-ocr-huggingface` - SmolVLM with sample image
- `pixi run demo-ocr-ollama` - Ollama with sample image
- `pixi run demo-ocr-openai` - OpenAI with sample image

**Development:**
- `pixi run test-components` - Test individual components
- `pixi run clean` - Clean cache and temporary files
- `pixi shell -e dev` - Enter development environment with Jupyter

### Basic Usage

```bash
# Default provider (SmolVLM) with local image
python main.py images/chocolate_cake_recipe.png

# Same with custom prompt
python main.py images/recipe.png --prompt "Extract ingredients only"
```

### URL Processing

```bash
# Process image from URL
python main.py "https://example.com/receipt.jpg"

# URL with custom prompt
python main.py "https://example.com/menu.png" \
    --prompt "Extract prices and menu items"

# Quick test with sample URL
pixi run ocr_url_example
```

### Provider Selection

```bash
# Hugging Face SmolVLM (default, local, private)
python main.py image.png --provider huggingface

# Ollama LLaVA (local, no API key needed)
python main.py image.png --provider ollama --model llava:7b

# OpenAI GPT-4o (cloud, requires API key)
python main.py image.png --provider openai --model gpt-4o
```

### Pixi Tasks (Convenient Shortcuts)

```bash
# Quick demo tests with sample images (no arguments needed)
pixi run demo-ocr-huggingface    # SmolVLM with sample image
pixi run demo-ocr-ollama         # LLaVA with sample image
pixi run demo-ocr-openai         # GPT-4o with sample image

# Flexible tasks (provide your own image path)
pixi run ocr_llm path/to/your/image.png
pixi run ocr_ollama path/to/your/image.jpg --provider ollama
pixi run ocr_smolvlm path/to/your/image.png --provider huggingface

# URL processing
pixi run ocr_url_example         # Fixed online image example

# Setup and validation
pixi run setup-smolvlm           # Download SmolVLM model
pixi run setup-ollama            # Install Ollama + LLaVA
pixi run test-setup              # Validate installation
```

### Using Flexible Pixi Tasks

The updated pixi tasks now accept file paths as arguments, making them more flexible:

```bash
# Basic usage - main OCR tasks (require image path argument)
pixi run ocr_llm "path/to/your/image.jpg"
pixi run ocr_ollama "path/to/your/image.png" 
pixi run ocr_smolvlm "https://example.com/image.jpg"

# Demo tasks - include sample image (no arguments needed)
pixi run demo-ocr-huggingface   # Uses images/chocolate_cake_recipe.png
pixi run demo-ocr-ollama        # Uses images/chocolate_cake_recipe.png  
pixi run demo-ocr-openai        # Uses images/chocolate_cake_recipe.png

# Advanced usage with additional options
pixi run ocr_llm "my-document.pdf" --prompt "Extract key information"
pixi run ocr_ollama "receipt.jpg" --prompt "Extract total amount"

# Examples with different images in the project
pixi run ocr_llm images/handwriting_sample.webp
pixi run ocr_ollama images/Acroplis-Athens.webp
pixi run demo-ocr-huggingface  # Always uses the chocolate cake recipe
```

**Key Differences:**
- **Flexible tasks** (`ocr_llm`, `ocr_ollama`, `ocr_smolvlm`) - Require image path argument
- **Demo tasks** (`demo-ocr-*`) - Use fixed sample image for quick testing
- **URL example** (`ocr_url_example`) - Fixed online image for testing URL functionality

## Example Use Cases

### 📄 Document Processing & Business

```bash
# Scanned document digitization
python main.py scanned-contract.png \
    --prompt "Extract all text while preserving structure and formatting"

# Business card data extraction
python main.py "https://example.com/business-card.jpg" \
    --prompt "Extract name, title, company, email, phone, and address"

# Form processing and validation
python main.py filled-application.png \
    --prompt "Extract all form field names and their filled values"

# Legal document analysis
python main.py legal-document.pdf \
    --prompt "Extract key clauses, dates, parties, and terms"

# Insurance claim processing
python main.py insurance-form.jpg \
    --prompt "Extract claim number, policy details, and incident description"
```

### 🍽️ Food & Restaurant Industry

```bash
# Recipe digitization from cookbooks
python main.py cookbook-page.jpg \
    --prompt "Extract recipe title, ingredients with measurements, and step-by-step instructions"

# Restaurant menu digitization
python main.py restaurant-menu.png \
    --prompt "Create structured list: category, item name, description, price"

# Nutritional label analysis
python main.py nutrition-facts.jpg \
    --prompt "Extract serving size, calories, and all nutritional values per serving"

# Food packaging compliance
python main.py food-label.png \
    --prompt "Extract ingredients list, allergen warnings, and expiration dates"

# Kitchen inventory management
python main.py pantry-labels.jpg \
    --prompt "List all food items with expiration dates and quantities"
```

### 💰 Financial & Accounting

```bash
# Expense management from receipts
python main.py receipt-collection.jpg \
    --prompt "Extract date, merchant, items purchased, tax amount, and total for each receipt"

# Invoice data extraction for accounting
python main.py "https://vendor.com/invoice-2024.pdf" \
    --prompt "Extract invoice #, date, vendor details, line items, subtotal, tax, and total due"

# Bank statement processing
python main.py bank-statement.png \
    --prompt "Extract all transactions with date, description, amount, and running balance"

# Credit card statement analysis
python main.py cc-statement.pdf \
    --prompt "Identify all charges, payments, fees, and interest charges with dates"

# Tax document preparation
python main.py tax-documents.jpg \
    --prompt "Extract W-2 information: employer, wages, taxes withheld, and other deductions"
```

### 📚 Education & Research

```bash
# Academic paper digitization
python main.py research-paper.pdf \
    --prompt "Extract abstract, methodology, key findings, and conclusion sections"

# Student homework processing
python main.py math-homework.jpg \
    --prompt "Extract all math problems, student answers, and any teacher corrections"

# Lecture note transcription
python main.py whiteboard-notes.png \
    --prompt "Organize notes by topic headings, bullet points, and key concepts"

# Textbook content extraction
python main.py textbook-chapter.jpg \
    --prompt "Extract chapter content, ignoring page numbers, headers, and footnotes"

# Exam and quiz processing
python main.py exam-paper.png \
    --prompt "Extract questions, multiple choice options, and student responses"
```

### 🏥 Healthcare & Medical

```bash
# Medical prescription analysis
python main.py prescription.jpg \
    --prompt "Extract patient name, medication names, dosages, frequency, and prescriber info"

# Lab result processing
python main.py lab-results.pdf \
    --prompt "Extract test names, values, reference ranges, and abnormal flags"

# Medical form digitization
python main.py patient-intake.png \
    --prompt "Extract patient demographics, medical history, and insurance information"

# Pharmacy label processing
python main.py pill-bottle.jpg \
    --prompt "Extract medication name, strength, quantity, directions, and pharmacy details"
```

### 🚗 Transportation & Logistics

```bash
# License plate recognition
python main.py license-plates.jpg \
    --prompt "Extract all visible license plate numbers and their states/countries"

# Shipping label processing
python main.py shipping-labels.png \
    --prompt "Extract tracking numbers, addresses, shipping method, and delivery dates"

# Vehicle inspection reports
python main.py inspection-report.pdf \
    --prompt "Extract vehicle details, inspection items, pass/fail status, and inspector notes"

# Parking ticket processing
python main.py parking-ticket.jpg \
    --prompt "Extract violation type, location, date/time, fine amount, and vehicle info"
```

### 🏠 Real Estate & Property

```bash
# Property listing analysis
python main.py listing-flyer.jpg \
    --prompt "Extract property address, price, square footage, bedrooms, bathrooms, and features"

# Lease agreement processing
python main.py lease-document.pdf \
    --prompt "Extract lease term, monthly rent, security deposit, and key lease conditions"

# Property inspection reports
python main.py inspection-checklist.png \
    --prompt "Extract room-by-room condition notes, repair needs, and overall assessment"

# HOA document processing
python main.py hoa-notice.jpg \
    --prompt "Extract meeting dates, agenda items, fee changes, and important announcements"
```

### 📊 Market Research & Analytics

```bash
# Survey response digitization
python main.py survey-forms.png \
    --prompt "Extract all questions and corresponding handwritten responses"

# Competitor pricing analysis
python main.py competitor-prices.jpg \
    --prompt "Create price comparison table with product names and prices"

# Customer feedback processing
python main.py feedback-cards.jpg \
    --prompt "Extract customer comments, ratings, and suggestions for improvement"

# Product catalog digitization
python main.py catalog-page.png \
    --prompt "Extract product names, descriptions, specifications, and pricing information"
```

## Configuration

### Provider Setup

**Hugging Face SmolVLM (Local, Default)**
1. Setup: `pixi run setup-smolvlm` (automatic ~2GB download)
2. No additional configuration needed
3. Use: `--provider huggingface --model HuggingFaceTB/SmolVLM-Instruct` (or no provider flag for default)

**Ollama LLaVA (Local)**
1. Setup: `pixi run setup-ollama` (automatic)
2. Or manual: Install Ollama → `ollama serve` → `ollama pull llava:7b`
3. Use: `--provider ollama --model llava:7b`

**OpenAI GPT-4o (Cloud-based)**
1. Set your OpenAI API key in `.env`:
   ```
   OPENAI_API_KEY=your_key_here
   ```
2. Use: `--provider openai --model gpt-4o`

### Quick Setup
Run the automated setup script:
```bash
./setup.sh
```
This will guide you through setting up all providers.



## Troubleshooting

### Import Errors
Run `pixi run test-imports` to verify all packages are installed correctly.

### Environment Variables
Run `pixi run check-env` to check if required API keys are set.

### Pixi Issues
- Clean and reinstall: `pixi run clean && pixi install`
- Update pixi: Follow instructions at https://pixi.sh/latest/#installation

## Development & Extension

This project is designed to demonstrate how agents can grow in complexity 
by incrementally adding new tools and capabilities.

### Adding New Tools

The project includes additional tools in the `additions/` folder that can 
be integrated to extend functionality:

1. **Image Preprocessing** (`additions_1_opencv.py`)
   - Threshold adjustment, deskewing, noise reduction
2. **Temperature Conversion** (`additions_2_temperature.py`) 
   - Fahrenheit ↔ Celsius conversions
3. **Unit Conversions** (`additions_3_unit_conversions.py`)
   - Cooking measurements, metric/imperial conversions

### Integration Process

To add new capabilities:
1. Review tools in `additions/` folder
2. Copy desired functions to `agent/tools.py`
3. Import and register tools in `main.py`
4. Test with `pixi run test-components`

### System Requirements

- **Python**: 3.10+ (managed by pixi)
- **Memory**: 4GB+ RAM (8GB+ recommended for SmolVLM)
- **Storage**: 3GB+ for all models
- **GPU**: Optional (CUDA-compatible for faster SmolVLM processing)

### Core Dependencies

Automatically managed by pixi:
- **AI/ML**: transformers, torch, accelerate, huggingface-hub
- **LangChain**: langchain-core, langchain-openai, langchain-ollama, langgraph
- **Image Processing**: opencv, pillow, numpy
- **CLI**: typer, python-dotenv