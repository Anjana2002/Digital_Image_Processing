#display a list of image
from PIL import Image
def display(imagepath):
    img = Image.open(imagepath)
    img.show()
    print("Mode of image: ",img.mode)
    print("Format of image: ",img.format)
    print("Size of image: ",img.size)
  
imagepath=['images/pandass.jpg','images/zebra.jpeg','images/lion.jpeg','images/images.jpeg','images/cat.jpeg']
for i in imagepath:
    display(i)