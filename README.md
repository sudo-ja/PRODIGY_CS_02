# PRODIGY_CS_02

Prodigy Cyber Security Internship - Task 2 - Pixel Manipulation for Image Encryption

Develop a simple image encryption GUI tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

This Python script utilizes Tkinter for the graphical user interface (GUI) and Pillow for image manipulation. Its primary function is to perform a straightforward pixel manipulation process, specifically bitwise XOR with a constant value, for both encryption and decryption purposes. The core functionality lies within the encrypt_decrypt function, which handles the encryption or decryption operation. 

It begins by opening the image, converting it to RGB format, and then applying a bitwise XOR operation to the RGB values of each pixel. The open_image function prompts the user to select an image through a file dialog and subsequently invokes the encrypt_decrypt function with the chosen image. The main segment of the program establishes a basic GUI featuring a button that triggers the open_image function upon being clicked.

To run this program successfully, ensure that you have the Tkinter and Pillow libraries installed within your Python environment. 

You can install them using pip: pip install tkinter pillow
