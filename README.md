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
