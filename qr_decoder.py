import os
from pyzbar.pyzbar import decode
from PIL import Image
import base64
import io

class QRCodeDecoder:
    @staticmethod
    def decode_qr_code_from_base64(base64_image):
        """
        Decode QR code from base64 encoded image
        
        Args:
            base64_image (str): Base64 encoded image string
        
        Returns:
            dict: Decoded QR code information or error details
        """
        try:
            # Remove data URI prefix if present
            if base64_image.startswith('data:image'):
                base64_image = base64_image.split(',')[1]
            
            # Decode base64 image
            image_bytes = base64.b64decode(base64_image)
            image = Image.open(io.BytesIO(image_bytes))
            
            # Decode QR codes in the image
            qr_codes = decode(image)
            
            if not qr_codes:
                return {"error": "No QR codes found in the image"}
            
            # Return first QR code's data
            qr_code = qr_codes[0]
            return {
                "data": qr_code.data.decode('utf-8'),
                "type": qr_code.type
            }
        
        except Exception as e:
            return {"error": str(e)}

# This can be used with a web framework like Flask or FastAPI