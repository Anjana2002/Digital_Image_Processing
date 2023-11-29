#Display an image
from PIL import Image
def display(imagepath):
    img = Image.open(imagepath)
    img.show()

imagepath = "images/pandass.jpg"
display(imagepath)