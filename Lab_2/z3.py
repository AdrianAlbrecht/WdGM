from PIL import Image
import numpy as np

tablica_reczna = np.loadtxt("lab1/5_mapa.txt", dtype=np.bool_)
obrazek_reczny = Image.fromarray(tablica_reczna)
obrazek_reczny.show()

#Wydaje mi się, że obrazy są identyczne
