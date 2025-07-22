#!/usr/bin/env python3
"""
APK Hiding Demonstration Script with Encryption
"""

from stegano import lsb
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import zipfile
import os
import base64

def simulate_apk_hiding(apk_path, png_path, output_path, key):
    # Read APK file
    with open(apk_path, 'rb') as apk_file:
        apk_data = apk_file.read()
    
    # Read PNG file
    with open(png_path, 'rb') as png_file:
        png_data = png_file.read()
    
    # Encrypt APK data
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(apk_data, AES.block_size))
    
    # Combine IV and encrypted data
    encrypted_apk = iv + encrypted_data
    
    # Simulate hiding APK data in PNG
    secret_png = lsb.hide(png_data, encrypted_apk)
    
    # Save the new PNG file
    with open(output_path, 'wb') as output_file:
        output_file.write(secret_png)
    
    print(f"APK would be hidden in PNG: {output_path}")

def simulate_apk_extraction(png_path, output_apk_path, key):
    # Read PNG file
    with open(png_path, 'rb') as png_file:
        png_data = png_file.read()
    
    # Extract APK data from PNG
    encrypted_apk = lsb.reveal(png_data)
    
    # Decrypt APK data
    iv = encrypted_apk[:AES.block_size]
    encrypted_data = encrypted_apk[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    apk_data = cipher.decrypt(encrypted_data)
    
    # Save the APK file
    with open(output_apk_path, 'wb') as apk_file:
        apk_file.write(apk_data)
    
    print(f"APK would be extracted from PNG: {output_apk_path}")

def main():
    # Get user input
    apk_path = input("Enter APK file path: ")
    png_path = input("Enter PNG file path: ")
    output_png_path = input("Enter output PNG file path: ")
    output_apk_path = input("Enter output APK file path: ")
    
    # Generate encryption key
    key = get_random_bytes(32)  # AES-256 key
    
    # Validate APK file
    if not os.path.exists(apk_path):
        print(f"Error: APK file '{apk_path}' not found.")
        return
    
    # Validate PNG file
    if not os.path.exists(png_path):
        print(f"Error: PNG file '{png_path}' not found.")
        return
    
    # Simulate APK hiding
    simulate_apk_hiding(apk_path, png_path, output_png_path, key)
    
    # Simulate APK extraction
    simulate_apk_extraction(output_png_path, output_apk_path, key)

if __name__ == "__main__":
    main()