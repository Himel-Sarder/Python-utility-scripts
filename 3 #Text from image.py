import pytesseract
from PIL import Image

# Open the image file
image = Image.open('test.png')

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
