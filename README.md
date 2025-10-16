# Vision Text Extractor

Extract text from images and documents using multiple AI providers. Choose from local models (SmolVLM, LLaVA) or cloud-based (OpenAI GPT-4o) for maximum flexibility.

## ✨ Features

- 🤖 **3 AI Providers**: Local SmolVLM/LLaVA or cloud OpenAI GPT-4o
- 🔒 **Privacy-First**: Local processing keeps your data private
- 🌐 **Flexible Input**: Local files or web URLs
- 💬 **Custom Prompts**: Extract specific information 
- ⚡ **Easy Setup**: One-command installation with Pixi

## 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/udit-asopa/vision-text-extractor.git
cd vision-text-extractor
pixi install

# Quick demo
pixi run demo-ocr-huggingface

# Use with your images  
python main.py path/to/your/image.jpg
python main.py "https://example.com/image.png"
```

## 📖 Documentation

For detailed guides and tutorials, visit our **[Wiki](https://github.com/udit-asopa/vision-text-extractor/wiki)**:

- 📋 [**Installation Guide**](https://github.com/udit-asopa/vision-text-extractor/wiki/Installation-Guide) - Complete setup for all providers
- 🚀 [**Quick Start Tutorial**](https://github.com/udit-asopa/vision-text-extractor/wiki/Quick-Start-Tutorial) - Get started in 5 minutes  
- 📊 [**Provider Comparison**](https://github.com/udit-asopa/vision-text-extractor/wiki/Provider-Comparison) - Choose the right AI model
- 📄 [**Document Processing**](https://github.com/udit-asopa/vision-text-extractor/wiki/Document-Processing-Tutorial) - Real-world examples
- ⚙️ [**Pixi Tasks Reference**](https://github.com/udit-asopa/vision-text-extractor/wiki/Pixi-Tasks-Reference) - All available commands

## 🛠️ Installation

### Prerequisites
- [Pixi](https://pixi.sh) package manager
- Python 3.10+ (managed by Pixi)

### Setup
```bash
git clone https://github.com/udit-asopa/vision-text-extractor.git
cd vision-text-extractor
pixi install
pixi run setup
```

### Choose Your AI Provider

**🟢 Local & Free (Recommended)**
```bash
pixi run setup-smolvlm    # Hugging Face SmolVLM (~2GB)
pixi run setup-ollama     # Ollama LLaVA (~4GB)  
```

**🟡 Cloud & Paid (Highest Accuracy)**
```bash
# Add your OpenAI key to .env file
echo "OPENAI_API_KEY=your_key_here" >> .env
```

## 💡 Basic Usage

```bash
# Extract text from any image
python main.py path/to/your/image.jpg

# Process web images
python main.py "https://example.com/document.png"

# Custom extraction prompt
python main.py receipt.jpg --prompt "Extract total amount and date"

# Try different providers
python main.py image.png --provider ollama --model llava:7b
python main.py image.png --provider openai --model gpt-4o
```

## 🎯 Common Use Cases

- 📄 **Business Documents**: Invoices, contracts, forms, receipts
- 🍽️ **Food & Restaurants**: Recipes, menus, nutrition labels  
- 💰 **Finance**: Bank statements, tax documents, expense reports
- 📚 **Education**: Homework, research papers, lecture notes
- 🏥 **Healthcare**: Prescriptions, lab results, medical forms

*See our [Document Processing Tutorial](https://github.com/udit-asopa/vision-text-extractor/wiki/Document-Processing-Tutorial) for detailed examples.*

## 🔧 Quick Commands

```bash
# Demo with sample images
pixi run demo-ocr-huggingface  # SmolVLM demo
pixi run demo-ocr-ollama       # LLaVA demo  
pixi run demo-ocr-openai       # OpenAI demo

# Test your setup
pixi run test-setup            # Validate installation
pixi run check-env             # Check API keys

# Process your files
pixi run ocr_llm "my-image.jpg"
pixi run ocr_ollama "document.pdf"
```

## 📂 Project Structure

```
vision-text-extractor/
├── main.py              # Main CLI application
├── agent/tools.py       # OCR extraction tools
├── tests/              # Test scripts
├── images/             # Sample images
├── wiki_content/       # Documentation source
├── LICENSE             # MIT License
└── pixi.toml          # Dependencies & tasks
```

## 🤝 Contributing

We welcome contributions! Please see our [Wiki](https://github.com/udit-asopa/vision-text-extractor/wiki) for development guides and check out existing [Issues](https://github.com/udit-asopa/vision-text-extractor/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**MIT License Summary:**
- ✅ **Commercial use** - Use in commercial projects
- ✅ **Modification** - Change and adapt the code  
- ✅ **Distribution** - Share with others
- ✅ **Private use** - Use for personal projects
- ❓ **Warranty** - No warranty provided

## ⚠️ Privacy Notice

- **Local providers** (SmolVLM, LLaVA): Your data never leaves your machine
- **OpenAI provider**: Data is sent to OpenAI's servers
- **API keys**: Never commit `.env` files to version control

---

**Need help?** Check our [Wiki](https://github.com/udit-asopa/vision-text-extractor/wiki) or create an [Issue](https://github.com/udit-asopa/vision-text-extractor/issues) 🚀
