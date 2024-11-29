import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Constants
FONT_DIR = Path("example_data/font")
TEST_TEXT = "Xin chào Việt Nam ĂÂĐÊÔƠƯàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹ"
IMAGE_SIZE = (800, 100)
FONT_SIZE = 32
OUTPUT_DIR = Path("font_test_results")

def test_font(font_path, output_dir):
    try:
        # Create image
        image = Image.new('RGB', IMAGE_SIZE, color='white')
        draw = ImageDraw.Draw(image)
        
        # Load and test font
        font = ImageFont.truetype(str(font_path), FONT_SIZE)
        draw.text((10, 10), TEST_TEXT, font=font, fill='black')
        
        # Save result
        font_name = font_path.stem
        output_path = output_dir / f"{font_name}_test.png"
        image.save(output_path)
        
        return True, None
        
    except Exception as e:
        return False, str(e)

def main():
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Get all font files with more detailed logging
    font_files = []
    print(f"Searching for fonts in: {FONT_DIR.absolute()}")
    
    if not FONT_DIR.exists():
        print(f"Error: Font directory does not exist: {FONT_DIR}")
        return
        
    for ext in ['*.ttf', '*.TTF', '*.otf', '*.OTF']:
        found = list(FONT_DIR.glob(ext))
        print(f"Found {len(found)} files with extension {ext}")
        font_files.extend(found)
    
    if not font_files:
        print("No font files found! Please check the font directory.")
        return
        
    print(f"\nFound font files:")
    for font in font_files:
        print(f"- {font.name}")
    
    print(f"\nTesting {len(font_files)} fonts...")
    
    results = []
    for font_path in font_files:
        print(f"\nTesting {font_path.name}...")
        success, error = test_font(font_path, OUTPUT_DIR)
        
        if success:
            print("✓ Success")
            results.append((font_path.name, True, None))
        else:
            print(f"✗ Failed: {error}")
            results.append((font_path.name, False, error))
    
    # Print summary
    print("\n=== Summary ===")
    print(f"Total fonts tested: {len(font_files)}")
    print(f"Successful: {sum(1 for r in results if r[1])}")
    print(f"Failed: {sum(1 for r in results if not r[1])}")
    
    print("\nFailed fonts:")
    for name, success, error in results:
        if not success:
            print(f"- {name}: {error}")
            
    print(f"\nResults saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()