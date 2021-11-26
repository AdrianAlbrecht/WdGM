from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from PIL import ImageEnhance


path = 'Lab_8/'
obraz = Image.open(path+'obraz.jpg')

#Zadanie 1
def filtruj(obraz, kernel, scale):
    w, h = obraz.size
    m = len(kernel)
    obraz_zmiany = obraz.copy()
    tablica_obraz_zmiany = obraz_zmiany.load()
    tablica_obraz = obraz.load()
    for x in range(int(m/2),w - int(m/2)):
        for y in range(int(m/2), h - int(m/2)):
            temp = [0,0,0]
            for a in range(m):
                for b in range(m):
                    xn = x + a - int(m/2)
                    yn = y + b - int(m/2)
                    ramka = tablica_obraz[xn, yn]
                    for c in range(3):
                        temp[c] += ramka[c] * kernel[a][b]
            tablica_obraz_zmiany[x, y] = (int(temp[0]/scale), int(temp[1]/scale), int(temp[2]/scale))
    return obraz_zmiany

# obraz.show()       
# obraz_filtruj_test = filtruj(obraz, ((-1, -2, -1),(-1, 8, -1),(-1, -2, -1)),1)
# obraz_filtruj_test.show()

#Zadanie 2
print(ImageFilter.BLUR.filterargs)
#obraz.show()
obraz_blur = filtruj(obraz, [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], ImageFilter.BLUR.filterargs[1])
#obraz_blur.show()
obraz_blur.save(path+"blur.jpg")
obraz_blur_filtr = obraz.filter(ImageFilter.BLUR)
obraz_blur_filtr.save(path+"blur1.jpg")
#ImageChops.difference(obraz_blur_filtr,obraz_blur).show()

#Zadanie 3.1
print(ImageFilter.SHARPEN.filterargs)
obraz_sharpen = filtruj(obraz, ((-2, -2, -2), (-2, 32, -2),( -2, -2, -2)), ImageFilter.SHARPEN.filterargs[1])
#obraz_sharpen.show()
obraz_sharpen.save(path+"filtr1_1.jpg")
obraz_sharpen_filtr = obraz.filter(ImageFilter.SHARPEN)
obraz_sharpen_filtr.save(path+"filtr1_2.jpg")
#ImageChops.difference(obraz_sharpen_filtr, obraz_sharpen).show()

#Zadanie 3.2
print(ImageFilter.SMOOTH_MORE.filterargs)
obraz_smooth_more = filtruj(obraz, ((1, 1, 1, 1, 1), (1, 5, 5, 5, 1),( 1, 5, 44, 5, 1),( 1, 5, 5, 5, 1),( 1, 1, 1, 1, 1)), ImageFilter.SMOOTH_MORE.filterargs[1])
#obraz_smooth_more.show()
obraz_smooth_more.save(path+'filtr2_1.jpg')
obraz_smooth_more_filter = obraz.filter(ImageFilter.SMOOTH_MORE)
obraz_smooth_more_filter.save(path+"filtr2_2.jpg")
#ImageChops.difference(obraz_smooth_more_filter,obraz_smooth_more).show()

#Zadanie 4
obraz_emboss = obraz.filter(ImageFilter.EMBOSS)
#obraz_emboss.show()
obraz_emboss.save(path+"emboss.jpg")

#Zadanie 5
print(ImageFilter.EMBOSS.filterargs)
obraz_L = obraz.convert("L")
ImageFilter.EMBOSS.filterargs = (
    (3, 3), 1, 128, (-1,  0,  1, -2,  0,  2, -1,  0,  1))
obraz_sobel_1 = obraz_L.filter(ImageFilter.EMBOSS)
#obraz_sobel_1.show()
obraz_sobel_1.save(path+"sobel1.jpg")
ImageFilter.EMBOSS.filterargs = (
    (3, 3), 1, 128, (-1, -2, -1, 0,  0, 0, 1, 2, 1))
obraz_sobel_2 = obraz_L.filter(ImageFilter.EMBOSS)
#obraz_sobel_2.show()
obraz_sobel_2.save(path+"sobel2.jpg")

#Sobel1 jest wypukły, Sobel2 jest wklęsły

#Zadanie 6
im1 = obraz.filter(ImageFilter.DETAIL)
im2 = obraz.filter(ImageFilter.EDGE_ENHANCE)
im3 = obraz.filter(ImageFilter.EDGE_ENHANCE_MORE)
im4 = obraz.filter(ImageFilter.FIND_EDGES)
im5 = obraz.filter(ImageFilter.SMOOTH)
im6 = obraz.filter(ImageFilter.CONTOUR)
im7 = obraz.filter(ImageFilter.BoxBlur(0))
im8 = obraz.filter(ImageFilter.GaussianBlur(radius=2))
im9 = obraz.filter(ImageFilter.UnsharpMask(radius=3, percent=200, threshold=5))
im10 = obraz.filter(ImageFilter.Kernel((3, 3),(-1, -1, -1, -1, 11, -2, -2, -2, -2), 1, 0))
im11 = obraz.filter(ImageFilter.RankFilter(size=3, rank=0))
im12 = obraz.filter(ImageFilter.MedianFilter(size=3))
im13 = obraz.filter(ImageFilter.MinFilter(size=3))
im14 = obraz.filter(ImageFilter.MaxFilter(size=3))

figure = plt.figure(figsize=(16,16))
for i in range(14):
    plt.subplot(2, 7, i + 1)

    plt.imshow(globals()[f'im{i + 1}'])
plt.show()
figure.savefig(path+'reszta.jpg')
