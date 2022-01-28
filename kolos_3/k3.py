import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageColor
import numpy as np
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from PIL import ImageEnhance
from PIL import ImageShow
from PIL import ImageStat as stat

path = "kolos_3/"
path2 = "kolos_3/obrazy/"

#Zadanie z okregami
# img = Image.open(path2+"img2.jpeg")
# height = img.size[1]
# bbox = [(0, 0), (height, height)]
# bbox2 = [(height/2, 0), (height*1.5, height)]
# dctx = ImageDraw.Draw(img)
# dctx.ellipse(bbox, outline="greenyellow", width=15)
# dctx.ellipse(bbox2, outline=(82, 0, 208), width=15)
# img.show()
# img.save(path+"okregi.png")


# def hex_to_rgb(value):
#     if("#" in value):
#         value = value.lstrip('#')
#     lv = len(value)
#     return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


#print("greenyellow:", hex_to_rgb(ImageColor.colormap['greenyellow']))

# greenyellow: (173, 255, 47) #adff2f
# negatyw: (82, 0, 208)

## Zadanie z wycinaniem i wklejaniem
# obraz2 = Image.open(path2+'obraz1.jpg')
# obraz2.show()
# w_o = obraz2.size[0]
# h_o = obraz2.size[1]
# w = obraz2.size[0]/5
# h = obraz2.size[1]/5
# obraz_crop = obraz2.crop((w_o - w, h_o - h, w_o, h_o))
# #print(obraz_crop.size)
# #obraz_crop.show()
# r_45 = obraz_crop.rotate(315)
# #r_45.show()
# obraz2.paste(r_45,(int(w_o - w), int(h_o - h)))
# obraz2.show()
# obraz2.save(path+"wklejanie.png")

### Tekściki here
# base = Image.open("img2.jpeg").convert('RGBA')
# text1 = "Niem się odezwiesz,"
# text2 = "pomyśl pierwej nieco,"
# text3 = "bo czesto słowa"
# text4 = "jakby z worka lecą."
# txt = Image.new('RGBA', base.size, (0, 0, 0, 0))
# wysokosc = int(base.size[1]/4)
# size = 25
# fnt1 = ImageFont.truetype(path2+"../../Lab_13/ttf/DejaVuSansMono-Oblique.ttf", size)
# fnt2 = ImageFont.truetype(path2+"../../Lab_13/ttf/DejaVuSans-BoldOblique.ttf", size)
# fnt3 = ImageFont.truetype(path2+"../../Lab_13/ttf/DejaVuSerif-Bold.ttf", size)
# fnt4 = ImageFont.truetype(path2+"../../Lab_13/ttf/DejaVuSerif.ttf", size)
# d = ImageDraw.Draw(txt)
# left = 10
# d.text((left+15,0+10), text1, font=fnt1, fill=(102, 51, 153, 255), align ="center")
# d.text((left, wysokosc+10), text2, font=fnt2, fill=(255, 0, 0, 255), align="center")
# d.text((left+40,wysokosc*2+10), text3, font=fnt3, fill=(0, 255, 0, 255), align ="center")
# d.text((left+30, wysokosc*3+10), text4, font=fnt4, fill=(0, 0, 255, 255), align="center")
# out = Image.alpha_composite(base, txt)
# out.show()
# out.save("tekst.png")

### Wklejanie 2
# do_wklejenia = Image.open(path2+"obraz1.jpg")
# #do_wklejenia.show()
# base = Image.open(path2+"img1.jpeg")
# #base.show()
# maska = Image.open(path2+"mask3.png")
# #maska.show()

# size = base.size
# dw = do_wklejenia.resize(size,0)
# m = maska.resize(size,0)

# base.paste(dw,(0,0),m)
# #base.show()
# base.save(path+"shrek w neganie.png")

### filtry
# original_image = Image.open(path2+"img2.jpeg")

# original_image = original_image.convert('L')

# emboss = original_image.filter(ImageFilter.EMBOSS)

# sobel1 = original_image.filter(ImageFilter.Kernel(size=(
#     3, 3), kernel=(-1, 0, 1, -2, 0, 2, -1, 0, 1), scale=1, offset=128)).convert('RGB')

# sobel2 = original_image.filter(ImageFilter.Kernel(size=(
#     3, 3), kernel=(-1, -2, -1, 0, 0, 0, 1, 2, 1), scale=1, offset=128)).convert('RGB')

# images = [emboss, sobel1, sobel2]

# figure = plt.figure(figsize=(16, 16))
# for i in range(len(images)):
#     figure.add_subplot(3, 1, i+1)
#     plt.imshow(images[i])
#     plt.axis('off')
# plt.savefig(path+'filtry.jpg')
# plt.show()

### wyrównanie
# im = Image.open(path2+"broken-leg3.jpg")
# original_image = im.convert('L')
# w, h = original_image.size
# pixels = w * h
# hist = original_image.histogram()

# def histogram_norm(image, pixels):
#     hist_norm = image.histogram()
#     hist_norm = [x / pixels for x in hist]

#     return hist_norm


# def histogram_cumul(histogram_normalized):
#     indexes = [x - 1 for x in range(len(histogram_normalized))]
#     hist_cum = [sum(histogram_normalized[:i]) for i in indexes]

#     return hist_cum


# def histogram_equalization(image, histogram_cumulated):
#     image_copy = image.copy()
#     w, h = image.size
#     for i in range(w):
#         for j in range(h):
#             old_pixel = image_copy.getpixel((i, j))
#             new_pixel = int(255 * histogram_cumulated[old_pixel])
#             image_copy.putpixel((i, j), new_pixel)
#     return image_copy


# def statystyki(im):
#    s = stat.Stat(im)
#    print("max i min ", s.extrema)  # max i min
#    print("zlicza ", s.count)  # zlicza
#    print("srednia ", s.mean)  # srednia
#    print("mediana ", s.median)  # mediana
#    print("odchylenie standardowe ", s.stddev)  # odchylenie standardowe

# hist_norm = histogram_norm(original_image, pixels)
# hist_cumul = histogram_cumul(hist_norm)
# hist_eq = histogram_equalization(original_image, hist_cumul)
# statystyki(hist_eq)

# 1086540/ 124/ 134/ 84
