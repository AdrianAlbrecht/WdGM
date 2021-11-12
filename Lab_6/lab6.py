from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1
path='Lab_6/'
obraz = Image.open(path+'obraz.png')
inicjaly = Image.open(path+'inicjaly.bmp')
inicjaly_copy =inicjaly.copy()

#Zadanie 2.1
def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    for i in range(0,inicjaly.size[0],1):
        for j in range(0, inicjaly.size[1], 1):
            if (m+i < obraz.size[0]) & (n+j < obraz.size[1]):
                if inicjaly.getpixel((i, j)) == 0:
                    obraz.putpixel((m+i,n+j),kolor)
            else:
                if inicjaly.getpixel((i, j)) == 0:
                    obraz.putpixel((m+i-obraz.size[0], n+j-obraz.size[1]), kolor)
            

obraz1 = obraz.copy()
obraz2 = obraz.copy()
wstaw_inicjaly(obraz1,inicjaly_copy,15,60,(0,255,0))
obraz1.show()
obraz1.save(path+'obraz1.png')
wstaw_inicjaly(obraz2, inicjaly_copy, 55, 150, (255, 0, 0))
obraz2.show()
obraz2.save(path+'obraz2.png')

#Zadanie 2.2
def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    w, h = inicjaly.size
    for i in range(0,w,1):
        for j in range(0,h,1):
            if inicjaly.getpixel((i, j)) == 0:
                if (m+i < obraz.size[0]) & (n+j < obraz.size[1]):
                    p = obraz.getpixel((i + m, j + n))
                    obraz.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
                else:
                    p = obraz.getpixel((i + m-obraz.size[0], j + n-obraz.size[1]))
                    obraz.putpixel((i + m -obraz.size[0] , j + n -obraz.size[1]), (p[0] + x, p[1] + y, p[2] + z))
                
                
obraz3 = obraz.copy()
obraz4 = obraz.copy()
wstaw_inicjaly_maska(obraz3, inicjaly_copy, 15, 60, 50, 100, -50)
obraz3.show()
obraz3.save(path+'obraz3.png')
wstaw_inicjaly_maska(obraz4, inicjaly_copy, 55, -10, 50, 100, -50)
obraz4.show()
obraz4.save(path+'obraz4.png')

#Zadanie 3
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


def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z): #zmienilem nazwe funkcji bo nie moga byc dwie funkcje o tej samej nazwie w jednym programie
    obr = obraz.load()
    ini = inicjaly.load()
    w, h = inicjaly.size
    for i in range(0, w, 1):
        for j in range(0, h, 1):
            if ini[i, j] == 0:
                if (m+i < obraz.size[0]) & (n+j < obraz.size[1]):
                    p = obr[i + m, j + n]
                    obr[i + m, j + n] = (p[0] + x, p[1] + y, p[2] + z)
                else:
                    p = obr[i + m-obraz.size[0], j + n-obraz.size[1]]
                    obr[i + m -obraz.size[0], j + n -obraz.size[1]] = (p[0] + x, p[1] + y, p[2] + z)
                

obraz_temp1 = obraz.copy()
obraz_temp2 = obraz.copy()
wstaw_inicjaly_load(obraz_temp1, inicjaly_copy, 65, 160, (255, 0, 0))
obraz_temp1.show()
wstaw_inicjaly_maska_load(obraz_temp2, inicjaly_copy, -30, -20, 50, 100, -50)
obraz_temp2.show()

#Zadanie 4.1
def kontrast(obraz, wsp_kontrastu): #wsp_kontrastu := <0,100>
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return obraz.point(lambda i: 128 + (i - 128) * mn)

kontrast(obraz,0).show()
kontrast(obraz,25).show()
kontrast(obraz,50).show()
kontrast(obraz, 75).show() 
kontrast(obraz, 100).show()
# Im większy współczynnik kontrastu tym ciemne obszary stają się ciemniejsze, a jasne jaśniejsze
obraz5 = kontrast(obraz, 40)
obraz5.show()
obraz5.save(path+'obraz5.png')

#Zadanie 4.2
def negatyw(obraz):
    return obraz.point(lambda i: 255-i)


obraz6 = negatyw(obraz)
obraz6.show()
obraz6.save(path+'obraz6.png')

#Zadanie 4.3
def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))


obraz7 = transformacja_logarytmiczna(obraz)
obraz7.show()
obraz7.save(path+'obraz7.png')

#Zadanie 4.4
def transformacja_gamma(obraz, gamma): #gamma > 0
    return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)


transformacja_gamma(obraz, 2).show()
transformacja_gamma(obraz, 4).show()
transformacja_gamma(obraz, 6).show()
transformacja_gamma(obraz, 8).show()
transformacja_gamma(obraz, 10).show()
transformacja_gamma(obraz, 12).show()
transformacja_gamma(obraz, 40).show()
# Im większa gamma, tym jaśniejsze są ciemne obszary, gamma wyłapuje ciemne piksele a nie całkowicie czarne (maksymalna wartosc czarnego) i rozjasnia je
obraz8 = transformacja_gamma(obraz,2)
obraz8.show()
obraz8.save(path+'obraz8.png')

#Zadanie 4.5
def utnij_wartości_pikseli(obraz, wsp_min, wsp_max):
    return obraz.point(lambda i: wsp_max if i>wsp_max else (wsp_min if i<wsp_min else i))


utnij_wartości_pikseli(obraz, 10, 240).show()
utnij_wartości_pikseli(obraz, 30, 210).show()
utnij_wartości_pikseli(obraz, 50, 190).show()
utnij_wartości_pikseli(obraz, 70, 170).show()
utnij_wartości_pikseli(obraz, 90, 150).show()
utnij_wartości_pikseli(obraz, 110, 130).show()

obraz9 = utnij_wartości_pikseli(obraz, 30, 210)
obraz9.show()
obraz9.save(path+'obraz9.png')
