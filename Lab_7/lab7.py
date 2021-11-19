from PIL import Image
import numpy as np

path = 'Lab_7/'
obraz = Image.open(path+'obraz.jpg')

#Zadanie 1.1
def konwertuj_na_szary(obraz, w1, w2, w3):
    w, h = obraz.size
    obr = obraz.load()
    for i in range(0, w, 1):
        for j in range(0, h, 1):
            x, y, z = obr[i, j]
            obr[i, j] = (int(x*w1+y*w2+z*w3),
                         int(x*w1+y*w2+z*w3),
                         int(x*w1+y*w2+z*w3))

#Zadanie 1.2
w1, w2, w3 = 0.2989, 0.5870, 0.1140
obraz1 = obraz.copy()
konwertuj_na_szary(obraz1, w1, w2, w3)
obraz1.show()
obraz1.save(path+'obraz1.jpg')

#Zadanie 1.3
R,G,B = obraz1.split()
R.show()
print(R.mode)

#Zadanie 2.1
def szary_na_czarnobialy(obraz, wsp):
    w,h = obraz.size
    obr = obraz.load()
    for i in range(0,w,1):
        for j in range(0,h,1):
            if obr[i,j]>(wsp,wsp,wsp):
                obr[i,j]=(255,255,255)
            else:
                obr[i,j]=(0,0,0)
                
#Zadanie 2.2
szary_na_czarnobialy(obraz1,100)
obraz1.show()

#Zadanie 3.1
def utnij_wartości_pikseli(obraz, wsp_min, wsp_max):
    return obraz.point(lambda i: wsp_max if i >= wsp_max else (wsp_min if i <= wsp_min else i))

#Zadanie 3.2
obraz2 = obraz.copy()
obraz2 = utnij_wartości_pikseli(obraz2,50,190)
obraz2.show()
obraz2.save(path+'obraz2.jpg')

#Zadanie 3.3
def utnij_wartości_pikseli2(obraz, wsp_min, wsp_max):
    return obraz.point(lambda i: 1 if i >= wsp_max else (0 if i <= wsp_min else i))

#Zadanie 3.4
obraz3 = obraz.copy()
obraz3 = utnij_wartości_pikseli2(obraz3, 50, 190)
obraz3.show()
obraz3.save(path+'obraz3.jpg')

#Zadanie 4.1
def rysuj_prostokat(obraz, m, n, a, b, kolor):
    obr = obraz.load()
    for i in range(m,m+b+1,1):
        for j in range(n,n+a+1):
            if (i == m)|(i==m+b)|(j==n)|(j==n+a):
                obr[i,j]=kolor


#Zadanie 4.2
obraz4 = obraz.copy()
rysuj_prostokat(obraz4, 25, 25, 25, 25, (250,250,250))
obraz4.show()
obraz4.save(path+'obraz4.jpg')

#Zadanie 4.3
def rysuj_kwadrat(obraz, m, n, a, kolor):
    obr = obraz.load()
    sr=int(a/2)
    for i in range(m-sr, m+sr+1, 1):
        for j in range(n-sr, n+sr+1):
            if (i == m-sr) | (i == m+sr) | (j == n-sr) | (j == n+sr):
                obr[i, j] = kolor
    
#Zadanie 4.4
obraz5 = obraz.copy()
rysuj_kwadrat(obraz5, 25,25,25, (250,250,250))
obraz5.show()
obraz5.save(path+'obraz5.jpg')

#Zadanie 5.1
def odbij_w_poziomie(obraz):
    nowy = Image.new("RGB", obraz.size)
    a = obraz.size[0] - 1
    for x in range(obraz.size[0]):
        for y in range(obraz.size[1]):
            pixel = obraz.getpixel((x, y))
            nowy.putpixel((a, y), pixel)
        a -= 1
    return nowy

#Zadanie 5.2
obraz6 = odbij_w_poziomie(obraz)
obraz6.show()
obraz6.save(path+'obraz6.jpg')

#Zadanie 5.3
def odbij_w_pionie(obraz):
   return obraz.transpose(Image.FLIP_TOP_BOTTOM)

#Zadanie 5.4
obraz7 = odbij_w_pionie(obraz)
obraz7.show()
obraz7.save(path+'obraz7.jpg')

#Zadanie 5.5
def odbij_w_poziomie_przez_środek(obraz):
   nowy = Image.new("RGB", obraz.size)
   a = obraz.size[0] - 1
   obraz_w_polowie = int(obraz.size[0]/2)
   for x in range(obraz.size[0]):
       for y in range(obraz.size[1]):
           if x >= obraz_w_polowie:
               pixel = obraz.getpixel((x, y))
               nowy.putpixel((a, y), pixel)
           else:
               pixel = obraz.getpixel((obraz_w_polowie+x, y))
               nowy.putpixel((obraz_w_polowie+x, y), pixel)
       a -= 1
   return nowy

#Zadanie 5.6
obraz8 = odbij_w_poziomie_przez_środek(obraz)
obraz8.show()
obraz8.save(path+'obraz8.jpg')

#Zadanie 5.7
def odbij_w_pionie_przez_środek(obraz):
    obraz_w_pionie = obraz.transpose(Image.FLIP_TOP_BOTTOM)
    nowy = Image.new("RGB", obraz.size)
    a = obraz.size[1] - 1
    obraz_w_polowie = int(obraz.size[1] / 2)
    for x in range(obraz.size[0]):
        for y in range(obraz.size[1]):
            if y <= obraz_w_polowie:
                pixel = obraz.getpixel((x, y))
                nowy.putpixel((x, y), pixel)
            else:
                pixel = obraz_w_pionie.getpixel((x, y))
                nowy.putpixel((x, y), pixel)
        a -= 1
    return nowy

#Zadanie 5.8
obraz9 = odbij_w_pionie_przez_środek(obraz)
obraz9.show()
obraz9.save(path+'obraz9.jpg')

#Zadanie 6
    # T = np.array(obraz, dtype='uint8')
    # T += 100
    # obraz_wynik = Image.fromarray(T, "RGB")
    # obraz_wynik.show()
T = np.array(obraz, dtype='uint8')

for i in range(obraz.height):
   for j in range(obraz.width):
       for k in range(3):
           if T[i, j, k] >= 155:
               T[i, j, k] = 255
           else:
               T[i, j, k] += 100


obraz_wynik = Image.fromarray(T, "RGB")
obraz_wynik.show()

# obrazek wyświetlał się w niepoprawny sposób ponieważ zakres wartości w kanałach rgb to 255
# gdy dodawaliśmy 100 do pixela o wartości większej niż 155 to wartość wracała do zera
# przez co obraz się nie rozjaśniał
