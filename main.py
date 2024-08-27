import pytesseract
from pdf2image import convert_from_path
import os

def pdf_to_text(pdf_path, output_file):
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    # Create a text file to write the extracted text
    with open(output_file, 'w', encoding='utf-8') as f:
        # Process each page
        for i, image in enumerate(images):
            # Extract text from the image using pytesseract
            text = pytesseract.image_to_string(image)
            
            # Write the extracted text to the file
            f.write(f"Page {i+1}:\n{text}\n\n")
    
    print(f"Text extracted and saved to {output_file}")

# Example usage
pdf_path = './666.pdf'
output_file = '666.txt'

pdf_to_text(pdf_path, output_file)