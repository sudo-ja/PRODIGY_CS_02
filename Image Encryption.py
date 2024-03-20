import tkinter as tk
from tkinter import filedialog
from PIL import Image

def encrypt_decrypt(image_path):
    key = 255  # Key for bitwise XOR operation
    with Image.open(image_path) as image:
        image = image.convert("RGB")
        width, height = image.size
        for i in range(width):
            for j in range(height):
                r, g, b = image.getpixel((i, j))
                image.putpixel((i, j), (r ^ key, g ^ key, b ^ key))
        return image

def open_image():
    image_path = filedialog.askopenfilename()
    if image_path:
        result_image = encrypt_decrypt(image_path)
        result_image.show()

if __name__ == "__main__":
    root = tk.Tk()
    button = tk.Button(root, text="Open Image", command=open_image)
    button.pack()
    root.mainloop()
