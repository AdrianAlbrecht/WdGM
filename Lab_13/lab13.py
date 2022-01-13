import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageColor


path = "Lab_13/"
# wpisywanie tekstu
base = Image.open(path+"jesien.jpg").convert('RGBA') # otwieramy plik i przygotowujemy kanał alpha do wpisania tekstu
print(base.size)
txt = Image.new('RGBA', base.size, (0,0,0,0)) # nowy obraz do wpisania tekstu, tekst pojawi się na kanale alfa
fnt = ImageFont.truetype(path+"ttf/DejaVuSans-BoldOblique.ttf", 80) # fonty pobieramy z biblioteki fontóow -  ImageFont.truetype(font_path, font_size)
# czcionku truetype są skalowalne
d = ImageDraw.Draw(txt) # wybór kontekstu
tekst = "Cierpliwy dostaje \n wszystko na czas"
d.text((140,140), tekst, font=fnt, fill=(255, 0, 255, 255), align ="left") # right, center
d.text((1000,900), "Chińskie przysłowie", font=fnt, fill=(255,255,255,180))
out = Image.alpha_composite(base, txt)
plt.title("wstawianie tekstu")
plt.axis('off')
plt.imshow(out)
plt.show()

# #********************************************************************************************************
# # rysowanie figur geometrycznych


# img = Image.open("jesien.jpg")
# w, h = img.size
# bbox = [(100, 100), (w - 100, h - 100)] # zakres wstawienia figury, potrzebny  w dalszych przykładach

# # ----------------------------------------------------------
# # prostokat
# #img = Image.new("RGB", (w, h), "#f9f9f9")  # nowy obraz, tryb, rozmiar, kolor --  można narysowac na nowym obrazie
# prostokat = ImageDraw.Draw(img)  # na img rysujemy prostokat (tzw. drawing context)
# prostokat.rectangle(bbox,  outline="blue", width = 3) # zakres, kolory  ramki, grubośc ramki
# #prostokat.rectangle(bbox,  outline="blue", width = 23, fill="#ddddff",) # kolor wypełnienia fill =
# del prostokat  # destroy drawing context
# plt.title("prostokat ")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# # ----------------------------------------------------------
# # elipsa
# img = Image.new("RGB", (w, h), "#f9f9f9")  #
# dctx = ImageDraw.Draw(img)  # skrót dctx od drawing context
# dctx.ellipse(bbox, fill="#ddddff", outline="blue") # w prostokąt bbox wpisuje elipsę
# del dctx
# plt.title("elipsa ")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# # ----------------------------------------------------------
# # łuk
# img = Image.new("RGB", (w, h), "#f9f9f9")
# dctx = ImageDraw.Draw(img)
# dctx.arc(bbox, start=20, end=130, fill="blue") # w zalezności od start i end rysowany jest odpowiedni fragment elipsy wpisanej w prostokąt bbox
# del dctx
# plt.title("łuk  ")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# # łuk2
# img = Image.new("RGB", (w, h), "#f9f9f9")
# dctx = ImageDraw.Draw(img)
# dctx.arc(bbox, start=20, end=300, fill="blue")
# del dctx
# plt.title("łuk2")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# # cięciwa z łukiem
# img = Image.new("RGB", (w, h), "#f9f9f9")
# dctx = ImageDraw.Draw(img)
# dctx.chord(bbox, start=20, end=130, fill="#ddddff", outline="blue")
# del dctx
# plt.title("cięciwa ")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# # cieciwa z łukiem 2
# img = Image.new("RGB", (w, h), "#f9f9f9")
# dctx = ImageDraw.Draw(img)
# dctx.chord(bbox, start=20, end=300, fill="#ddddff", outline="blue")
# del dctx  # destroy drawing context
# plt.title("cieciwa z łukiem 2")
# plt.axis('off')
# plt.imshow(img)
# plt.show()


# # ----------------------------------------------------------
# # wycinek koła
# img = Image.new("RGB", (w, h), "#f9f9f9")
# dctx = ImageDraw.Draw(img)  #
# dctx.pieslice(bbox, start=20, end=130, fill="#ddddff", outline="blue")
# del dctx
# plt.title("wycinek koła ")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# # wycinek koła 2 (end=300)
# img = Image.new("RGB", (w, h), "#f9f9f9")
# dctx = ImageDraw.Draw(img)  # create drawing context
# dctx.pieslice(bbox, start=20, end=300, fill="#ddddff", outline="blue")
# del dctx
# plt.title("wycinek kola 2")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# # ---------------------------------------------------------------------
# # wielokąt
# img = Image.new("RGB", (w, h), "#f9f9f9")
# dctx = ImageDraw.Draw(img)
# coordinates = [(10,10), (100,10), (100,50), (50,80), (50,50), (10,10)]
# dctx.polygon(coordinates, fill="#eeeeff", outline="blue")
# plt.title("wielokąt")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# #********************************************************************
# # punkty

# img = Image.new("RGB", (16, 16), "#f9f9f9")  # tworzy nowy obraz
# dctx = ImageDraw.Draw(img)  # tworzy kontekst rysunku
# dctx.point([(2, 3)], fill="blue")  # rysuje punkt niebieski
# dctx.point([(3, 5)], fill="green")  # rysuje punkt zielony
# dctx.point([(5, 8)], fill="red")  # rysuje punkt czerwony
# dctx.point([(8, 2)], fill="pink")  # rysuje punkt różowy
# del dctx  # destroy drawing context
# img = img.resize((128, 128)) # powiekszamy obrazek, żeby zobaczyć punkty
# plt.title("punkty ")
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# # -----------------------------------------------------------------------------------------
# #lista kolorów

# def rgb_to_hex(red, green, blue):
#     return '#%02x%02x%02x' % (red, green, blue)
# print(rgb_to_hex(126,200,230))


# def hex_to_rgb(value):
#     value = value.lstrip('#')
#     lv = len(value)
#     return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# def wypisz_kolory():
#     for n, hex in ImageColor.colormap.items():
#         print(n, hex, hex_to_rgb(hex))

# print(ImageColor.colormap.items())
# wypisz_kolory()