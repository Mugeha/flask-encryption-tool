import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

# Load or generate key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

cipher = Fernet(load_key())

# Encrypt file
def encrypt_file(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        encrypted = cipher.encrypt(data)

        encrypted_file_path = file_path + ".encrypted"
        with open(encrypted_file_path, "wb") as f:
            f.write(encrypted)

        print(f"✅ File encrypted: {encrypted_file_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Decrypt file
def decrypt_file(file_path):
    try:
        if not file_path.endswith(".encrypted"):
            print("❌ Only .encrypted files can be decrypted.")
            return

        with open(file_path, "rb") as f:
            data = f.read()

        decrypted = cipher.decrypt(data)

        original_path = file_path.replace(".encrypted", ".decrypted")
        with open(original_path, "wb") as f:
            f.write(decrypted)

        print(f"✅ File decrypted: {original_path}")
    except Exception as e:
        print(f"❌ Decryption failed: {e}")

# === Run from terminal ===
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage:\n  python file_encryptor.py encrypt <file_path>\n  python file_encryptor.py decrypt <file_path>")
        exit()

    action = sys.argv[1]
    file_path = sys.argv[2]

    if action == "encrypt":
        encrypt_file(file_path)
    elif action == "decrypt":
        decrypt_file(file_path)
    else:
        print("❓ Use 'encrypt' or 'decrypt'")
