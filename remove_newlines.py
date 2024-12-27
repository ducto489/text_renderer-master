
def remove_newlines(input_file, output_file):
    try:
        # Read the content of the file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove all newlines
        content_without_newlines = content.replace('\n', ' ')
        
        # Write the modified content back to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content_without_newlines)
            
        print(f"Successfully removed all newlines. Result saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Could not find file {input_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "example_data/text/vie_text.txt"
    output_file = "example_data/text/vie_text_no_newlines.txt"
    remove_newlines(input_file, output_file)