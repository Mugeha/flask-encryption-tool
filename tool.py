import sys
from cryptography.fernet import Fernet

# Save key to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load key from file
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("🔐 Key not found. Generating a new one...")
        generate_key()
        return load_key()

# Encrypt message
def encrypt_message(message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypt message
def decrypt_message(token):
    key = load_key()
    cipher = Fernet(key)
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
