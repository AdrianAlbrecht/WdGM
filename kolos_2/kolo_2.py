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

path = "kolos_2/obrazy do kolokwium 2-20220117/"

# # Zadanie 1
# # obraz = Image.open(path+'crop5.jpg')
# # obraz.show()
# # obraz2 = Image.open(path+'img5.jpeg')
# # #obraz2.show()
# # print(obraz.size)
# # obraz_crop = obraz2.crop((500, 0, 850, 400))
# # print(obraz_crop.size)
# # obraz_crop.show()
# # ImageChops.difference(obraz, obraz_crop).show()
# # if(all(pixel == (0, 0, 0) for pixel in list(ImageChops.difference(obraz, obraz_crop).getdata()))):
# #     print("Obrazki są identyczne")
# # else:
# #     print("Obrazki NIE są identyczne")
    
# # Zadanie 2

# # Zadanie 3
# # my_image = Image.open(path+"obraz3.jpg")
# # zdjecie_przefiltrowane = Image.open(path+"filtered5.jpg")
# # my_image.show()
# # zdjecie_przefiltrowane.show()

# # image1 = my_image.filter(ImageFilter.BLUR)
# # image2 = my_image.filter(ImageFilter.DETAIL)
# # image3 = my_image.filter(ImageFilter.EDGE_ENHANCE)
# # image4 = my_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
# # image5 = my_image.filter(ImageFilter.FIND_EDGES)
# # image6 = my_image.filter(ImageFilter.SHARPEN)
# # image7 = my_image.filter(ImageFilter.SMOOTH)
# # image8 = my_image.filter(ImageFilter.SMOOTH_MORE)
# # image9 = my_image.filter(ImageFilter.CONTOUR)
# # image10 = my_image.filter(ImageFilter.EMBOSS)
# # image11 = my_image.filter(ImageFilter.BoxBlur(1))
# # image12 = my_image.filter(ImageFilter.GaussianBlur)
# # image13 = my_image.filter(ImageFilter.UnsharpMask)
# # image14 = my_image.filter(ImageFilter.Kernel(size=(3, 3), kernel=(0, -1, 0, -1, 10, -1, 0, -1, 0), scale=6, offset=0))
# # image15 = my_image.filter(ImageFilter.RankFilter(3, 0))
# # image16 = my_image.filter(ImageFilter.MedianFilter)
# # image17 = my_image.filter(ImageFilter.MinFilter)
# # image18 = my_image.filter(ImageFilter.MaxFilter)
# # ImageFilter.EMBOSS.filterargs = (
# #     (3, 3), 1, 128, (-1, 0, 1, -2, 0, 2, -1, 0, 1))
# # image19 = my_image.filter(ImageFilter.EMBOSS)
# # ImageFilter.EMBOSS.filterargs = (
# #     (3, 3), 1, 128, (-1, -2, -1, 0, 0, 0, 1, 2, 1))
# # image20 = my_image.filter(ImageFilter.EMBOSS)

# # all_images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11,
# #               image12, image13, image14, image15, image16, image17, image18, image19, image20]

# # filter_names = ["Blur", "Detail", "Edge Enhance", "Edge Enhance More", "Find Edges", "Sharpen", "Smooth", "Smooth More", "Emboss", "Box Blur",
# #                 "Gaussian Blur", "Unsharpen Mask", "Kernel", "Rank Filter", "Median Filter", "MinFilter", "Max Filter", "Sobel1", "Sobel2"]


# # for i in range(len(all_images)):
# #    image_diff = ImageChops.difference(
# #        zdjecie_przefiltrowane, all_images[i]).getdata()
# #    if all(pixel == (0, 0, 0, 0) for pixel in list(image_diff)):
# #        print(f'Your filtered image is identical to filter {filter_names[i]}')

