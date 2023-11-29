#display images from a folder
from PIL import Image
def display(imagepath):
    img = Image.open(imagepath)
    img.show()
    print("Mode of image: ",img.mode)
    print("Format of image: ",img.format)
    print("Size of image: ",img.size)
  
imagepath="/home/nasc/Documents/anjana/IP/images/"
for i in imagepath:
    display(i)