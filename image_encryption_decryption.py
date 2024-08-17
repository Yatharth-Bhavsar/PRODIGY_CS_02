from PIL import Image

KEY = 3  # Fixed encryption and decryption key

def encrypt_image(image_path):
    try:
        img = Image.open(image_path)
        width, height = img.size

        encrypted_img = Image.new('RGB', (width, height))
        pixels_encrypted = []

        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                r = (r + KEY) % 256
                g = (g + KEY) % 256
                b = (b + KEY) % 256
                pixels_encrypted.append((r, g, b))

        encrypted_img.putdata(pixels_encrypted)
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully.")
    except Exception as e:
        print("Error:", e)

def decrypt_image(encrypted_image_path):
    try:
        img = Image.open(encrypted_image_path)
        width, height = img.size

        decrypted_img = Image.new('RGB', (width, height))
        pixels_decrypted = []

        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                r = (r - KEY) % 256
                g = (g - KEY) % 256
                b = (b - KEY) % 256
                pixels_decrypted.append((r, g, b))

        decrypted_img.putdata(pixels_decrypted)
        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully.")
    except Exception as e:
        print("Error:", e)

# Main loop for user interaction
while True:
    print("\nImage Encryption Tool Menu:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        image_path = input("Enter the path of the image to encrypt: ").strip()
        encrypt_image(image_path)
    elif choice == '2':
        encrypted_image_path = input("Enter the path of the encrypted image: ").strip()
        decrypt_image(encrypted_image_path)
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
