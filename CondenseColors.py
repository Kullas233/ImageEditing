from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy as np
from PIL import Image
from itertools import product
import os


def patch_asscalar(a):
    return a.item()


setattr(np, "asscalar", patch_asscalar)


WHITE = (255, 255, 255, 255)

change = []
# tile(''''IMG_0186.PNG'''', ''''/Users/dkullas/Documents/Python_Scripts/Game Pics'''', ''''/Users/dkullas/Documents/Python_Scripts/Game Pics/pics'''', 20)

directory = 'pics'

# iterate over files in
# that directory
maxm =0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        img = Image.open(f)

        # print(img.getcolors())
        all_colors = []
        for x in range(img.size[0]):  # for every pixel:
            for y in range(img.size[0]):
                pixel = img.getpixel((x,y))
                
                all_colors.append((pixel[0], pixel[1], pixel[2]))

        all_colors = set(all_colors)
        dict_colors = {}

        for color in all_colors:
            color_rgb = sRGBColor(color[0], color[1], color[2])
            white_rgb = sRGBColor(255, 255, 255)

            color_lab = convert_color(color_rgb, LabColor)
            white_lab = convert_color(white_rgb, LabColor)

            delta_e = delta_e_cie2000(color_lab, white_lab)
            dict_colors[(color[0], color[1], color[2])] = delta_e
        dict_colors = dict(sorted(dict_colors.items(), key=lambda item: item[1]))

        dict_keys = list(dict_colors.keys())
        chosen_colors = []
        num_colors = 50

        for x in range(num_colors):
            tmplst = dict_keys[round(len(dict_colors)/num_colors)*x]
            chosen_colors.append(sRGBColor(tmplst[0], tmplst[1], tmplst[2]))
        chosen_colors.append(sRGBColor(0, 0, 0))

        # print(chosen_colors)
        # print(len(chosen_colors))
        # exit()

        tes = img.load()
        for x in range(img.size[0]):  # for every pixel:
            for y in range(img.size[0]):
                pixel = img.getpixel((x,y))
                
                color_rgb = sRGBColor(pixel[0], pixel[1], pixel[2])
                colors_rgb = chosen_colors#[sRGBColor(224, 211, 141), sRGBColor(84, 83, 53), sRGBColor(27, 33, 31), sRGBColor(125, 96, 54), sRGBColor(173, 104, 37), sRGBColor(133, 124, 67),         sRGBColor(255, 255, 255), sRGBColor(0, 0, 0)]
                
                
                # Convert from RGB to Lab Color Space
                color_lab = convert_color(color_rgb, LabColor)
                colors_lab = []
                for c_rgb in colors_rgb: 
                    colors_lab.append(convert_color(c_rgb, LabColor))
                
                # Find the color difference
                sim = 500000
                num = 0
                count = 0
                for c_lab in colors_lab:
                    delta_e = delta_e_cie2000(color_lab, c_lab)
                    # if (delta_e > 40 and delta_e < 45):
                    if(delta_e < sim):
                        sim = delta_e
                        num = count
                    count+=1
                # for block in change:
                # print(colors_rgb[num].rgb_r)
                tes[x, y] = (int(colors_rgb[num].rgb_r), int(colors_rgb[num].rgb_g), int(colors_rgb[num].rgb_b), 255)
                # print("This matches with ", colors_rgb[num])
                # print(pixel)
# print(maxm)

            img.save("my.png")