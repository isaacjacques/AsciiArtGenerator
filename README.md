# AsciiArtGenerator
Converts images into ascii art using python

| Input         | Output
| ------------- | ------------- |
| ![husky](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/0ea36cdd-5c19-42b2-b893-4fffbc858b8b)        | ![HuskyAscii](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/3f123f69-35f7-46b3-b5a1-65e6947cb22c)  |
| ![tree](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/d055cb99-6636-4895-a242-9cb6b949bbbb)         | ![TreeAscii](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/831e7b41-6178-45ad-9d3e-b40cb0468591)   |
| ![whiteferrari](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/99224578-31ac-4fa6-98eb-6df20f3de093) | ![FerrariAscii](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/89f7a255-0d0c-4bbe-a068-dec6ade53a66)|


## Usage
```bat
C:\Demo>AsciiArtGenerator.py imgs\ferrari.jpg n .5
```
AsciiArtGenerator.py `image_path` `inverse_color` `resize_scale`
 * `image_path`: relative path to source image (ex. "imgs\ferrari.jpg")
 * `inverse_color`: inverse each pixels grayscale ('y' or 'n') default('n')
 * `resize_scale`: decimal value to resize original dimensions for the resulting image (ex. ".5")


## How It Work
### Imports
```python
from PIL import Image   #support for opening, manipulating, and saving many different image file formats
import numpy as np      #used to convert image into an array
import os               #used to get working directory and concat the output filename/path
import sys              #support for arguments passed in from cli 
```

### AsciiArtGenerator
```python
    #First the image is opened, resized and converted to an array
    image = Image.open(image_path)
    image_resized = image.resize((round(image.size[0]*resize_scale), round(image.size[1]*resize_scale)))
    image_array = np.asarray(image_resized)
    rows = image_array.shape[0]
    columns = image_array.shape[1]

    #Then iterate over each pixel by row/col: O(n²)
      #Convert rgb into greyscale (average brightness) 
      #Scale the greyscale value (0 - 255) into an index representing a character in ASCII_CHARS['@#W$9876543210:+=-._ '] (0 - len(ASCII_CHARS))
      #If inversing the scale, get the corresponding character from the opposite end of the array/character spectrum
      #Append the ascii character, returning to the next line at the end of the current row
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

    #Write the ascii string to a file
    with open(output_path, 'w') as file:
        file.write(ascii_string)
    print(f"Generated ascii art written to {output_path}")
```


## Technologies Used
* VS Code
* Python 3
 * numpy
 * pillow


## Authors
* **Isaac Jacques** - *Initial work* - [isaacjacques](https://isaacjacques.com)
  
![MadeBy](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/9ba9fd49-0e05-41be-9310-df7d993fad3f)

