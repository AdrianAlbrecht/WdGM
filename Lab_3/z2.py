from PIL import Image
import numpy as np

obrazek = Image.open("Lab_3/obrazek.bmp")
tab = np.asarray(obrazek)
for i in range(0, len(tab)):
    for j in range(0, len(tab[i])):
        tab[i,j]= not(tab[i,j])
obrazek_negacja = Image.fromarray(tab)
obrazek_negacja.show()
obrazek_negacja.save("Lab_3/inicjaly_negatyw.bmp")
