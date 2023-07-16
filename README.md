# AsciiArtGenerator
Converts images into ascii art using python
```diff
                                                                                      ++                  
                                                 .2_                              =3-6W-                  
                                                 .@$+                              7@@3                   
                                                 .W@@3_                            1@@1                   
                                                  0#@@8=                           1@@1                   
                     0.   -0    +.        .1-      =$@@#1        .0               .3@@1  -0     _1_   =:  
                   _4@7  =W@1  0@9_:=  _+3W@#7:1.   -W@@@7=0    +$@2             _W@@@1 +W@0   .8@6  =WW_ 
                   3@@@+=$@@#.0@@@$8.  =86#@@@@6  _19#6@@@@6  -5@@@@1            _18@@10#@@#. -8@@@-:@@@1 
                   .3@@86=8@@75+W@@2    5_.1W@@:  -@@7 :#@@6  3@@3@@@2             2@@$6=9@@: ::5@@776@@8 
                    1@@8. 2@@7_ 4@@:    10  4@@+  -@@7  :@@6  3@@-1@@7_            3@@6_ 2@@0   3@@8._W@#.
                    0@@1  0@@2  3@@:    =8- 4@@=  -@@7  =@@6  3@@- 76_             3@@:  2@@0   3@@1  6@@.
                    :@@1  1@@2  4@@:   _76626@@=  -@@7  =@@6  3@@=33               3@@0  2@@0   3@@1  5@W_
                    :@@1  1@@2  4@@:   4#._1W@@=  -@@7  =@@6  3@@92                3@@0  2@@0   3@@1  7@6 
                    :@@1  1@@2  4@@:  .@9   5@@=  -@@7  =@@6  3@@1                 3@@0  2@@0   3@@1 _W@= 
                    :@@1  1@@2  4@@:  1@9   4@@=  -@@7  =@@6  3@@-                 3@@0  2@@0   3@@1 2@3  
                    :@@1  0@@2  4@@:  6@#.  6@@=  -@@7  =@@6  3@@-                 3@@1  2@@0   3@@1.#5   
                    0@@3  1@@2  3@@1  6@@2 1W@@=  +@@@5==@@6  5@@2_ +0            _9@@@4.2@@1   3@@483    
                   _8@@#-_9@@W- 1@@W3 1@@#403@@80 3@@@@@$@@2 .#@@@$56-            _29@@@W$@$=   3@@$:     
                   _5@@8._6@@7. -@@$= _9@#: +@@9-  -19@@@5-  .17@@@5_                =6@@W1_    9@5.      
                     35_   33    17-   -6+   46_     _28+       081                    15.     28+        
                                                                                              =6_         
                                                                                              3:   _.     
                                                                                              17- _77     
                                                                                               25566=     
                       19-                                                                       __       
                       85                                                                                 
                      _4_                                                                  .              
                      _.                                                                   83             
                      _        .          ..        .        ..    __       __        ._   17             
                     1$+    _.2#92..-    -$W:      0W3_     -9W=  .99-     -98_      :#93-_21             
                   _4@@#+  _68@@@@#9=  _0W@@@5_  =6@@@9:   =$@@#._9@@$.  _2#@@6    _3@@@@@#7_             
                   -08@@W_  4++6#@@7   1@@8@@7  1@@$@@@@9: =7@@8_ 7@@7_  8@WW@@6_  7@W7W@@#-              
                     1@@5   :3  0@@4   2@@++6-  3@@+=7@@@1  0@@1  1@@1   W@8=#@@2  $@7 .-61               
                     7@@-   _6. +@@3   2@@:     2@@+  6@@=  0@@1  1@@1   $@8 =@7.  9@8  +7                
                    _W@8    =$7::@@2   2@@:     2@@+  6@@=  0@@1  1@@1   $@8 23_   9@9__$@4_              
                    -@@4   .W3.48@@2   2@@:     2@@+  6@@=  0@@1  1@@1   $@963     $@@97@@@9.             
                    +@@3   5@-  1@@2   2@@:     2@@+  6@@=  0@@1  1@@1   $@@1      1#@@54@@@-             
                    +@@3  _#@-  +@@2   2@@:     2@@+  6@@=  0@@1  1@@1   $@8        .7$_ 3@@-             
                    -@@3  +@@+  +@@2   2@@+     2@@+  5@@=  0@@1  2@@1   $@8         6+  0@@-             
                    _W@6  1@@5 _6@@2   2@@1  __ 2@@+ _8@@=  0@@1 =$@@1   W@9_  -.   24   0@@-             
                     $@7  +@@#:43@@7+__9@@@6:6= 2@@5.3#@@=  0@@9056@@6+ +@@@$117.  -#$$923@@-             
                     8@7   8@@9-_#@@4__29@@@$+  =#@@8=7@@=  .W@@7_+@@@3 1$@@@@6.  _9@@@@@@8:              
                     7@4   -$7.  5@2    _1W6.    0@8- 8@@=   +W4  _6@2    :W@2    081039#2                
                     $@=    __   _-       .       -_  8@@=    .    _+      _-     _    _.                 
                    =@5                               8@@+                                                
                   .96_                              .#$76                                                
                   :2                                26. 0.                                               
                                                     _
```


## Usage
```bat
C:\Demo>AsciiArtGenerator.py imgs\ferrari.jpg n .5
```
AsciiArtGenerator.py `image_path` `inverse_color` `resize_scale`
 * `image_path`: relative path to source image (ex. "imgs\ferrari.jpg")
 * `inverse_color`: inverse each pixels grayscale ('y' or 'n') default('n')
 * `resize_scale`: decimal value to resize original dimensions for the resulting image (ex. ".5")

   
## Examples
| Input         | Output
| ------------- | ------------- |
| ![husky](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/0ea36cdd-5c19-42b2-b893-4fffbc858b8b)        | ![HuskyAscii](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/3f123f69-35f7-46b3-b5a1-65e6947cb22c)  |
| ![tree](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/d055cb99-6636-4895-a242-9cb6b949bbbb)         | ![TreeAscii](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/831e7b41-6178-45ad-9d3e-b40cb0468591)   |
| ![whiteferrari](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/99224578-31ac-4fa6-98eb-6df20f3de093) | ![FerrariAscii](https://github.com/isaacjacques/AsciiArtGenerator/assets/137218652/89f7a255-0d0c-4bbe-a068-dec6ade53a66)|


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
