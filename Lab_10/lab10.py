import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path='Lab_10/'
obraz = Image.open(path+'obraz.png').convert('RGB')

# Zadanie 1

# NEAREST = NONE = 0
# BOX = 4
# BILINEAR = LINEAR = 2
# HAMMING = 5
# BICUBIC = CUBIC = 3
# LANCZOS = ANTIALIAS = 1

def zmien_rozmiar(obraz, s1, s2, filtr):
    w, h = obraz.size
    w = int(w*s1)
    h = int(h*s2)

    return obraz.resize(size=(w, h), resample=filtr)

obraz.show()
zmien_rozmiar(obraz, 1/3, 1/3, 0).show()
zmien_rozmiar(obraz, 1/3, 1, 1).show()
zmien_rozmiar(obraz, 1, 1/3, 2).show()
zmien_rozmiar(obraz, 1/3, 4/3, 3).show()
zmien_rozmiar(obraz, 4/3, 1/3, 4).show()
zmien_rozmiar(obraz, 4/3, 4/3, 5).show()
obraz.show()

# Zadanie 2
obraz_nearest = zmien_rozmiar(obraz, 1/3, 1/3, 0)
obraz_box = zmien_rozmiar(obraz, 1/3, 1/3, 4)
obraz_bilinear = zmien_rozmiar(obraz, 1/3, 1/3, 2)
obraz_hamming = zmien_rozmiar(obraz, 1/3, 1/3, 5)
obraz_bicubic = zmien_rozmiar(obraz, 1/3, 1/3, 3)
obraz_lanczos = zmien_rozmiar(obraz, 1/3, 1/3, 1)

obraz_filtered = [obraz_nearest, obraz_box, obraz_bilinear,
                   obraz_hamming, obraz_bicubic, obraz_lanczos]


figure = plt.figure(figsize=(32, 32))
for i in range(len(obraz_filtered)):
    plt.subplot(3, 2, i+1)
    plt.imshow(obraz_filtered[i])
plt.savefig(path+'resize.jpg')
plt.show()

# Zadanie 3
glowa = obraz.resize(size=obraz.size, box=(40, 5, 190, 155))
glowa = glowa.resize((glowa.size[0]*2,glowa.size[1]*3))
glowa.show()
glowa.save(path+"glowa.jpg")

# Zadanie 4
czerwony_60 = obraz.rotate(60, expand=1, fillcolor="red")
czerwony_60.show()
czerwony_60.save(path+"obrot1.jpg")

# Zadanie 5
zolty_30 = obraz.rotate(330, fillcolor="yellow")
zolty_30.show()
zolty_30.save(path+"obrot2.jpg")

# Zadanie 6
rozowy_45 = obraz.rotate(45, center=(92,97), fillcolor="pink")
rozowy_45.show()
rozowy_45.save(path+"obrot3.jpg")

rozowy_45_not_center = obraz.rotate(45, fillcolor="pink")
rozowy_45_not_center.show()



