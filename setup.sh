#!/bin/bash
set -e

echo "🚀 OCR LLM Agent - Multi-Provider Setup"
echo "======================================="
echo "Supports: Hugging Face SmolVLM (default) | Ollama LLaVA | OpenAI GPT-4o"
echo

# Check if pixi is installed
if ! command -v pixi &> /dev/null; then
    echo "❌ Pixi is not installed!"
    echo "📦 Install pixi: https://pixi.sh/latest/#installation"
    exit 1
fi

echo "✅ Pixi is installed"

# Install dependencies
echo "📦 Installing dependencies..."
pixi install

# Setup environment file
echo "⚙️  Setting up environment file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file from template"
    echo "💡 Add your OpenAI API key to .env if you want to use OpenAI GPT-4o"
else
    echo "✅ .env file already exists"
fi

# Test basic setup
echo "🔍 Testing basic setup..."
pixi run test-imports

echo
echo "🤖 Setting up AI providers..."
echo

# Setup SmolVLM (default, recommended)
echo "📥 Setting up Hugging Face SmolVLM (default provider)..."
read -p "Download SmolVLM model (~2GB)? (Y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Nn]$ ]]; then
    echo "⏭️  Skipping SmolVLM setup"
else
    pixi run setup-smolvlm
    echo "✅ SmolVLM setup complete (default provider ready!)"
fi

# Setup Ollama (optional)
echo
echo "📥 Setting up Ollama (local LLaVA model)..."
read -p "Install Ollama and LLaVA model? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    pixi run setup-ollama
    echo "✅ Ollama setup complete"
else
    echo "⏭️  Skipping Ollama setup"
fi

echo
echo "🎉 Setup complete!"
echo
echo "🚀 Available commands:"
echo "  # Hugging Face SmolVLM (default, local)"
echo "  pixi run ocr_llm myimage.png"
echo "  pixi run ocr_smolvlm myimage.png"
echo
echo "  # Ollama LLaVA (local, if installed)"  
echo "  pixi run ocr_ollama myimage.png"
echo
echo "  # URL Processing (works with any provider)"
echo "  pixi run ocr_url_example  # Try the tomato soup recipe!"
echo "  python main.py https://example.com/image.jpg"
echo "  python main.py https://example.com/receipt.png --prompt 'Extract prices'"
echo
echo "  # Manual usage with any provider"
echo "  python main.py image.png --provider huggingface"
echo "  python main.py image.png --provider ollama --model llava:7b"
echo "  python main.py image.png --provider openai --model gpt-4o"
echo
echo "📋 Test examples:"
echo "  pixi run ocr_llm images/chocolate_cake_recipe.png  # Local file"
echo "  pixi run ocr_url_example  # Online URL"
echo
echo "🔧 Environment setup:"
echo "  - Edit .env file with your OpenAI API key for GPT-4o"
echo "  - Ollama runs locally (no API key needed)"
echo "  - SmolVLM runs locally (no API key needed)"
