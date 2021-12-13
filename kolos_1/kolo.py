from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

path_gotowe = "kolos_1/obrazy/"
path = "kolos_1/"


#Zadanie 1
obrazek = Image.open(path_gotowe+"obraz2.jpg")
dane_obrazka = np.asarray(obrazek)

print("rozmiar:", obrazek.size)
print("typ danych tablicy:", dane_obrazka.dtype)
print(obrazek.getpixel((162,305)))
print(dane_obrazka[351][127])


#Zadanie 2

im = obrazek.copy()
#im.show()
a = 12
b = 3
im = im.point(lambda i: i * a +b)
#im.show()

# Zadanie 3
#Pobierz obraz maska2.jpg i pobierz obraz obraz9.jpg
# Nastepnie, na obrazie obraz9.jpg zmien wartości pikesli odpowiadających czarnym pikselom maski
# w nastepujący sposób
# 1. lewy górny róg maski pokrywa sie z lewym górnym rogiem obrazu
# 2. wartości kanału r ściemniają się o 130
# 3. wartości kanału g rozjaśniają się o 120
# 4. wartości kanału b rozjaśniają się o 160
# W odpowiedzi wstaw obraz końcowy

obraz = Image.open(path_gotowe+"obraz9.jpg")
maska = Image.open(path_gotowe+"maska2.jpg")
                    
#obraz.show()
tablica_maski = np.asarray(maska)
tablica_obrazu = np.asarray(obraz)
wymiar_tablicy = np.shape(maska)
for i in range(wymiar_tablicy[0]):
    for j in range(wymiar_tablicy[1]):
        if tablica_maski[i, j] == 0:
            if tablica_obrazu[i, j, 0] < 130:
                tablica_obrazu[i, j, 0] = 0
            else:
                tablica_obrazu[i, j, 0] = tablica_obrazu[i, j, 0] -130
            if tablica_obrazu[i, j, 1] > 135:
                tablica_obrazu[i, j, 1] = 255
            else:
                tablica_obrazu[i, j, 1] = tablica_obrazu[i, j, 1] + 120
            if tablica_obrazu[i, j, 2] > 95:
                tablica_obrazu[i, j, 2] = 255
            else:
                tablica_obrazu[i, j, 2] = tablica_obrazu[i, j, 2] + 160
obraz2 = Image.fromarray(tablica_obrazu)
#obraz.show()
obraz2.save(path+"z1.jpg")

#Zadanie 4
obraz3 = obrazek.copy()
kanaly = Image.Image.split(obraz3)
obraz3 = Image.merge('RGB', (kanaly[2], kanaly[1], kanaly[0]))
#obraz3.show()

# Zadanie 5
# Utwórz obraz z pliku tekstowego tab2.txt i pobierz obraz obraz4.jpg
# Nastepnie, wstaw obraz powstały z tablicy w obraz obraz4.jpg tak, żeby
# czarne piksele były w kolorze niebieskim a białe piksele nic nie zmieniały w obrazie
# oraz tak, że prawy górny róg obrazu utworzonego z tablicy pokrywał się z prawym górnym rogiem obrazu
# W odpowiedzi wstaw obraz koncowy.

tablica_maski = np.loadtxt(path_gotowe+"tab2.txt", dtype=np.bool_)
maska = Image.fromarray(tablica_maski)
obraz4 = Image.open(path_gotowe+"obraz4.jpg")
tablica_obrazu = np.asarray(obraz4)

wymiar_tablicy = np.shape(tablica_maski)
print(np.shape(tablica_maski))
print(np.shape(tablica_obrazu))


def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obr = obraz.load()
    ini = inicjaly.load()
    for i in range(0, inicjaly.size[0], 1):
        for j in range(0, inicjaly.size[1], 1):
            if (m+i < obraz.size[0]) & (n+j < obraz.size[1]):
                if ini[i, j] == 0:
                    obr[m+i, n+j] = kolor
            else:
                if ini[i, j] == 0:
                    obr[m+i-obraz.size[0], n+j-obraz.size[1]] = kolor
                    
# obraz4.show()
# maska.show()
wstaw_inicjaly_load(obraz4, maska, 316,0,(0,0,255))
# obraz4.show()
obraz4.save(path+"z4.jpg")

# Zadanie 6
def rysuj_ramke_kolor(w, h, dzielnik, r, g, b):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = [255, 0, 0]
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2, 0] = r
    tab[grub:z1, grub:z2, 1] = g
    tab[grub:z1, grub:z2, 2] = b
    return tab


#Image.fromarray(rysuj_ramke_kolor(100, 60, 3, 100, 200, 300)).show()

#Zadanie 7
# 1. Napisz program szary(w, h), który tworzy tablicę obrazu o wymiarach w, h
# według wzoru(i + 3*j) % 256  gdzie i, j sa indeksami tablicy.
# 2. Nastepnie pobierz obraz obraz7.jpg i korzystając z programu stwórz obraz szary odpowiednich rozmiarów.
# 3. Stwórz 3 obrazy, które powstaja przez zastąpnie, odpowiednio, kanałów r, g, b obrazu obraz7.jpg obrazem szarym
# 4. Przedstaw na jednym diagramie plt obraz obraz7.jpg i trzy obrazy z pkt3. Zapisz jako obraz mix.jpg
# W odpowiedzi wstaw plik z kodem i obraz mix.jpg

def szary(w, h):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(0,h, 1):
        for j in range(0, w, 1):
            tab[i, j] = (i + 3*j) % 256
    return tab


obraz7 = Image.open(path_gotowe+"obraz7.jpg")
#obraz7.show()
tab_szary = szary(obraz7.size[0], obraz7.size[1])
obraz_szary = Image.fromarray(tab_szary)
#obraz_szary.show()
kanaly = Image.Image.split(obraz7)

im_r = Image.merge("RGB",(obraz_szary,kanaly[1],kanaly[2]))
im_g = Image.merge("RGB", (kanaly[0], obraz_szary,kanaly[2]))
im_b = Image.merge("RGB", (kanaly[0], kanaly[1], obraz_szary))

obrazy = [obraz7, im_r, im_g, im_b]


figure = plt.figure(figsize=(16, 16))
for i in range(len(obrazy)):
    plt.subplot(2, 2, i+1)
    plt.imshow(obrazy[i])
plt.savefig(path+'mix.jpg')
#plt.show()

# Zadanie 8

# Pobierz obrazy owal3.bmp i prostakat1.jpg
# utwórz i zapisz obraz wynik.jpg, który jest   sumą białych fragmentów  tych obrazów.
# Wskazówka: W razie potrzeby dokonaj konwersji odpowiedniego obrazu.
# W odpowiedzi wstaw  obraz wynik.jpg

owal = Image.open(path_gotowe+"owal3.bmp")
prostokat = Image.open(path_gotowe+"prostokat1.jpg").convert('1')
owal.show()
prostokat.show()

dane_owal = np.asarray(owal)
dane_prostokat = np.asarray(prostokat)

# print(owal.mode)
# print(prostokat.mode)


def zad321(arr1, arr2):
    t = arr1.shape
    arr = np.zeros(t, dtype=np.bool)
    for i in range(t[0]):
        for j in range(t[1]):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 1
    return arr

im_ramka = Image.fromarray(zad321(dane_owal, dane_prostokat))
im_ramka.show()
im_ramka.save(path+"wynik.jpg")



