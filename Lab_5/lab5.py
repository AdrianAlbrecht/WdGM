# RGB_16bits_palette_sample_image.png
from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# Zadanie 1
image = Image.open("Lab_5/RGB_16bits_palette_sample_image.png")
tab_image = np.asarray(image, dtype=np.uint8)

# Zadanie 2
red = Image.fromarray(tab_image[:, :, 0])
green = Image.fromarray(tab_image[:, :, 1])
blue = Image.fromarray(tab_image[:, :, 2])
red.show()
red.save("Lab_5/im_r.png")
green.show()
green.save("Lab_5/im_g.png")
blue.show()
blue.save("Lab_5/im_b.png")

# Zadanie 3
image_canal = Image.Image.split(image)
image_canal[0].show()
image_canal[1].show()
image_canal[2].show()

# Zadanie 4
union_image = Image.merge('RGB', (red, image_canal[1], image_canal[2]))
union_image.show()

# Zadanie 4.1
roznice = ImageChops.difference(image, union_image)
tablica_roznic = np.asarray(roznice, dtype=np.uint8)

if tablica_roznic.all()==0:
    print("Tablice nie mają różnic :)")
else:
    print("Tablice mają różnice!!!!")

# Zadanie 4.2
tab_new_image = np.asarray(union_image, dtype=np.uint8)

if np.array_equal(tab_image, tab_new_image):
    print("Tablice są identyczne :)")
else:
    print("Tablice nie są identyczne!!!!!")

# Zadanie 5

def szary(w, h, dzielnik):
    czy_rysowac = False
    t = (h, w)
    tab = np.full(t, 255, dtype=np.uint8)
    grubosc = int(w / dzielnik)
    ilosc_pasow = int(w / grubosc)
    roznica = int(255 / ilosc_pasow)
    odcien = 0 - roznica
    for i in range(0, h, 1):
        for j in range(0, w, 1):
            if j % grubosc == 0:
                czy_rysowac = not(czy_rysowac)
                odcien += roznica
            if czy_rysowac:
                tab[i, j] = odcien
        odcien = 0 - roznica
    return tab


tablica_szary = np.array(szary(150, 200, 10))
obraz_szary = Image.fromarray(tablica_szary)
obraz_szary.save("Lab_5/z5.png")
obraz_szary.show()

im1 = Image.merge('RGB', (obraz_szary, green, blue))
im2 = Image.merge('RGB', (red, obraz_szary, blue))
im3 = Image.merge('RGB', (red, green, obraz_szary))
im4 = Image.merge('RGB', (obraz_szary, green, obraz_szary))
im5 = Image.merge('RGB', (obraz_szary, obraz_szary, blue))
im6 = Image.merge('RGB', (red, obraz_szary, obraz_szary))

plt.figure(figsize=(16, 16))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(globals()[f'im{i + 1}'])
plt.show()

# Zadanie 6

tab_red, tab_green, tab_blue = np.array(red), np.array(green), np.array(blue)

w1 = 0.2
w2 = 0.1
w3 = 0.7
image_weight_sum = (w1 * tab_red) + (w2 * tab_green) + (w3 * tab_blue)
image_weight = Image.fromarray(image_weight_sum)
image_weight.show()
Image.fromarray(np.asarray(image_weight, dtype=np.uint8)).save("Lab_5/z6.png")

# Zadanie 7
gwiazda = Image.open("Lab_5/gwiazdka.png").convert('L')
kolo = Image.open("Lab_5/kolo.png").convert('L')
romb = Image.open("Lab_5/romb.png").convert('L')

im1 = Image.merge('RGB', (gwiazda, kolo, romb))
im2 = Image.merge('RGB', (gwiazda, romb, kolo))
im3 = Image.merge('RGB', (kolo, romb, gwiazda))
im4 = Image.merge('RGB', (kolo, gwiazda, romb))
im5 = Image.merge('RGB', (romb, gwiazda, kolo))
im6 = Image.merge('RGB', (romb, kolo, gwiazda))

plt.figure(figsize=(16, 16))
for i in range(6):
    plt.subplot(2, 3, i + 1)

    plt.imshow(globals()[f'im{i + 1}'])
plt.show()
