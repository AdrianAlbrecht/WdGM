from PIL import Image
import numpy as np


def rysuj_pasy(w, h, dzielnik):
    czy_rysowac = True;
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grubosc = int(w / dzielnik)
    for i in range(0,h,1):
        for j in range(0,w,1):
            if j%grubosc == 0:
                czy_rysowac = not(czy_rysowac)
            if czy_rysowac:
                tab[i,j]=255
    return tab


tab = rysuj_pasy(120, 60, 8)
im_ramka = Image.fromarray(tab)
im_ramka.show()
im_ramka.save("obrazek2.bmp")
