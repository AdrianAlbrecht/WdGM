from PIL import Image
import numpy as np
import math
from random import random

def rysuj_pasy(w, h, dzielnik):
    czy_rysowac = False;
    t = (h, w)
    tab = np.full(t, 255, dtype=np.uint8)
    grubosc = int(w / dzielnik)
    ilosc_pasow = int(w / grubosc)
    roznica = int(255 / ilosc_pasow)
    odcien = 0 - roznica
    for i in range(0,h,1):
        for j in range(0,w,1):
            if j%grubosc == 0:
                czy_rysowac = not(czy_rysowac)
                odcien += roznica
            if czy_rysowac:
                tab[i,j]=odcien
        odcien = 0 - roznica
    return tab


def negatyw(tab, w, h):
    for i in range(0, h, 1):
        for j in range(0, w, 1):
            tab[i,j]=255-tab[i,j]
    return tab


def rysuj_ramke(w, h, dzielnik):
    t = (h, w, 3)
    tablica = np.zeros(t, dtype=np.uint8)
    grubosc = int(min(w, h) / dzielnik)
    ilosc_pasow = math.ceil((h/grubosc)/4)
    roznica = int(255 / ilosc_pasow)
    odcien = 0
    return ramka_rek(tablica, h, w, grubosc, 0, odcien, roznica)


def ramka_rek(tablica, h, w, grubosc, wspolczynnik_przesuniecia, odcien, roznica):
    if (wspolczynnik_przesuniecia > int(w/2)) & (wspolczynnik_przesuniecia > int(h/2)):
        return tablica
    else:
        tablica[wspolczynnik_przesuniecia:h, wspolczynnik_przesuniecia:w] = [odcien,odcien+85, odcien +170]
        for i in range(0+wspolczynnik_przesuniecia, h, 1):
            for j in range(0+wspolczynnik_przesuniecia, w, 1):
                if (i >= grubosc+wspolczynnik_przesuniecia) & (i < h-grubosc) & (j >= grubosc+wspolczynnik_przesuniecia) & (j < w-grubosc):
                    tablica[i, j] = [255,255,255]
        return ramka_rek(tablica, h-(2*grubosc), w-(2*grubosc), grubosc, wspolczynnik_przesuniecia+(2*grubosc), odcien + roznica, roznica)


def negatyw_3d(tab, w, h):
    for i in range(0, h, 1):
        for j in range(0, w, 1):
            for k in range(0, 3, 1):
                tab[i, j, k] = 255-tab[i, j, k]
    return tab


def tab2d_to_3d(tab,w,h):
    t = (h, w, 3)
    tablica = np.zeros(t, dtype=np.uint8)
    for i in range(0, h, 1):
        for j in range(0, w, 1):
            for k in range(0, 3, 1):
                tablica [i, j, k] = tab[i,j]
    return tablica


def kolory(tab, w, grubosc, h_start, h_end):
    ilosc_pasow = int((h_end-h_start)/grubosc)
    roznica = int(255 / ilosc_pasow)
    odcien = 0
    for i in range(h_start, h_end, 1):
        if i % grubosc == 0:
            if i != h_start:
                odcien += roznica
        for j in range(0, w, 1):
            if tab[i, j].all() == 0:
                tab[i,j]=[odcien, odcien +85, odcien +170]
    return tab

# Zadanie 1
# stopniowo każdy kolejny pas będzie jaśniejszy

tab = rysuj_pasy(120, 60, 8)
tab_kopia = tab.copy()
tab_negatyw = negatyw(tab_kopia, 120, 60)
im_ramka = Image.fromarray(tab)
im_negatyw = Image.fromarray(tab_negatyw)
# im_ramka.show()
# im_negatyw.show()
im_ramka.save("Lab_4/z1.jpg")
im_negatyw.save("Lab_4/z1_negatyw.jpg")

# Zadanie 2
# Każda kolejna ramka będzie miała inny kolor według wzoru [x,x+85,x+170] począwszy od x=0, zwiększając z każdą ramką x o wartość (255/ilosc ramek)

tab = rysuj_ramke(120, 60, 16)
tab_kopia = tab.copy()
tab_negatyw = negatyw_3d(tab_kopia, 120, 60)  # Czy to jest na pewno negatyw?
im_ramka = Image.fromarray(tab)
im_negatyw = Image.fromarray(tab_negatyw)
# im_ramka.show()
# im_negatyw.show()
im_ramka.save("Lab_4/z2.jpg")
im_negatyw.save("Lab_4/z2_negatyw.jpg")  

# Zadanie 3
inicjaly = Image.open("Lab_4/obrazek.bmp")
dane_inicjaly = np.asarray(inicjaly)
dane_inicjaly = np.array(dane_inicjaly, dtype='uint8')
dane_inicjaly *= 255
h_start=0
h_end=0
for i in range(0, inicjaly.size[1], 1):
    for j in range(0, inicjaly.size[0], 1):
        if dane_inicjaly[i, j] == 0:
            if h_start==0:
                h_start = i
        if dane_inicjaly[i, j] == 0:
                h_end = i+1
dane_inicjaly = kolory(tab2d_to_3d(dane_inicjaly, inicjaly.size[0], inicjaly.size[1]), inicjaly.size[0], 5, h_start, h_end)
im_ramka = Image.fromarray(dane_inicjaly)
#im_ramka.show()
im_ramka.save("Lab_4/z3.jpg")
