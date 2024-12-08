# 📸 QR Code Decoder Web Application

Welcome to the **QR Code Decoder Web Application**! This project allows users to **drag and drop an image** containing a QR code and decode it effortlessly using a combination of **Python, Flask**, and **modern web technologies**. 🚀

---

## 🌟 Features

- 🎯 **Drag & Drop**: Upload images intuitively by dragging them onto the drop zone.  
- 🖼️ **Preview Images**: See the uploaded image before decoding.  
- 🧠 **Smart Decoding**: Decodes QR codes with **Pyzbar** library for accurate results.  
- 🚀 **Responsive Design**: Built with **Tailwind CSS** for an elegant and adaptive UI.  
- 💡 **Error Handling**: Friendly error messages for invalid inputs.  
- 🔄 **Cross-Origin Requests**: Enabled with **CORS** for seamless backend communication.

---

## 🛠️ Tech Stack

- **Frontend**:
  - 🖋️ **HTML5**: Structure of the application.
  - 🎨 **CSS3 (Tailwind CSS)**: Stylish, responsive, and modern user interface.
  - 📜 **JavaScript**: Handles drag-and-drop interactions and image preview.

- **Backend**:
  - 🐍 **Python**: Decoding logic and server-side operations.
  - ⚡ **Flask**: Lightweight web framework for managing routes.
  - 📦 **Pyzbar**: High-precision QR code decoding.
  - 🖼️ **Pillow**: Image processing and decoding.

- **Other**:
  - 🌐 **CORS**: Cross-Origin Resource Sharing for API communication.
  - 🗂️ **Base64**: For handling image data in JSON format.

---

## 🏗️ Setup Guide

### Prerequisites
- **Python 3.8+**
- Package manager **pip**
- Basic knowledge of **command line**

---

### 📥 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/qr-code-decoder-web.git
   cd qr-code-decoder-web
   ```

2. **Install Dependencies**
   ```bash
   pip install flask flask-cors pillow pyzbar
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Web App**
   Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

### 📂 Project Structure

```plaintext
qr-code-decoder-web/
│
├── qr_decoder.py         # QR Code Decoder class
├── app.py                # Flask backend
└── templates/
    └── index.html        # Frontend UI
```
---

## 📸 Preview
Initial Interface
![image](https://github.com/user-attachments/assets/a41f3601-c58b-478a-9788-3f6405a7eb32)
Decoding Result
![image](https://github.com/user-attachments/assets/4ebe2357-9747-4e21-99d8-e6c120255372)

---

## ⚖️ License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it!

---

## 🙌 Acknowledgments

- Icons by [Flaticon](https://www.flaticon.com/).  
- QR decoding powered by the **Pyzbar** library.  
- Tailwind CSS for the modern UI.

---

## 💬 Contact

For any questions or suggestions:  
📧 **vithanagettp@gmail.com**  
🌟 **[GitHub](https://github.com/Thiyasara-github)**  

Let’s build something amazing together! 🚀
