# Implementation of transformation of an image
import cv2
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

img = cv2.imread('images/lion.jpeg')
resize_img = cv2.resize(img,(200,200))
rotate_img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
flip_img = cv2.flip(img,0)
flip_img1 = cv2.flip(img,1)
gray_scale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
blurred_img = cv2.GaussianBlur(img,(85,85),0)

plt.figure(figsize=(12,8))
plt.subplot(241)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(242)
plt.title("Resized Image")
plt.imshow(cv2.cvtColor(resize_img,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(243)
plt.title("Rotated Image (180) ")
plt.imshow(cv2.cvtColor(rotate_img,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(244)
plt.title("Horizontal_flipped Image")
plt.imshow(cv2.cvtColor(flip_img1,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(245)
plt.title("Vertical_flipped Image")
plt.imshow(cv2.cvtColor(flip_img,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(246)
plt.title("Gray_scale Image")
plt.imshow(gray_scale,cmap="gray")
plt.axis("off")

plt.subplot(247)
plt.title("Blurred Image")
plt.imshow(blurred_img)
plt.axis("off")
plt.show()