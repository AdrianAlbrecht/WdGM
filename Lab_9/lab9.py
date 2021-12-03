from PIL import Image
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL.ImageFilter import (
    CONTOUR, DETAIL, SHARPEN)

path = "Lab_9/"

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

# Zadanie 1
im = Image.open(path+'zeby.jpg')
print(im.mode)
im.show()
im_L = im.convert("L")
print(im_L.mode)
im_L.show()

# Zadanie 2
statystyki(im_L)
# extrema  [(0, 255)]       -   Najmniejsza i największa wartość jest na granicy wartości (mniejsze bądź większe być nie mogą )
# count[403900]             -   suma wszytskich wartości odcieni szarości wynosi 403900
# mean[137.61641743005694]  -   średnia wartość pixela to 137,61
# median[156]               -   mediana wartości pixela wynosi 157
# stddev[83.42975190652318] -   odchylenie standardowe to 83,42, czyli od wartości środkowej większość wartości znajduje się +- o 83/84 
hist = im_L.histogram()
#print(hist)
plt.title("histogram - zeby.jpg ")
plt.plot(hist)
plt.show()

# Zadanie 3
def histogram_norm(obraz):
    h,w = obraz.size
    size = w*h
    hist = obraz.histogram()
    hist_norm = hist.copy()
    for i in range(0, len(hist), 1):
        hist_norm[i] = hist[i] / size
    return hist_norm


hist_norm = histogram_norm(im_L)
# print(hist)
# print(hist_norm)
plt.title("histogram znormalizowany - zeby.jpg ")
plt.plot(hist_norm)
plt.savefig(path+"norm.jpg")
plt.show()


# Zadanie 4
def histogram_cumul(obraz):
    hist = histogram_norm(obraz)
    hits_cum = [None] * 256
    hits_cum[0]=hist[0]
    for i in range(1, len(hist),1):
        hits_cum[i] = hits_cum[i-1] + hist[i]
    return hits_cum


hist_cumul = histogram_cumul(im_L)
# print(hist)
# print(hist_norm)
plt.title("histogram skumulowany - zeby.jpg ")
plt.plot(hist_cumul)
plt.savefig(path+"kumul.jpg")
plt.show()


# Zadanie 5
def histogram_equalization(obraz):
    hist_cum = histogram_cumul(obraz)
    new_im = obraz.point(lambda i: int(255*hist_cum[i]))
    return new_im
    

im_L.show()
im_eq = histogram_equalization(im_L)
im_eq.show()  
im_eq.save(path+"equalized.jpg")

# Zadanie 7 (6 w domyśle jak mniemam ;) )
im_equalized1 = ImageOps.equalize(im_L, mask=None)
im_equalized1.show()
im_equalized1.save(path+"equalized1.jpg")

# Zadanie 7.1
ImageChops.difference(im_eq, im_equalized1).show() #obrazy są identyczne

# Zadanie 7.2
plt.title("histogram - porównanie ")
plt.bar(range(256), im_eq.histogram(), color='r', alpha=0.5)
plt.bar(range(256), im_equalized1.histogram(), color='b', alpha=0.5)
plt.savefig(path+"porownanie.jpg")
plt.show()

# Zadanie 7.3
print ("====================im_eq===========================")
statystyki(im_eq)
print("====================im_equalized1===========================")
statystyki(im_equalized1)
# extrema[(0, 255)]
# count[114917]
# mean[127.92917496976078]
# median[127]
# stddev[73.6939900387736]

# extrema[(0, 255)]
# count[114917]
# mean[126.7450333719119]
# median[126]
# stddev[73.66424986734268]

# średnia i mediana różnią sie o dosłownie jedna wartość jednostkową, a odchylenie standardowe równi sie nieznacznie

# Zadanie 8
im1 = im_L.filter(ImageFilter.DETAIL).convert("RGB")
im2 = im_L.filter(ImageFilter.SHARPEN).convert("RGB")
im3 = im_L.filter(ImageFilter.CONTOUR).convert("RGB")
im4=im_equalized1.copy().convert("RGB")

figure = plt.figure(figsize=(16, 16))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(globals()[f'im{i + 1}'])
plt.show()
figure.savefig(path+'filtry.jpg')
