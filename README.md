Image to Text Converter Web Application:
This is a simple web application that allows users to upload an image and convert it into text using Optical Character Recognition (OCR) technology. The application is built using Python's Flask framework for the back-end and HTML/CSS/JavaScript for the front-end.

Installation:
Clone the repository to your local machine: git clone https://github.com/tejas0709/image-to-text-converter.git

Install the required packages:
pip install -r requirements.txt
This will install Flask, PyTesseract, Pillow, and their dependencies.

Download and install Tesseract OCR from the official website:
    https://github.com/tesseract-ocr/tesseract/releases
    Set the path of the Tesseract executable file in the pytesseract.pytesseract.tesseract_cmd variable in app.py.

Usage:
    Run the Flask application:
    $env:FLASK_APP = "app.py"
    $flask run
    This will start the server and the application will be accessible at http://localhost:5000.
    Upload an image file using the form on the home page.
    Click the "Convert" button to start the conversion process.
    The recognized text will be displayed in a separate section below the form.

Contributing:
Contributions are welcome! If you find a bug or have a suggestion for improvement, please open an issue or create a pull request.
