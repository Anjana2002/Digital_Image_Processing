#Stimulation and Display of an Image, Negative of an Image(Binary & Gray Scale)
from PIL import Image,ImageOps
def print_image(image_path):
    img = Image.open(image_path)
    img.show()
    neg_img = ImageOps.invert(img)
    neg_img.show()
    gray_img = ImageOps.grayscale(img)
    gray_img.show()
    gray_scale_neg = ImageOps.invert(gray_img)
    gray_scale_neg.show()

image_path = ('images/lion.jpeg')
print_image(image_path)
