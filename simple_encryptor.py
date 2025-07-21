from cryptography.fernet import Fernet

# STEP 1: Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# STEP 2: Write a message to encrypt
message = "Hello, this is secret!".encode()

# STEP 3: Encrypt the message
encrypted = cipher.encrypt(message)

# STEP 4: Decrypt the message
decrypted = cipher.decrypt(encrypted)

# STEP 5: Print results
print("🔑 Secret Key:", key.decode())
print("📤 Encrypted Message:", encrypted.decode())
print("📥 Decrypted Message:", decrypted.decode())
