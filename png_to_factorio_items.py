from PIL import Image
import time
from functools import partial

IN_FILE = 'dickbutt.png'
OUT_FILE = "dickbutt.txt"

def color_distance(rgb1, rgb2):
    from colormath.color_objects import sRGBColor, LabColor
    from colormath.color_conversions import convert_color
    from colormath.color_diff import delta_e_cie2000

    # Red Color
    color1_rgb = sRGBColor(rgb1[0]/255.0, rgb1[1]/255.0, rgb1[2]/255.0);

    # Blue Color
    color2_rgb = sRGBColor(rgb2[0]/255.0, rgb2[1]/255.0, rgb2[2]/255.0);

    # Convert from RGB to Lab Color Space
    color1_lab = convert_color(color1_rgb, LabColor);

    # Convert from RGB to Lab Color Space
    color2_lab = convert_color(color2_rgb, LabColor);

    # Find the color difference
    delta_e = delta_e_cie2000(color1_lab, color2_lab);

    return delta_e

"""
               (210,176,161):(159,0),
               (162,83,38):(159,1),
               (155,92,113):(159,2),
               (116,112,143):(159,3),
               (192,140,37):(159,4),
               (107,123,56):(159,5),
               (169,82,83):(159,6),
               (58,43,37):(159,7),
               (140,111,101):(159,8),
               (89,94,94):(159,9),
               (123,73,91):(159,10),
               (76,62,94):(159,11),
               (80,53,37):(159,12),
               (78,87,45):(159,13),
               (150,64,49):(159,14),
               (39,23,15):(159,15),
"""

block_colors = {(255,255,255):"plastic-bar",
               (221,137,0):"productivity-module-3",
               (166,64,0):"explosives",
               (96,133,209):"science-pack-3",
               (225,210,42):"sulfur",
               (54,154,5):"electronic-circuit",
               (65,65,65):"solid-fuel",
               (180,186,186):"iron-plate",
               (27,114,164):"blueprint",
               (142,60,211):"filter-inserter",
               (41,54,167):"speed-module",
               (93,55,29):"wooden-chest",
               (60,84,26):"pumpjack",
               (172,46,41):"deconstruction-planner",
               (0,0,0):"coal",
               }
               

start_time =  time.time()
im = Image.open(IN_FILE)

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
f = open(OUT_FILE, 'w')
i = 0
converted_str = "{"
for row in pixels:
    converted_str = "%s{" % converted_str
    for column in row:
        result = min(block_colors.keys(), key=partial(color_distance, column))
        converted_str = "%s'%s'," % (converted_str, block_colors[result])
    converted_str = "%s},\n" % converted_str[:-1]
    print i
    i += 1

converted_str = "%s}" % converted_str[:-2]
f.write(converted_str)
f.close()

end_time = time.time()
print ("%ssec" % (end_time - start_time))

#print pixels
