from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


path_gotowe = "kolos_1/obrazy/"
path = "kolos_1/"

def szary(w, h):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(0, h, 1):
        for j in range(0, w, 1):
            tab[i, j] = (i + 3*j) % 256
    return tab


obraz7 = Image.open(path_gotowe+"obraz7.jpg")
#obraz7.show()
tab_szary = szary(obraz7.size[0], obraz7.size[1])
obraz_szary = Image.fromarray(tab_szary)
#obraz_szary.show()
kanaly = Image.Image.split(obraz7)

im_r = Image.merge("RGB", (obraz_szary, kanaly[1], kanaly[2]))
im_g = Image.merge("RGB", (kanaly[0], obraz_szary, kanaly[2]))
im_b = Image.merge("RGB", (kanaly[0], kanaly[1], obraz_szary))

obrazy = [obraz7, im_r, im_g, im_b]


figure = plt.figure(figsize=(16, 16))
for i in range(len(obrazy)):
    plt.subplot(2, 2, i+1)
    plt.imshow(obrazy[i])
plt.savefig(path+'mix.jpg')
plt.show()
