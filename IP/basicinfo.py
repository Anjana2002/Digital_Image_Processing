#Display the basic information of  a image
from PIL import Image
def display(imagepath):
    img = Image.open(imagepath)
    img.show()
    print("Mode of image: ",img.mode)
    print("Format of image: ",img.format)
    print("Size of image: ",img.size)

imagepath="images/pandass.jpg"
display(imagepath)