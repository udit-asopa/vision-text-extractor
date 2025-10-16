# Text Recognition Agent Tutorial
A step-by-step tutorial for building an OCR (Optical Character Recognition) AI agent using LangGraph that can extract and process text from images, with progressively added tools for enhanced functionality.

## Overview
This project demonstrates how to create an AI agent that can:
* Extract text from images using vision-capable language models
* Preprocess images to improve OCR accuracy
* Convert temperatures between Fahrenheit and Celsius
* Convert measurements (length, weight, volume) between different units

The tutorial is designed to show how agents can grow in complexity by incrementally adding new tools and capabilities.

## Project Structure

``` 
text-recognition-agent/
├── agent/
│   └── tools.py              # Tools that the agent can access
├── additions/                # Tools to be added incrementally
│   ├── additions_1_opencv.py    # Image preprocessing tools
│   ├── additions_2_temperature.py  # Temperature conversion
│   └── additions_3_unit_conversions.py  # Unit conversion tools
├── images/
│   └── chocolate_cake_recipe.png  # Sample image for testing
├── main.py                   # Main agent implementation
└── README.md
```

## Project set up

The tutorial starts with the agent having access to one tool, which allows the agent to do OCR text extraction from images using vision-capable LLMs (OpenAI GPT-4o or Ollama Qwen2.5-VL).

Tools can then be copied to `tools.py` and imported to `main.py` to extend the functionality of the agent.

1. Image Preprocessing (`additions_1_opencv.py`)
2. Fahrenheit to Celsius conversion (`additions_2_temperature.py`)
3. Unit Conversions (`additions_3_unit_conversions.py`)

## Requirements
* Python 3.13.5
* Virtual environment with the following packages:
  * `numpy`
  * `opencv-python`
  * `pyyaml`
  * `requests`
  * `langchain-core`
  * `langchain-openai`
  * `langchain-ollama`
  * `langgraph`

## Usage

### Basic OCR
Run the main script to extract text from the sample image.

### Adding New Tools
The tutorial aims to demonstrate how you can add incremental complexity by moving tools from the additions/ folder to agent/tools.py:
* Start with basic OCR - Use only extract_text tool
* Add image preprocessing - Import tools from additions_1_opencv.py
* Add temperature conversion - Import from additions_2_temperature.py
* Add unit conversions - Import from additions_3_unit_conversions.py