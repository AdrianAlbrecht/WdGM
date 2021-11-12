from PIL import Image
import numpy as np

tablica_reczna = np.loadtxt("lab1/5_mapa.txt", dtype=np.uint8)
tablica_reczna = tablica_reczna * 255 #ponieważ będą wartości tylko 0 i 1 a określa się tutaj jakby natężęnie (kontrast), więc albo 0 czyli czarny albo 255 czyli biały
obrazek_reczny = Image.fromarray(tablica_reczna)
obrazek_reczny.show()