# # Zadanie 4
# # img = Image.new("RGB", (400, 240), "#ffffff")
# # bbox = [(0,0), (200, 200)]
# # bbox2 = [(200, 0), (400, 200)]
# # dctx = ImageDraw.Draw(img)
# # dctx.ellipse(bbox, outline="limegreen", width=8)
# # dctx.ellipse(bbox2, outline=(205,50,205), width=8)
# # img.show()
# # img.save(path+"zadanie3.jpg")


# print("limegreen:", ImageColor.colormap['limegreen'])

# # limegreen: (50, 205, 50)
# # negatyw: 

# #Zadanie 5


# def hex_to_rgb(value):
#     lv = len(value)
#     return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# base = Image.open(path + "img1.jpeg").convert('RGBA')
# text = "idź wyprostowany wśród tych \n co na kolanach wśród odwróconych \n plecami i obalonych w proch"
# txt = Image.new('RGBA', base.size, (0, 0, 0, 0))
# fnt = ImageFont.truetype(path+"../../Lab_13/ttf/DejaVuSans-BoldOblique.ttf", 15)
# d = ImageDraw.Draw(txt)
# d.text((0,70), text, font=fnt, fill=(102, 51, 153, 255), align ="center")
# print(hex_to_rgb("663399"))
# out = Image.alpha_composite(base, txt)
# out.show()
# out.save(path+"../z5.png")

# #Zadanie 6
# original_image = Image.open(path+"img2.jpeg")

# original_image = original_image.convert('L')
# w, h = original_image.size
# pixels = w * h
# hist = original_image.histogram()


# def histogram_norm(image, pixels):
#     hist_norm = image.histogram()
#     hist_norm = [x / pixels for x in hist]

#     #plt.title("zeby - histogram znormalizowany")
#     #plt.bar(range(256), hist_norm[:256], color='r', alpha=0.5)
#     #plt.show()
#     #plt.savefig('norm.jpg')

#     return hist_norm


# def histogram_cumul(histogram_normalized):
#     indexes = [x - 1 for x in range(len(histogram_normalized))]
#     hist_cum = [sum(histogram_normalized[:i]) for i in indexes]

#     plt.title("zeby - histogram zkumulowany")
#     plt.bar(range(256), hist_cum[:256], color='r', alpha=0.5)
#     plt.show()
#     #plt.savefig('kumul.jpg')

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


# hist_norm = histogram_norm(original_image, pixels)
# hist_cumul = histogram_cumul(hist_norm)
# hist_eq = histogram_equalization(original_image, hist_cumul).convert('RGB')


# sobel1 = original_image.filter(ImageFilter.Kernel(size=(
#     3, 3), kernel=(-1, 0, 1, -2, 0, 2, -1, 0, 1), scale=1, offset=128)).convert('RGB')

# sobel2 = original_image.filter(ImageFilter.Kernel(size=(
#     3, 3), kernel=(-1, -2, -1, 0, 0, 0, 1, 2, 1), scale=1, offset=128)).convert('RGB')

# images = [hist_eq, sobel1, sobel2]

# figure = plt.figure(figsize=(16, 16))
# for i in range(len(images)):
#     figure.add_subplot(3, 1, i+1)
#     plt.imshow(images[i])
# plt.savefig('zad5.jpg')
# plt.show()

#Zadanie 7

# im = Image.open(path+"obraz4.jpg")
# imObrot = Image.open(path+"obrot2.jpg")
# imObrot.show()

# def zad4(image):
#     return image.rotate(angle=300, fillcolor="red")


# image_rotate_red = zad4(im)
# image_rotate_red.show()

# roznica = ImageChops.difference(image_rotate_red, imObrot)
# roznica.show()

# Zadanie 8
im = Image.open(path+"WD3.jpg")
image_split = Image.Image.split(im)
b = image_split[1]


def statystyki(im):
   s = stat.Stat(im)
   print("max i min ", s.extrema)  # max i min
   print("zlicza ", s.count)  # zlicza
   print("srednia ", s.mean)  # srednia
   print("mediana ", s.median)  # mediana
   print("odchylenie standardowe ", s.stddev)  # odchylenie standardowe


statystyki(b)
