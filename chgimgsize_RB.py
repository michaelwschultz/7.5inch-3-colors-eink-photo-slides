#test checking the image size resolution/colors
from PIL import Image
from PIL import *
#import time
import os
import numpy
#define image size
width = 800
height = 480
#define palette array
palettedata = [
        0, 0, 0,
        255, 255, 255,
        255, 0, 0,
    ]
p_img = Image.new('P', (16, 16))
p_img.putpalette(palettedata * 32)
#walk all files under folder
path1 = 'E:/py-script/testpicture/jpg/'
path2 = 'E:/py-script/testpicture/bmp/'
filelist = os.listdir(path1)

for item in filelist:
#    if item.endswith('.jpg'):
    if os.path.isfile(path1+item):
# Image.open() can also open other image types
        img = Image.open(path1+item)
        h, w = img.size
# rotate the vertical image
        if h < w:
            img = img.rotate(270, expand=True)
        else:
            pass
# WIDTH and HEIGHT are integers
        resized_img = img.resize((width, height))
        colored_img = resized_img.quantize(palette=p_img)
#        f, e = os.path.splitext(path2+item)
#        newimage.new('RGB', (width, height), "white")
#        newimgR.save(path2 + item + '-R.bmp')
        colored_img.save(path2 + item + '.bmp')
        img.close()
        resized_img.close()
        colored_img.close()
    else:
        pass