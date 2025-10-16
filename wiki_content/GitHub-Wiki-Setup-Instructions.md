# GitHub Wiki Setup Instructions

Follow these steps to create your comprehensive Vision Text Extractor wiki on GitHub.

## 🔧 **Step 1: Enable Wiki on GitHub**

1. Go to your repository: https://github.com/udit-asopa/vision-text-extractor
2. Click on **Settings** tab (must be repository owner/admin)
3. Scroll down to **Features** section
4. Check the box for **Wikis** ✅
5. Click **Save changes**

## 📚 **Step 2: Create Wiki Pages**

After enabling wiki, you'll see a **Wiki** tab next to Code, Issues, etc.

### **Create Each Page**

1. Click **Wiki** tab → **Create the first page**
2. For each page below, click **New Page** and copy the content:

## 📄 **Wiki Pages to Create**

### **Page 1: Home** (Default wiki homepage)
- **Title**: `Home`
- **Content**: Copy from `wiki_content/Home.md`

### **Page 2: Installation Guide**
- **Title**: `Installation Guide`
- **Content**: Copy from `wiki_content/Installation-Guide.md`

### **Page 3: Quick Start Tutorial**
- **Title**: `Quick Start Tutorial`
- **Content**: Copy from `wiki_content/Quick-Start-Tutorial.md`

### **Page 4: Provider Comparison**
- **Title**: `Provider Comparison`
- **Content**: Copy from `wiki_content/Provider-Comparison.md`

### **Page 5: Pixi Tasks Reference**
- **Title**: `Pixi Tasks Reference`
- **Content**: Copy from `wiki_content/Pixi-Tasks-Reference.md`

### **Page 6: Document Processing Tutorial**
- **Title**: `Document Processing Tutorial`
- **Content**: Copy from `wiki_content/Document-Processing-Tutorial.md`

## 📝 **Additional Pages to Create** (Optional)

You can also create these additional pages for a complete wiki:

### **Basic Usage**
```markdown
# Basic Usage

## Command Line Interface

The Vision Text Extractor uses a simple command-line interface built with Typer.

### Basic Syntax
```bash
python main.py [IMAGE_PATH] [OPTIONS]
```

### Examples
```bash
# Basic usage
python main.py image.jpg

# With custom prompt
python main.py document.pdf --prompt "Extract key information"

# Specify provider
python main.py image.png --provider ollama --model llava:7b
```

For more details, see [Quick Start Tutorial](Quick-Start-Tutorial).
```

### **Configuration**
```markdown
# Configuration

## Environment Variables

Create a `.env` file in the project root:

```bash
# OpenAI API Key (optional - only for OpenAI provider)
OPENAI_API_KEY=your_openai_api_key_here

# Hugging Face Token (optional - for private models)
HF_TOKEN=your_hf_token_here

# Custom cache directories (optional)
HF_HOME=/custom/huggingface/cache
OLLAMA_MODELS=/custom/ollama/models
```

## Provider Configuration

### SmolVLM (Hugging Face)
- No configuration required
- Downloads automatically on first use
- Stored in `~/.cache/huggingface/`

### Ollama
- Requires Ollama installation
- Use `pixi run setup-ollama` for automatic setup
- Models stored in `~/.ollama/models/`

### OpenAI
- Requires API key in `.env` file
- Get key from: https://platform.openai.com/api-keys
- Billing must be set up on OpenAI account
```

### **Troubleshooting**
```markdown
# Troubleshooting

## Common Issues

### Installation Problems

**Pixi not found**
```bash
# Add to PATH
export PATH="$HOME/.pixi/bin:$PATH"
```

**Permission denied**
```bash
chmod +x ~/.pixi/bin/pixi
```

### Runtime Issues

**Out of memory with SmolVLM**
- Switch to Ollama: `--provider ollama`
- Close other applications
- Use smaller images

**OpenAI API errors**
- Check API key in `.env`
- Verify billing setup
- Check rate limits

**Ollama connection failed**
- Start Ollama: `ollama serve`
- Check model is installed: `ollama list`

### Getting Help

1. Check this troubleshooting guide
2. Review [GitHub Issues](https://github.com/udit-asopa/vision-text-extractor/issues)
3. Create a new issue with:
   - Operating system
   - Python version
   - Error message
   - Steps to reproduce
```

## 🎯 **Pro Tips**

### **Page Organization**
- Keep page titles consistent with navigation links
- Use clear, descriptive titles
- Organize content with proper headings

### **Cross-Linking**
- Link between related pages using `[Page Title](Page-Title)` format
- Create a logical navigation flow
- Reference the Home page from other pages

### **Content Updates**
- Update wiki pages when you update the code
- Keep examples current with latest features
- Add new use cases and tutorials over time

## ✅ **Final Steps**

After creating all wiki pages:

1. **Test Navigation**: Click through all links to ensure they work
2. **Review Content**: Check for typos and formatting
3. **Update Home Page**: Ensure all pages are linked from Home
4. **Share**: Your wiki is now public and searchable!

## 🌟 **Your Wiki Structure**

When complete, users will have access to:

- **Home**: Overview and navigation
- **Installation Guide**: Complete setup instructions  
- **Quick Start Tutorial**: 5-minute getting started guide
- **Provider Comparison**: Help choosing the right AI model
- **Pixi Tasks Reference**: Complete command reference
- **Document Processing Tutorial**: Real-world usage examples

Your wiki will be accessible at:
**https://github.com/udit-asopa/vision-text-extractor/wiki**

---

*This comprehensive wiki will help users get the most out of your Vision Text Extractor project!* 🚀
