from flask import Flask, render_template, request
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Get secret key securely from environment
SECRET_KEY = os.getenv("SECRET_KEY")

# Safety check
if not SECRET_KEY:
    raise Exception("SECRET_KEY not found in environment variables!")

cipher = Fernet(SECRET_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form['text']
    encrypted = cipher.encrypt(text.encode()).decode()
    return render_template('index.html', original=text, result=encrypted, mode='Encryption')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_text = request.form['text']
    try:
        decrypted = cipher.decrypt(encrypted_text.encode()).decode()
        return render_template('index.html', original=encrypted_text, result=decrypted, mode='Decryption')
    except Exception:
        return render_template('index.html', original=encrypted_text, result="Invalid key or corrupted data", mode='Decryption')

if __name__ == '__main__':
    app.run(debug=True)
