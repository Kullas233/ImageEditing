from PIL import Image
from itertools import product
import os
import numpy as np

WHITE = (255, 255, 255, 255)

change = []
# tile(''''IMG_0186.PNG'''', ''''/Users/dkullas/Documents/Python_Scripts/Game Pics'''', ''''/Users/dkullas/Documents/Python_Scripts/Game Pics/pics'''', 20)

directory = 'pics'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        img = Image.open('my.png')

        tes = img.load()
        for x in range(img.size[0]):  # for every pixel:
            for y in range(img.size[0]):

                if (img.getpixel((x, y)) == WHITE):
                    if (y > 1 and y < 95):
                        # Check Left
                        if (img.getpixel((x, y-1)) == WHITE and img.getpixel((x, y-2)) == WHITE and img.getpixel((x, y+1)) != WHITE):
                            change.append([x, y])

                    if (y < 94 and y > 0):
                        # Check Right
                        if (img.getpixel((x, y+1)) == WHITE and img.getpixel((x, y+2)) == WHITE and img.getpixel((x, y-1)) != WHITE):
                            change.append([x, y])
                    if (x > 1 and x < 95):
                        # Check Up
                        if (img.getpixel((x-1, y)) == WHITE and img.getpixel((x-2, y)) == WHITE and img.getpixel((x+1, y)) != WHITE):
                            change.append([x, y])
                    if (x < 94 and x > 0):
                        # Check Down
                        if (img.getpixel((x+1, y)) == WHITE and img.getpixel((x+2, y)) == WHITE and img.getpixel((x-1, y)) != WHITE):
                            change.append([x, y])

        for block in change:
            tes[block[0], block[1]] = (0, 0, 0, 255)

            img.save("my.png")
