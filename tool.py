import sys
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get encryption key from environment
key = os.environ.get("ENCRYPTION_KEY")

if not key:
    print("❌ ENCRYPTION_KEY not found in environment variables.")
    sys.exit(1)

# Convert key to bytes if needed
if isinstance(key, str):
    key = key.encode()

cipher = Fernet(key)

# Encrypt message
def encrypt_message(message):
    return cipher.encrypt(message.encode())

# Decrypt message
def decrypt_message(token):
    return cipher.decrypt(token.encode()).decode()

# MAIN PROGRAM
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tool.py encrypt|decrypt <message>")
        sys.exit(1)

    action = sys.argv[1]
    data = sys.argv[2]

    if action == "encrypt":
        encrypted = encrypt_message(data)
        print("📤 Encrypted:", encrypted.decode())
    elif action == "decrypt":
        try:
            decrypted = decrypt_message(data)
            print("📥 Decrypted:", decrypted)
        except Exception as e:
            print("❌ Decryption failed:", str(e))
    else:
        print("❓ Invalid action. Use 'encrypt' or 'decrypt'.")
