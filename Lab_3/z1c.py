from PIL import Image
import numpy as np


def rysuj_prostokaty(w, h, m, n):
    czy_rysowac = True
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    tab[0:h,0:w]=255
    for i in range(0, n, 1):
        for j in range(0, m, 1):
            tab[i, j] = 0
    for i in range(n, h, 1):
        for j in range(m, w, 1):
            tab[i, j] = 0
    return tab


def rysuj_prostokaty_na_odwrot(w, h, m, n):
    czy_rysowac = True
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    tab[0:h, 0:w] = 255
    for i in range(0, m, 1):
        for j in range(0, n, 1):
            tab[i, j] = 0
    for i in range(m, h, 1):
        for j in range(n, w, 1):
            tab[i, j] = 0
    return tab


tab = rysuj_prostokaty(120, 60, 50, 20)
tab2 = rysuj_prostokaty_na_odwrot(120, 60, 50, 20)
im_ramka = Image.fromarray(tab)
im_ramka2 = Image.fromarray(tab2)
im_ramka.show()
im_ramka2.show()
im_ramka.save("obrazek3a.bmp")
im_ramka2.save("obrazek3b.bmp")
