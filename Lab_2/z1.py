from PIL import Image
import numpy as np

print("*****Zad1*********************************************************************************************")
print("============>Obrazek.bmp")
obrazek = Image.open("lab1/obrazek.bmp") 
print("typ:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)
dane_obrazka = np.asarray(obrazek)
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("wymiar wyrazu tablicy:", dane_obrazka.itemsize)
print("pierwszy wyraz:", dane_obrazka[0][0])
print("drugi wyraz:", dane_obrazka[1][0])

obrazek2 = Image.open("lab1/obrazek2.jpg")
print("============>Obrazek2.jpg")
print("typ", obrazek2.mode)
print("format", obrazek2.format)
print("rozmiar", obrazek2.size)
dane_obrazka2 = np.asarray(obrazek2)
print("typ danych tablicy:", dane_obrazka2.dtype)
print("rozmiar tablicy:", dane_obrazka2.shape)
print("liczba elementow:", dane_obrazka2.size)
print("wymiar tablicy:", dane_obrazka2.ndim)
print("wymiar wyrazu tablicy:", dane_obrazka2.itemsize)
print("pierwszy wyraz:", dane_obrazka2[0][0])
print("drugi wyraz:", dane_obrazka2[1][0])

obrazek3 = Image.open("lab1/obrazek3.png")
print("============>Obrazek3.png")
print("typ", obrazek3.mode)
print("format", obrazek3.format)
print("rozmiar", obrazek3.size)
dane_obrazka3 = np.asarray(obrazek3)
print("typ danych tablicy:", dane_obrazka3.dtype)
print("rozmiar tablicy:", dane_obrazka3.shape)
print("liczba elementow:", dane_obrazka3.size)
print("wymiar tablicy:", dane_obrazka3.ndim)
print("wymiar wyrazu tablicy:", dane_obrazka3.itemsize)
print("pierwszy wyraz:", dane_obrazka3[0][0])
print("drugi wyraz:", dane_obrazka3[1][0])


# - obrazek1 ma typ boolean, czyli przyjmuje wartosci jednostkowe, wiec ilosc elementow bedzie rowny iloczynowy wysokosci i szerokosci
# - obrazek2 ma typ RGB czyli dochodzi dodatkowy potrojny wymiar okreslajacy kolor w RGB, wiec ilosc elementow bedzie rowny iloczynowy wysokosci szerokosci i trójki
# - obrazek2 ma typ RGBA czyli dochodzi dodatkowy poczwórny wymiar okreslajacy kolor w RGB z kanałem alfa (przezroczystość), wiec ilosc elementow bedzie rowny iloczynowy wysokosci szerokosci i czwórki

# Wymiary tablicy obrazów:
# obrazek1: 2
# obrazek2 i 3: 3

# Wymiary wyrazów tablic obrazkow:
# obrazek1: 1
# obrazek2: 3
# obrazek3: 4

# Typy danych tablic obrazkow:
# obrazek1: bool
# obrazek2 i 3: uint8