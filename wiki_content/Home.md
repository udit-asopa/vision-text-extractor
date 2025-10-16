# Vision Text Extractor Wiki

Welcome to the **Vision Text Extractor** wiki! This comprehensive guide will help you get the most out of this multi-provider OCR tool.

## 🚀 Quick Navigation

### **Getting Started**
- [Installation Guide](Installation-Guide) - Complete setup instructions
- [Quick Start Tutorial](Quick-Start-Tutorial) - Get running in 5 minutes
- [Configuration](Configuration) - Environment setup and API keys

### **Usage Guides**
- [Basic Usage](Basic-Usage) - Command-line interface basics
- [Advanced Features](Advanced-Features) - Custom prompts, batch processing
- [Provider Comparison](Provider-Comparison) - Choosing the right AI model

### **Tutorials**
- [Document Processing](Document-Processing-Tutorial) - Business documents, forms, receipts
- [Recipe Extraction](Recipe-Extraction-Tutorial) - Cooking and food industry use cases
- [Academic Research](Academic-Research-Tutorial) - Educational and research applications

### **Technical Reference**
- [API Reference](API-Reference) - Function documentation
- [Pixi Tasks](Pixi-Tasks-Reference) - Complete task reference
- [Troubleshooting](Troubleshooting) - Common issues and solutions

### **Development**
- [Contributing](Contributing) - How to contribute to the project
- [Architecture](Architecture) - Technical architecture overview
- [Adding New Providers](Adding-New-Providers) - Extend with more AI models

## 🌟 **What is Vision Text Extractor?**

Vision Text Extractor is a powerful, multi-provider OCR (Optical Character Recognition) tool that uses state-of-the-art vision-language models to extract text from images and documents. 

### **Key Features**
- **3 AI Providers**: Choose from Hugging Face SmolVLM (local), Ollama LLaVA (local), or OpenAI GPT-4o (cloud)
- **Flexible Input**: Support for local files and web URLs
- **Custom Prompts**: Extract specific information with targeted prompts
- **Professional CLI**: Built with Typer for excellent user experience
- **Easy Setup**: Managed dependencies with Pixi

### **Use Cases**
- 📄 **Business Documents**: Contracts, invoices, forms
- 🍽️ **Food Industry**: Recipes, menus, nutrition labels
- 💰 **Finance**: Receipts, bank statements, tax documents
- 📚 **Education**: Homework, research papers, lecture notes
- 🏥 **Healthcare**: Prescriptions, lab results, medical forms
- 🏠 **Real Estate**: Property listings, lease agreements

## 🎯 **Quick Example**

```bash
# Install and setup
git clone https://github.com/udit-asopa/vision-text-extractor.git
cd vision-text-extractor
pixi install
pixi run setup

# Extract text from an image
pixi run demo-ocr-huggingface
python main.py path/to/your/image.jpg

# Custom extraction
python main.py receipt.jpg --prompt "Extract total amount and date"
```

## 📚 **Learning Path**

**New Users**: Start with [Installation Guide](Installation-Guide) → [Quick Start Tutorial](Quick-Start-Tutorial)

**Power Users**: Jump to [Advanced Features](Advanced-Features) → [API Reference](API-Reference)

**Developers**: Check out [Architecture](Architecture) → [Contributing](Contributing)

---

*Last updated: October 2025*
