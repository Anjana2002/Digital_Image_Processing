#print RGB information of a particular pixel
from PIL import Image
def display(image_path):
    img = Image.open(image_path)
    #img.show()
    print("Image size ",img.size)
    print("Image format ",img.format)
    print("Image mode ",img.mode)
    r_channel, g_channel, b_channel = img.split()
    pixel_data = list(img.getdata())
    first_pixel_color = pixel_data[500]
    print("color of first pixel: ",first_pixel_color)
image_path = "red.jpg"
display(image_path)