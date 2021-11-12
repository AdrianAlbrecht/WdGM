# Obraz posiadający ramkę o grubości x pikseli w kolorze czarnym oraz pionowe czarne linie grubości x piksel licząc x piksel od ramki. Reszta pikseli biała.
# Pseudokod:
# rysowanie domyślnie jako prawda
# for(i=0; i < 200; i++):
# 	for(j=0; j < 200; j++):
# 		- jeżeli i < 5 lub i >= 195 to tab[i][j] = 255
# 		- jeżeli nie to jeżeli j < 5 lub j >= 195 to tab[i][j] = 255
# 		- jeżeli nie to jeżeli i modulo x równe 0 zaneguj ryowanie
# 		- jeżeli nie jeżeli rysowanie to prawda to tab[i][j] = 0

from PIL import Image
import numpy as np


def rysuj_moje(w, h, grub):
    czy_rysowac = True
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = 255
    for i in range(grub, h-grub,1):
        czy_rysowac = True
        for j in range(grub, w-grub,1):
            if j % grub == 0:
                czy_rysowac = not(czy_rysowac)
            if czy_rysowac:
                tab[i, j] = 0
    return tab


tab = rysuj_moje(120, 60, 8)
im_ramka = Image.fromarray(tab)
im_ramka.show()
im_ramka.save("obrazek4.bmp")
