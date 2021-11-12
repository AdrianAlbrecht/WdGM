from PIL import Image
import numpy as np


def zad321(arr1, arr2):
    t = (409, 610)
    arr = np.zeros(t, dtype=np.uint8)
    for i in range(409):
        for j in range(610):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 255
    return arr

def zad322(arr1, arr2):
    t = (409, 610)
    arr = np.zeros(t, dtype=np.uint8)
    for i in range(409):
        for j in range(610):
            if arr1[i][j] == 0 or arr2[i][j] == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 255
    return arr


def zad323_1(arr1, arr2):
    t = (409, 610)
    arr = np.zeros(t, dtype=np.uint8)
    for i in range(409):
        for j in range(610):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                arr[i][j] = 255
            elif arr1[i][j] == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 255
    return arr

def zad323_2(arr1, arr2):
    t = (409, 610)
    arr = np.zeros(t, dtype=np.uint8)
    for i in range(409):
        for j in range(610):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                arr[i][j] = 255
            elif arr2[i][j] == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 255
    return arr

def zad324(arr1, arr2):
    t = (409, 610)
    arr = np.zeros(t, dtype=np.uint8)
    for i in range(409):
        for j in range(610):
            if arr1[i][j] == 0 or arr2[i][j] == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 255
    return arr

def zad326_1(arr1, arr2):
    t = (409, 610)
    arr = np.zeros(t, dtype=np.uint8)
    for i in range(409):
        for j in range(610):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                arr[i][j] = 0
            elif arr1[i][j] == 0:
                arr[i][j] = 255
            else:
                arr[i][j] = 0
    return arr


def zad326_2(arr1, arr2):
    t = (409, 610)
    arr = np.zeros(t, dtype=np.uint8)
    for i in range(409):
        for j in range(610):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                arr[i][j] = 0
            elif arr2[i][j] == 0:
                arr[i][j] = 255
            else:
                arr[i][j] = 0
    return arr

obrazek1 = Image.open("Lab_3/gwiazdka.bmp")
dane_gwiazdka = np.asarray(obrazek1)
obrazek2 = Image.open("Lab_3/kolo.bmp")
dane_kolo = np.asarray(obrazek2)

# 3.2.1
im_ramka = Image.fromarray(zad321(dane_gwiazdka, dane_kolo))
im_ramka.show()
im_ramka.save("Lab_3/z3_2_1.bmp")

# 3.2.2
im_ramka2 = Image.fromarray(zad322(dane_gwiazdka, dane_kolo))
im_ramka2.show()
im_ramka2.save("Lab_3/z3_2_2.bmp")

# 3.2.3
im_ramka31 = Image.fromarray(zad323_1(dane_gwiazdka, dane_kolo)) #roznica kola od gwiazdki
im_ramka31.show()
im_ramka31.save("Lab_3/z3_2_3_kolo_od_gwiazdki.bmp")
im_ramka32 = Image.fromarray(zad323_2(dane_gwiazdka, dane_kolo)) #roznica gwiazdki od kola
im_ramka32.show() 
im_ramka32.save("Lab_3/z3_2_3_gwiazdka_od_kola.bmp")

# 3.2.4
im_ramka4 = Image.fromarray(zad324(dane_gwiazdka, dane_kolo))
im_ramka4.show()
im_ramka4.save("Lab_3/z3_2_4.bmp")

# 3.2.5
im_ramka5 = Image.fromarray(zad321(dane_gwiazdka, dane_kolo)) #czesc wspolna czarny jest tez suma bialych
im_ramka5.show()
im_ramka5.save("Lab_3/z3_2_5.bmp")

# 3.2.6
im_ramka6_1 = Image.fromarray(zad326_1(dane_gwiazdka, dane_kolo)) # gwiazdka od kola
im_ramka6_1.show()
im_ramka6_1.save("Lab_3/z3_2_6_gwiazdka_od_kola.bmp")
im_ramka6_2 = Image.fromarray(zad326_2(dane_gwiazdka, dane_kolo)) # kolo od gwiazdki
im_ramka6_2.show()
im_ramka6_2.save("Lab_3/z3_2_6_kolo_od_gwiazdki.bmp")
