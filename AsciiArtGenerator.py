from PIL import Image
import numpy as np
import os

ASCII_CHARS = '@#W$9876543210:+=-._ '
ASCII_CHARS_LEN = len(ASCII_CHARS)

def AsciiArtGenerator(image_path, output_path, inverse_color, resize_scale):
    image = Image.open(image_path)
    image_resized = image.resize((round(image.size[0]*resize_scale), round(image.size[1]*resize_scale)))

    image_array = np.asarray(image_resized)
    rows = image_array.shape[0]
    columns = image_array.shape[1]

    ascii_string = ""
    for row in range(rows):
        for col in range(columns):
            pixel_value = image_array[row, col]
            r = int(pixel_value[0])
            g = int(pixel_value[1])
            b = int(pixel_value[2])
            brightness = (r+g+b) / 3
            brightness_scale = brightness/255
            ascii_index = int(round(brightness_scale * (ASCII_CHARS_LEN - 1)))
            ascii_index = max(0,ascii_index)
            ascii_index = min(ascii_index, ASCII_CHARS_LEN-1)

            if(inverse_color):
                ascii_index = (ASCII_CHARS_LEN-1) - ascii_index 

            ascii_char = ASCII_CHARS[ascii_index]
            ascii_string += ascii_char
        ascii_string += "\n"
    
    with open(output_path, 'w') as file:
        file.write(ascii_string)
    print(f"Generated ascii art written to {output_path}")


try:
    image_path = input("Input the source image path: ")
    app_path = os.path.dirname(os.path.abspath(__file__))
    output_path, ext = os.path.splitext(image_path)
    output_path += ".txt"
    inverse_color = (input("Inverse image colors? (y/n): ") == "y")
    resize_scale = round(float(input("As a decimal, provide the amount to scale the image by (default 1):")),2)
    if(not resize_scale):
        resize_scale = 1

    AsciiArtGenerator(image_path, output_path, inverse_color, resize_scale)
except Exception as e:
    print(f"exception caught: {e}")

