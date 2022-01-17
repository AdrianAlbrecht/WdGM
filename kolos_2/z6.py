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

path = "kolos_2/"
path2 = "kolos_2/obrazy do kolokwium 2-20220117/"

#Zadanie 6
original_image = Image.open(path2+"img2.jpeg")

original_image = original_image.convert('L')
w, h = original_image.size
pixels = w * h
hist = original_image.histogram()


def histogram_norm(image, pixels):
    hist_norm = image.histogram()
    hist_norm = [x / pixels for x in hist]

    #plt.title("zeby - histogram znormalizowany")
    #plt.bar(range(256), hist_norm[:256], color='r', alpha=0.5)
    #plt.show()
    #plt.savefig('norm.jpg')

    return hist_norm


def histogram_cumul(histogram_normalized):
    indexes = [x - 1 for x in range(len(histogram_normalized))]
    hist_cum = [sum(histogram_normalized[:i]) for i in indexes]

    plt.title("zeby - histogram zkumulowany")
    plt.bar(range(256), hist_cum[:256], color='r', alpha=0.5)
    # plt.savefig(path+'kumul.jpg')
    plt.show()

    return hist_cum


def histogram_equalization(image, histogram_cumulated):
    image_copy = image.copy()
    w, h = image.size
    for i in range(w):
        for j in range(h):
            old_pixel = image_copy.getpixel((i, j))
            new_pixel = int(255 * histogram_cumulated[old_pixel])
            image_copy.putpixel((i, j), new_pixel)
    return image_copy


hist_norm = histogram_norm(original_image, pixels)
hist_cumul = histogram_cumul(hist_norm)
hist_eq = histogram_equalization(original_image, hist_cumul).convert('RGB')


sobel1 = original_image.filter(ImageFilter.Kernel(size=(
    3, 3), kernel=(-1, 0, 1, -2, 0, 2, -1, 0, 1), scale=1, offset=128)).convert('RGB')

sobel2 = original_image.filter(ImageFilter.Kernel(size=(
    3, 3), kernel=(-1, -2, -1, 0, 0, 0, 1, 2, 1), scale=1, offset=128)).convert('RGB')

images = [hist_eq, sobel1, sobel2]

figure = plt.figure(figsize=(16, 16))
for i in range(len(images)):
    figure.add_subplot(3, 1, i+1)
    plt.imshow(images[i])
plt.savefig(path+'zad6.jpg')
plt.show()
