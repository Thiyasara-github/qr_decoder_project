# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# from qr_decoder import QRCodeDecoder  # Import the decoder class from previous artifact

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/decode-qr', methods=['POST'])
# def decode_qr():
#     """
#     Endpoint to decode QR code from base64 image
#     """
#     try:
#         # Get base64 image from request
#         data = request.get_json()
#         base64_image = data.get('image')
        
#         if not base64_image:
#             return jsonify({"error": "No image provided"}), 400
        
#         # Decode QR code
#         decoder = QRCodeDecoder()
#         result = decoder.decode_qr_code_from_base64(base64_image)
        
#         return jsonify(result)
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from qr_decoder import QRCodeDecoder
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return send_file('Home.html')

@app.route('/decode-qr', methods=['POST'])
def decode_qr():
    try:
        data = request.get_json()
        base64_image = data.get('image')
        
        if not base64_image:
            return jsonify({"error": "No image provided"}), 400
        
        decoder = QRCodeDecoder()
        result = decoder.decode_qr_code_from_base64(base64_image)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)