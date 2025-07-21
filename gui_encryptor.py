import tkinter as tk
from tkinter import messagebox, scrolledtext
from cryptography.fernet import Fernet
import os

# === KEY MANAGEMENT ===
from dotenv import load_dotenv
load_dotenv()

import base64

key = os.getenv("ENCRYPTION_KEY")

if not key:
    raise Exception("ENCRYPTION_KEY is not set in .env")

cipher = Fernet(key.encode())


# === GUI LOGIC ===
def encrypt_text():
    text = input_area.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to encrypt.")
        return
    encrypted = cipher.encrypt(text.encode()).decode()
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, encrypted)

def decrypt_text():
    text = input_area.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to decrypt.")
        return
    try:
        decrypted = cipher.decrypt(text.encode()).decode()
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, decrypted)
    except:
        messagebox.showerror("Error", "Decryption failed. Invalid key or text.")

def clear_fields():
    input_area.delete("1.0", tk.END)
    output_area.delete("1.0", tk.END)

def copy_output():
    result = output_area.get("1.0", tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Result copied to clipboard!")

# === GUI DESIGN ===
root = tk.Tk()
root.title("🔐 Encryption/Decryption Tool - GUI Edition")
root.geometry("700x500")
root.configure(bg="#1e1e2f")

# Header
title = tk.Label(root, text="🔒 Secure Message Tool", font=("Arial", 20, "bold"), fg="white", bg="#1e1e2f")
title.pack(pady=10)

# Input Label
tk.Label(root, text="Input (Text to Encrypt/Decrypt):", font=("Arial", 12), fg="white", bg="#1e1e2f").pack()

# Input Text Area
input_area = scrolledtext.ScrolledText(root, height=6, width=80, font=("Courier", 12))
input_area.pack(pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(btn_frame, text="🔐 Encrypt", command=encrypt_text, width=15, bg="#28a745", fg="white", font=("Arial", 11, "bold"))
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(btn_frame, text="🔓 Decrypt", command=decrypt_text, width=15, bg="#007bff", fg="white", font=("Arial", 11, "bold"))
decrypt_btn.grid(row=0, column=1, padx=5)

copy_btn = tk.Button(btn_frame, text="📋 Copy Output", command=copy_output, width=15, bg="#17a2b8", fg="white", font=("Arial", 11, "bold"))
copy_btn.grid(row=0, column=2, padx=5)

clear_btn = tk.Button(btn_frame, text="🧹 Clear", command=clear_fields, width=15, bg="#dc3545", fg="white", font=("Arial", 11, "bold"))
clear_btn.grid(row=0, column=3, padx=5)

# Output Label
tk.Label(root, text="Output (Encrypted/Decrypted Text):", font=("Arial", 12), fg="white", bg="#1e1e2f").pack()

# Output Text Area
output_area = scrolledtext.ScrolledText(root, height=6, width=80, font=("Courier", 12), bg="#f0f0f0")
output_area.pack(pady=5)

# Footer
footer = tk.Label(root, text="Created by Mugeha • Beginner Cybersecurity Project", fg="#888", bg="#1e1e2f", font=("Arial", 10))
footer.pack(pady=10)

# Start the GUI
root.mainloop()
