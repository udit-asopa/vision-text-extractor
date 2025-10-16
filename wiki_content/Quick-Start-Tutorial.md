# Quick Start Tutorial

Get up and running with Vision Text Extractor in under 5 minutes! This tutorial assumes you've completed the [Installation Guide](Installation-Guide).

## 🎯 **Your First Text Extraction**

### **Step 1: Verify Installation**
```bash
cd vision-text-extractor
pixi run test-setup
```
You should see: `🎉 All dependencies imported successfully!`

### **Step 2: Try the Demo**
```bash
# Use the built-in sample image
pixi run demo-ocr-huggingface
```

**Expected Output:**
```
🔍 Processing image: images/chocolate_cake_recipe.png
💬 Using prompt: Please transcribe the provided image.
🤖 Model provider: huggingface
🧠 Model: HuggingFaceTB/SmolVLM-Instruct
🔄 Loading SmolVLM vision model...

🎉 Text extraction completed!
==================================================
Chocolate Cake Recipe

Ingredients:
- 2 cups all-purpose flour
- 2 cups sugar
- 3/4 cup cocoa powder
...
==================================================
```

🎉 **Congratulations!** You just extracted text from an image using AI!

## 📸 **Try Your Own Images**

### **Local Image Files**
```bash
# Basic extraction
python main.py path/to/your/image.jpg

# With custom prompt
python main.py receipt.jpg --prompt "Extract the total amount and date"

# Different file types
python main.py document.pdf
python main.py screenshot.png
```

### **Online Images (URLs)**
```bash
# Extract from web image
python main.py "https://example.com/menu.jpg"

# With custom prompt
python main.py "https://example.com/receipt.jpg" \
  --prompt "List all items and prices"
```

## 🤖 **Try Different AI Models**

### **Ollama LLaVA (Alternative Local Model)**
```bash
# Setup (one-time)
pixi run setup-ollama

# Use Ollama
python main.py image.jpg --provider ollama --model llava:7b
```

### **OpenAI GPT-4o (Highest Accuracy)**
```bash
# Requires API key in .env file
python main.py image.jpg --provider openai --model gpt-4o
```

## 🎯 **Common Use Cases**

### **📄 Business Documents**
```bash
# Extract contract details
python main.py contract.pdf \
  --prompt "Extract party names, dates, and key terms"

# Process invoice
python main.py invoice.jpg \
  --prompt "Extract invoice number, total amount, and due date"
```

### **🍽️ Food & Recipes**
```bash
# Get recipe ingredients
python main.py recipe-photo.jpg \
  --prompt "List all ingredients with quantities"

# Extract menu prices
python main.py menu.png \
  --prompt "Extract menu items and their prices"
```

### **💰 Financial Documents**
```bash
# Process receipt
python main.py receipt.jpg \
  --prompt "Extract store name, items, prices, and total"

# Bank statement
python main.py statement.pdf \
  --prompt "List all transactions with dates and amounts"
```

## 🚀 **Power User Tips**

### **Pixi Task Shortcuts**
```bash
# Quick demos (no arguments needed)
pixi run demo-ocr-huggingface
pixi run demo-ocr-ollama  
pixi run demo-ocr-openai

# Flexible tasks (your image as argument)
pixi run ocr_llm "my-image.jpg"
pixi run ocr_ollama "my-document.pdf"
```

### **Batch Processing Multiple Images**
```bash
# Process multiple files
for img in *.jpg; do
  python main.py "$img" --prompt "Extract key information"
done
```

### **Save Output to File**
```bash
# Redirect output to file
python main.py document.jpg > extracted_text.txt

# Or use with timestamp
python main.py receipt.jpg > "receipt_$(date +%Y%m%d_%H%M%S).txt"
```

## 🔧 **Customizing Your Prompts**

### **Specific Information Extraction**
```bash
# Extract only phone numbers
python main.py business-card.jpg \
  --prompt "Extract only phone numbers from this business card"

# Get nutritional information
python main.py nutrition-label.jpg \
  --prompt "Extract calories, protein, carbs, and fat content"

# Focus on dates and amounts
python main.py invoice.pdf \
  --prompt "Extract all dates and monetary amounts"
```

### **Structured Output**
```bash
# Request JSON format
python main.py receipt.jpg \
  --prompt "Extract receipt data as JSON with fields: store, date, items, total"

# Table format
python main.py price-list.jpg \
  --prompt "Extract as a table with columns: item, description, price"
```

## ⚡ **Performance Tips**

### **Choose the Right Model**
- **SmolVLM (Hugging Face)**: Best for privacy, decent accuracy
- **LLaVA (Ollama)**: Good alternative, different strengths
- **GPT-4o (OpenAI)**: Highest accuracy, but costs money

### **Optimize for Your Use Case**
```bash
# For handwriting
python main.py handwritten.jpg \
  --prompt "Carefully transcribe this handwritten text"

# For low-quality images
python main.py blurry-scan.jpg \
  --prompt "Extract text even if image quality is poor"

# For multilingual content
python main.py multilingual.jpg \
  --prompt "Extract text and identify the languages used"
```

## 🚨 **Common Issues & Quick Fixes**

### **Model Loading Issues**
```bash
# Re-download SmolVLM if corrupted
rm -rf ~/.cache/huggingface/hub/models--HuggingFaceTB--SmolVLM-Instruct
pixi run setup-smolvlm
```

### **Memory Issues**
```bash
# Use Ollama instead of SmolVLM for lower memory usage
pixi run setup-ollama
python main.py image.jpg --provider ollama
```

### **API Key Issues**
```bash
# Check if OpenAI key is set
pixi run check-env

# Reset environment file
pixi run setup-env
```

## ➡️ **What's Next?**

Now that you're comfortable with the basics:

1. 📖 **Deep Dive**: Read [Basic Usage](Basic-Usage) for more details
2. 🎯 **Specific Tutorials**: Try [Document Processing](Document-Processing-Tutorial)
3. ⚙️ **Advanced Features**: Explore [Advanced Features](Advanced-Features)
4. 🔧 **Configuration**: Learn about [Configuration](Configuration) options

## 🎉 **You're Ready!**

You now know how to:
- ✅ Extract text from any image or document
- ✅ Use different AI providers
- ✅ Customize prompts for specific needs
- ✅ Handle common use cases

Happy text extracting! 🚀

---

*Need help? Check [Troubleshooting](Troubleshooting) or ask in [GitHub Issues](https://github.com/udit-asopa/vision-text-extractor/issues)*
