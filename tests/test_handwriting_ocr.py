#!/usr/bin/env python3
"""
Test script to verify OCR output for handwriting_sample.webp image.
Tests that the extracted text matches the expected handwriting content using SmolVLM.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def extract_text_with_smolvlm(image_path: str, prompt: str = "Please transcribe the provided image.") -> str:
    """
    Extract text from image using Hugging Face SmolVLM model.
    
    Args:
        image_path: Path to image file
        prompt: Prompt to send to the model
        
    Returns:
        Extracted text from the image
    """
    try:
        from PIL import Image
        from transformers import AutoProcessor, Idefics3ForConditionalGeneration
        import torch
        
        model_name = "HuggingFaceTB/SmolVLM-Instruct"
        
        print(f"   🔄 Loading SmolVLM vision model...")
        
        # Load model and processor
        processor = AutoProcessor.from_pretrained(model_name)
        vision_model = Idefics3ForConditionalGeneration.from_pretrained(
            model_name,
            dtype=(torch.float16 if torch.cuda.is_available() 
                   else torch.float32),
            device_map="auto" if torch.cuda.is_available() else "cpu",
            trust_remote_code=True
        )
        
        # Load and process image
        image = Image.open(image_path)
        
        # Create prompt for vision model
        messages = [{
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", 
                 "text": f"{prompt}\n\nPlease extract and transcribe "
                        "all text visible in this image."}
            ]
        }]
        
        # Process inputs
        text_input = processor.apply_chat_template(
            messages, 
            add_generation_prompt=True
        )
        inputs = processor(
            text=text_input,
            images=[image],
            return_tensors="pt",
            padding=True
        )
        
        # Move to device if GPU available
        if torch.cuda.is_available():
            inputs = {k: v.to(vision_model.device) for k, v in inputs.items()}
        
        # Generate response
        with torch.no_grad():
            generated_ids = vision_model.generate(
                **inputs,
                max_new_tokens=1000,
                do_sample=False
            )
        
        # Decode response
        generated_text = processor.batch_decode(
            generated_ids[:, inputs["input_ids"].shape[1]:],
            skip_special_tokens=True
        )[0]
        
        return generated_text.strip()
        
    except Exception as e:
        print(f"❌ Error during SmolVLM extraction: {e}")
        raise


def test_handwriting_sample_extraction():
    """
    Test that handwriting_sample.webp is correctly extracted using SmolVLM.
    
    Expected output:
    "My name is Erin Fish. I am taking this course to improve my handwriting 
    so I can enjoy writing in my journals again. As it stands now I find my 
    handwriting to be ununiformed and unattractive. I would like my freehand 
    to flow much more smoothly and as effortlessly as possible."
    """
    
    expected_text = (
        "My name is Erin Fish. I am taking this course to improve my handwriting "
        "so I can enjoy writing in my journals again. As it stands now I find my "
        "handwriting to be ununiformed and unattractive. I would like my freehand "
        "to flow much more smoothly and as effortlessly as possible."
    )
    
    image_path = "images/handwriting_sample.webp"
    
    # Check if image exists
    if not os.path.exists(image_path):
        print(f"❌ Test image not found: {image_path}")
        return False
    
    print(f"🔍 Testing handwriting sample extraction with SmolVLM...")
    print(f"   📄 Image: {image_path}")
    
    try:
        # Extract text using SmolVLM
        extracted = extract_text_with_smolvlm(image_path)
        
        if not extracted:
            print(f"❌ No text extracted from image")
            return False
        
        print(f"\n📝 Extracted text:")
        print(f"   {extracted}")
        
        # Normalize both strings for comparison (remove extra whitespace)
        extracted_normalized = " ".join(extracted.split())
        expected_normalized = " ".join(expected_text.split())
        
        # Check if extracted text matches expected
        if extracted_normalized == expected_normalized:
            print(f"\n✅ Perfect match! Extracted text matches expected output exactly.")
            return True
        else:
            # Check for similarity even if not exact (allows for minor variations)
            # Calculate similarity by checking if all key phrases are present
            key_phrases = [
                "My name is Erin Fish",
                "taking this course",
                "improve my handwriting",
                "journals again",
                "ununiformed and unattractive",
                "freehand to flow",
                "smoothly and as effortlessly"
            ]
            
            all_phrases_found = all(phrase in extracted for phrase in key_phrases)
            
            if all_phrases_found:
                print(f"\n⚠️  Extracted text contains all key phrases but has minor differences:")
                print(f"\n   Expected:")
                print(f"   {expected_text}")
                print(f"\n   Got:")
                print(f"   {extracted}")
                return True
            else:
                print(f"\n❌ Extracted text does not match expected output")
                print(f"\n   Expected:")
                print(f"   {expected_text}")
                print(f"\n   Got:")
                print(f"   {extracted}")
                
                # Show which phrases are missing
                missing = [p for p in key_phrases if p not in extracted]
                if missing:
                    print(f"\n   Missing phrases:")
                    for phrase in missing:
                        print(f"   - {phrase}")
                
                return False
        
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run the handwriting OCR test."""
    print("🧪 Handwriting Sample OCR Test")
    print("=" * 50)
    
    try:
        result = test_handwriting_sample_extraction()
        
        print("\n" + "=" * 50)
        if result:
            print("✅ Test PASSED: Handwriting extraction works correctly")
            return 0
        else:
            print("❌ Test FAILED: Handwriting extraction needs improvement")
            return 1
            
    except Exception as e:
        print(f"\n❌ Test error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
