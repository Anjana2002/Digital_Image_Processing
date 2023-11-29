#read an image, display image, and its negative image by gray scale
from PIL import Image
import numpy as np
import cv2
gray_image = cv2.imread("images/lion.jpeg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Grayscale image",gray_image)
cv2.waitKey(0)

negative_gray_image = 255-gray_image
cv2.imshow("Negative Grayscale",negative_gray_image)
cv2.waitKey(0)
 