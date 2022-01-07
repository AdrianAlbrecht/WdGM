from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

path = "Lab_11/"
# Zadanie 1
obraz1 = Image.open(path+"obraz5.jpg")
obraz2 = Image.open(path+"obraz7.jpg")

maska1 = Image.open(path+"maska0.jpg").convert("1")
maska2 = Image.open(path+"maska2.jpg").convert("L")
maska3 = Image.open(path+"maska3.png")

print(obraz1.mode, obraz2.mode, maska1.mode, maska2.mode, maska3.mode)
# obraz1.show()
# obraz2.show()
# maska1.show()
# maska2.show()
# maska3.show()

# Zadanie 2
w, h = obraz1.size
w1, h1 = obraz2.size
# print(w,h,w1,h1)
W = min(w, w1)
H = min(h, h1)
# print(W, H)

o1_resize = obraz1.resize((W, H), 0)
o2_resize = obraz2.resize((W, H), 0)
maska1_resize = maska1.resize((W, H), 0)
maska2_resize = maska2.resize((W, H), 0)
maska3_resize = maska3.resize((W, H), 0)

o1_m1 = o1_resize.copy()
o1_m2 = o1_resize.copy()
o1_m3 = o1_resize.copy()
o2_m1 = o2_resize.copy()
o2_m2 = o2_resize.copy()
o2_m3 = o2_resize.copy()
o1 = o1_resize.crop((10, 10, 100, 150))
o2 = o2_resize.crop((10, 10, 100, 150))
maska1_resize2 = maska1_resize.resize(o2.size, 0)
maska2_resize2 = maska2_resize.resize(o2.size, 0)
maska3_resize2 = maska3_resize.resize(o2.size, 0)
maska1_resize1 = maska1_resize.resize(o1.size, 0)
maska2_resize1 = maska2_resize.resize(o1.size, 0)
maska3_resize1 = maska3_resize.resize(o1.size, 0)

o1_m1.paste(o2, (10, 10), maska1_resize2)
o1_m2.paste(o2, (10, 10), maska2_resize2)
o1_m3.paste(o2, (10, 10), maska3_resize2)
o2_m1.paste(o1, (10, 10), maska1_resize1)
o2_m2.paste(o1, (10, 10), maska2_resize1)
o2_m3.paste(o1, (10, 10), maska3_resize1)

obrazy = [o1_m1, o2_m1, o1_m2, o2_m2, o1_m3, o2_m3]
figure = plt.figure(figsize=(16, 16))
for i in range(len(obrazy)):
    plt.subplot(3, 2, i+1)
    plt.imshow(obrazy[i])
plt.savefig(path+'zadanie2.png')
plt.show()

# Zadanie 3
z3_o1_o2_L = Image.composite(o1_resize, o2_resize, maska2_resize)
z3_o1_o2_RGBA = Image.composite(o1_resize, o2_resize, maska3_resize)
z3_o2_o1_L = Image.composite(o2_resize, o1_resize, maska2_resize)
z3_o2_o1_RGBA = Image.composite(o2_resize, o1_resize, maska3_resize)

obrazy = [z3_o1_o2_L, z3_o2_o1_L, z3_o1_o2_RGBA, z3_o2_o1_RGBA]
figure = plt.figure(figsize=(16, 16))
for i in range(len(obrazy)):
    plt.subplot(2, 2, i+1)
    plt.imshow(obrazy[i])
plt.savefig(path+'zadanie3.png')
plt.show()

#Zadanie 4
obraz3 = Image.open(path+"obraz3.png")
obraz4 = Image.open(path+"obraz4.png")

w, h = obraz3.size
w1, h1 = obraz4.size
W = min(w, w1)
H = min(h, h1)
o3_resize = obraz3.resize((W, H), 0)
o4_resize = obraz4.resize((W, H), 0)

tlo = Image.composite(o3_resize, o4_resize, o3_resize)
tlo.show()
tlo.save(path+"zadanie4.png")

