# Image Encryption Tool

This Python tool allows you to encrypt and decrypt images using a simple pixel manipulation method. The encryption and decryption operations are based on a fixed key, which is added or subtracted from the pixel values to perform the respective operations.

## 📦 Requirements

- 🐍 Python 3.x
- 📦 Pillow library (PIL fork)

## ▶️ How to Run

1. **📥 Clone this repository**:
    ```bash
    git clone https://github.com/Yatharth-Bhavsar/PRODIGY_CS_02.git
    ```

2. **📂 Navigate to the project directory**:
    ```bash
    cd PRODIGY_CS_02
    ```

3. **📦 Install the required libraries**:
    ```bash
    pip install pillow
    ```

4. **🏃 Run the Python script**:
    ```bash
    python image_encryption_decryption.py
    ```

## 📜 Usage

When you run the script, you will be presented with a menu to choose from:

1. **Encrypt an image**: Enter the path of the image to encrypt. The encrypted image will be saved as `encrypted_image.png`.
2. **Decrypt an image**: Enter the path of the encrypted image to decrypt. The decrypted image will be saved as `decrypted_image.png`.
3. **Exit**: Exit the program.

### Example

Image Encryption Tool Menu:
1. Encrypt an image
2. Decrypt an image
3. Exit
Choose an option (1/2/3): 1
Enter the path of the image to encrypt: path/to/your/image.jpg

##🛠️ Implementation Details
Encryption/Decryption Key: The key used for encryption and decryption is fixed at +3 for encryption and -3 for decryption.
File Names: The encrypted image is saved as encrypted_image.png and the decrypted image is saved as decrypted_image.png.

## 👤 Author

- Yatharth Bhavsar
