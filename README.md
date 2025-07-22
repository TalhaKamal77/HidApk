# 🔒 APK Hider in PNG with AES Encryption & Steganography

This Python script demonstrates how to **hide an APK file inside a PNG image** using **AES encryption** and **LSB steganography**. It also supports securely extracting the original APK file from the modified PNG using a password-based key.

> ⚠️ For **educational purposes only**. Do not use for malicious or unauthorized activities.

---

## 📦 Features

- 🔐 **AES-256 encryption** to secure the APK
- 🖼️ **LSB steganography** using the `stegano` library
- 🧠 Simple password-based key derivation (SHA-256)
- 🧪 Includes both **hiding** and **extraction** steps

---

## 📂 How It Works

1. User provides:
   - Path to an APK file
   - A clean PNG image
   - A password
2. Script:
   - Encrypts the APK using AES-256 with a key derived from the password
   - Base64-encodes the encrypted data
   - Hides the base64 string in the PNG using LSB steganography
3. To extract:
   - Script reveals the hidden message from the PNG
   - Decrypts the APK using the same password
   - Writes it back to disk

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/apk-stegano-hider.git
cd apk-stegano-hider
pip install -r requirements.txt
Requirements
Python 3.x

stegano

pycryptodome

You can install manually with:

bash
Copy
Edit
pip install stegano pycryptodome
🛠️ Usage
bash
Copy
Edit
python apk_hider.py
You'll be prompted to enter:

APK file path

PNG image file path (host image)

Output PNG path (to save hidden image)

Output APK path (for recovered APK)

Password (used for AES encryption/decryption)

📌 Example
lua
Copy
Edit
Enter APK file path: myapp.apk
Enter PNG file path: cover.png
Enter output PNG file path: secret_output.png
Enter output APK file path: recovered.apk
Enter password for encryption/decryption: mysecurepassword
⚠️ Disclaimer
This project is intended solely for educational and ethical purposes. Do not use it to distribute or hide malicious content. Misuse may be illegal and unethical. The authors are not responsible for any misuse of this tool.

