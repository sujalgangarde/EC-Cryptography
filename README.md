# EC-Cryptography
 
# Image Cryptography Tool

A Python-based application that encrypts and decrypts image files using **Elliptic Curve Cryptography (ECC)**. This project was developed during the 3rd semester of Computer Engineering to explore the integration of cryptography with image processing and GUI development.

## Features

- **Image Encryption**:
  - Encrypts images using ECC public key.
  - Saves the encrypted image with `_encrypted` appended to the original filename.
  
- **Image Decryption**:
  - Decrypts encrypted images using the ECC private key.
  - Saves the decrypted image with `_decrypted` appended to the filename.

- **Graphical User Interface (GUI)**:
  - A simple and intuitive interface built using `tkinter`.

## How It Works

1. **Encryption**:
   - Generates an ECC key pair (private and public keys).
   - Encrypts the image data using an XOR operation with the ECC public key.
   - Saves the encrypted image.

2. **Decryption**:
   - Uses the ECC private key to decrypt the image data.
   - Restores the original image and saves it.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `tkinter`: For the graphical user interface.
  - `Pillow`: For image handling.
  - `numpy`: For numerical operations on image data.
  - `ecdsa`: For ECC-based cryptographic operations.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You also need the following Python libraries:

```bash
pip install pillow numpy ecdsa