# Zadanie 5
obraz6 = Image.open(path+'obraz1.png')
obraz7 = Image.open(path+'obraz2.png')

im1 = obraz6.copy()
im2 = obraz7.copy()
w1, h1 = im1.size
w2, h2 = im2.size

W = min(w1, w2)
H = min(h1, h2)
print(W, H)

im_duda = im1.resize((W, H), 0)
im_godek = im2.resize((W, H), 0)

i = 1
plt.figure(figsize=(18, 15))
for alpha in np.linspace(0, 1, 20):
    plt.subplot(4, 5, i)
    mix = Image.blend(im_godek, im_duda, alpha=alpha)
    plt.imshow(mix)
    plt.axis('off')
    i += 1
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig(path+'zadanie5.png')
plt.show()

# Zadanie 6
ciekawe = obraz2.copy()
maska_c = Image.open(path+"maska_z6.png")
inferno = Image.open(path+"inferno.png")
skulls = Image.open(path+"skulls.png")
w1, h1 = ciekawe.size
w2, h2 = maska_c.size
W = min(w1, w2)
H = min(h1, h2)
#print(W, H)

#wyrównujemy wielkości obrazów
c = ciekawe.resize((W, H), 0)
m_c = maska_c.resize((W, H), 0)
inf = inferno.resize((W, H), 0)
sk = skulls.resize((W, H), 0)
#print(c.size)
cR = c.transpose(Image.FLIP_LEFT_RIGHT) #obracamy obraz papugi lewo z prawo - papuga ma głowę u góry patrzy w prawo
cTB = c.transpose(Image.FLIP_TOP_BOTTOM)  # obracamy obraz papugi góra z dołem - papuga na dole u góry patrzy w lewo
cTBR = cTB.transpose(Image.FLIP_LEFT_RIGHT) #obracamy obraz papugi góra z dołem i lewo z prawo - papuga na dole u góry patrzy w prawo
#teraz wycinamy główki
cR_crop = cR.crop((75,0,150,100))
cTB_crop = cTB.crop((0,100,75,200))
cTBR_crop = cTBR.crop((75,100,150,200))
#łączymy obrazy względem środka
c.paste(cR_crop,(75,0))
c.paste(cTB_crop,(0,100))
c.paste(cTBR_crop,(75,100))
# W tym momencie mamy obraz przypominający kalejdoskop
# Dodajem maskę Trójkąta Odyna w tło czaszek
c.paste(sk,(0,0),m_c)
# Blendujemy z obrazkiem ognia
mix = Image.blend(inf, c, 0.5)
# To oryginalny obraz
obraz2.show()
# i nasz wynik
mix.show()
mix.save(path+"zadanie6.png")

# Zadanie 7
glowa = obraz3.copy()
cialo = glowa.copy()
glowa = glowa.crop((171,29, 216,93))
glowa_p = glowa.copy()
glowa = glowa.resize((glowa.size[0]*2, glowa.size[1]*2))
glowa.show()
cialo.paste(glowa,(150,0))
cialo.show()
cialo.save(path+"zadanie7.png")

# Zadanie 8
def wlasny_crop(obraz,w1,h1,w2,h2):
    nowy = Image.new(obraz.mode,(w2-w1,h2-h1),(0,0,0))
    for i in range(0,w2-w1,1):
        for j in range(0,h2-h1,1):
            nowy.putpixel((i,j),obraz.getpixel((w1+i, h1+j)))
    return nowy

glowa_wlasny_crop = wlasny_crop(obraz3,171,29,216,93)
glowa_wlasny_crop.show()
glowa_p.show()
if(all(pixel == (0,0,0,0) for pixel in list(ImageChops.difference(glowa_wlasny_crop, glowa_p).getdata()))):
    print("Obrazki są identyczne. Crop dziala")
else:
    print("Obrazki NIE są identyczne. Crop NIE dziala")
