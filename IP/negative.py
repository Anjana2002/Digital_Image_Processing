from PIL import Image,ImageOps
def display(img_path):
    img= Image.open(img_path)
    img.show()

    neg = ImageOps.invert(img)
    neg.show()

    g = ImageOps.grayscale(img)
    g.show()
img_path="images/lion.jpeg"
display(img_path)