from PIL import Image, ImageDraw, ImageFont
from PIL import ImageColor

path = "kolos_2/"
path2 = "kolos_2/obrazy do kolokwium 2-20220117/"

img = Image.open(path2+"obraz1.jpg")
width = img.size[0]/2
bbox = [(0, 0), (width, width)]
bbox2 = [(width, 0), (width*2, width)]
dctx = ImageDraw.Draw(img)
dctx.ellipse(bbox, outline="limegreen", width=5)
dctx.ellipse(bbox2, outline=(205, 50, 205), width=5)
img.show()
img.save(path+"zadanie3.png")


print("limegreen:", ImageColor.colormap['limegreen'])

# limegreen: (50, 205, 50)
# negatyw: (205, 50, 205)

#Zadanie 6

