from flask import Flask, request, jsonify, send_file
import pytesseract
from PIL import Image
import io
import os

pytesseract.pytesseract.tesseract_cmd = r'D:\project\tesseract\tesseract.exe'

app = Flask(__name__)

@app.route('/')
def home():
    return send_file("index.html")

@app.route('/convert-image-to-text', methods=['POST'])
def convert_image_to_text():
    # Get the uploaded image file
    image_file = request.files['image']
    
    # Read the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # Convert the image to grayscale
    image = image.convert('L')
    
    # Apply OCR using Tesseract
    text = pytesseract.image_to_string(image)
    
    # Return the recognized text as a JSON response
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
