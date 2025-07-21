import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables from .env (useful in local dev)
load_dotenv()

# Get key from environment
key = os.environ.get("ENCRYPTION_KEY")

if not key:
    raise ValueError("❌ ENCRYPTION_KEY is not set in environment variables")

# Convert to bytes if it's in string format
if isinstance(key, str):
    key = key.encode()

cipher = Fernet(key)

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
