import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the encryption key from environment
key = os.environ.get("ENCRYPTION_KEY")

if not key:
    raise ValueError("❌ ENCRYPTION_KEY is not set in environment variables")

# Convert to bytes if it's in string format
if isinstance(key, str):
    key = key.encode()

cipher = Fernet(key)

# STEP 1: Write a message to encrypt
message = "Hello, this is secret!".encode()

# STEP 2: Encrypt the message
encrypted = cipher.encrypt(message)

# STEP 3: Decrypt the message
decrypted = cipher.decrypt(encrypted)

# STEP 4: Print results
print("📤 Encrypted Message:", encrypted.decode())
print("📥 Decrypted Message:", decrypted.decode())
