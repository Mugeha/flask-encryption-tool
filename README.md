# 🔐 Encryption & Decryption Web App

A simple yet secure web application built using **Flask** and **Fernet encryption** from the `cryptography` library. Users can enter text to encrypt or decrypt messages in a clean and minimal UI. This project is ideal for anyone learning about web security and Python-based cryptography.

---

## 🌐 Live Demo

👉 [Click to Try the App Live](https://flask-encryption-tool-ny2t.onrender.com)

---

## 🎥 Video Walkthrough

📹 [Watch Loom Demo Walkthrough](https://www.loom.com/share/56e036ae61614bb88add64e907579849?sid=565b6d34-04ff-46f2-a6a3-30ae5f9e7617)

---

## 📝 Blog Post

📘 [Read the Build Journey on My Blog](https://mugeha585.hashnode.dev/building-a-simple-web-based-text-encryptor-with-flask-and-fernet)

---

## ⚙️ Tech Stack

- Python 3.x
- Flask
- Cryptography (Fernet)
- python-dotenv
- HTML/CSS (Jinja2)
- Render for deployment

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/encryption-tool.git
cd encryption-tool
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create a .env file in your project root directory with the following content:


```bash
SECRET_KEY=your_fernet_generated_key_here
FLASK_SECRET_KEY=your_flask_secret_key_here
```

To generate keys:

Fernet key:

```bash
from cryptography.fernet import Fernet  
print(Fernet.generate_key().decode())
```

Flask-secret-key

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. How It Works

- Encryption: Enter plain text and click Encrypt.
- The text is encoded and encrypted using Fernet symmetric encryption.
- Decryption: Paste the encrypted text and click Decrypt. If valid, it shows the original message.

### 6. Project Structure

encryption-tool/

│

├── templates/

│   └── index.html

├── .env  

├── .gitignore

├── requirements.txt

├── simple_encryptor.py    # Optional helper module

└── web_app.py             # Main Flask app


### 7. Screenshots

[Guiversion](uploads/guiversion.png)

### 8. Author

Name: Mugeha

LinkedIn:

Email: your.email@example.com

📄 License
This project is licensed under the MIT License.

