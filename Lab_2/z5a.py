from PIL import Image
import numpy as np


def rysuj_ramke(w, h, dzielnik):
    t = (h, w)
    tablica = np.zeros(t, dtype=np.uint8)
    grubosc = int(min(w, h) / dzielnik)
    return ramka_rek(tablica, h, w, grubosc, 0)


def ramka_rek(tablica, h, w, grubosc, wspolczynnik_przesuniecia):
    if (wspolczynnik_przesuniecia>int(w/2))&(wspolczynnik_przesuniecia>int(h/2)):
        return tablica
    else:
        tablica[wspolczynnik_przesuniecia:h,wspolczynnik_przesuniecia:w] = 0
        for i in range(0+wspolczynnik_przesuniecia,h,1):
            for j in range(0+wspolczynnik_przesuniecia, w, 1):
                if (i >= grubosc+wspolczynnik_przesuniecia) & (i < h-grubosc)&(j >= grubosc+wspolczynnik_przesuniecia) & (j < w-grubosc):
                    tablica [i,j]=255
        return ramka_rek(tablica, h-(2*grubosc), w-(2*grubosc), grubosc, wspolczynnik_przesuniecia+(2*grubosc))



tab = rysuj_ramke(120, 60, 8)
im_ramka = Image.fromarray(tab)
im_ramka.show()
im_ramka.save("obrazek1.bmp")
