import os

def extract_font_names():
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to find the fonts directory
    font_dir = os.path.join(os.path.dirname(current_dir), 'font')
    output_file = os.path.join(current_dir, 'font_list.txt')
    
    # Create fonts directory if it doesn't exist
    if not os.path.exists(font_dir):
        os.makedirs(font_dir)
        print(f"Created fonts directory at: {font_dir}")
    
    # Get all font files
    font_files = [f for f in os.listdir(font_dir) if f.lower().endswith(('.ttf', '.otf'))]
    
    # Write to font_list.txt
    with open(output_file, 'w') as f:
        for font in sorted(font_files):
            f.write(f'{font}\n')

if __name__ == '__main__':
    extract_font_names()