from flask import Flask, render_template, request
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Load Flask secret key for session security
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")  # for Flask's internal use

# Load encryption key (used for Fernet)
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

# Safety check
if not ENCRYPTION_KEY:
    raise Exception("ENCRYPTION_KEY not found in environment variables!")

cipher = Fernet(ENCRYPTION_KEY)

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
