import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np
import os
from ecdsa import SigningKey, VerifyingKey

# Generate ECC key pair
private_key = SigningKey.generate()
public_key = private_key.verifying_key

def encrypt_image(image_path):
    # Load image
    img = Image.open(image_path)
    img_data = np.array(img)

    # Serialize ECC public key
    serialized_public_key = public_key.to_string()
    
    # Resize public key to match image shape
    serialized_public_key_resized = np.resize(serialized_public_key, img_data.shape)

    # Encrypt image data using ECC public key
    # encrypted_data = img_data ^ serialized_public_key_resized  # XOR operation/
    # Resize public key to match image shape
    serialized_public_key_resized = np.resize(serialized_public_key, img_data.shape[:2] + (len(serialized_public_key),))

    encrypted_data = np.array(encrypted_img)
    # Save encrypted image
    encrypted_image_path = os.path.splitext(image_path)[0] + '_encrypted.png'
    encrypted_img = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_img.save(encrypted_image_path)

    return encrypted_image_path

def decrypt_image(encrypted_image_path, output_path):
    # Load encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_data = np.array(encrypted_img)

    # Deserialize ECC private key
    deserialized_private_key = SigningKey.from_string(private_key.to_string())

    # Convert public key to NumPy array
    serialized_public_key = deserialized_private_key.verifying_key.to_string()
    
    # Resize public key to match encrypted image shape
    serialized_public_key_resized = np.resize(serialized_public_key, encrypted_data.shape)

    # Decrypt image data using ECC private key
    decrypted_data = encrypted_data ^ serialized_public_key_resized  # XOR operation

    # Restore decrypted image
    decrypted_img = Image.fromarray(decrypted_data.astype('uint8'))

    # Save decrypted image at the same path as the original image
    decrypted_image_path = os.path.splitext(output_path)[0] + '_decrypted.png'
    decrypted_img.save(decrypted_image_path)

    return decrypted_image_path

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    return filename

def encrypt():
    file_path = browse_file()
    if file_path:
        encrypted_image_path = encrypt_image(file_path)
        print("Image encrypted successfully:", encrypted_image_path)

def decrypt():
    file_path = browse_file()
    if file_path:
        output_path = file_path[:-4]  # Remove extension from original file path
        decrypted_image_path = decrypt_image(file_path, output_path)
        print("Image decrypted and saved successfully:", decrypted_image_path)

# Create GUI
root = tk.Tk()
root.title("Image Cryptography")

# Add buttons
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt)
decrypt_button.pack(pady=10)

root.mainloop()
