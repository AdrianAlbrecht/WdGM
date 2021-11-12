from PIL import Image
import numpy as np

print("*****Zad2*********************************************************************************************")
tablica_reczna = np.loadtxt("lab1/5_mapa.txt", dtype=np.bool_)
obrazek = Image.open("lab1/obrazek.bmp")
dane_obrazka = np.asarray(obrazek)
if (dane_obrazka == tablica_reczna).all():
    print("Tablice są równe")
else:
    print("Tablice nie są równe")
