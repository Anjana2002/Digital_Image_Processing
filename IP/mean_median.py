import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
img=cv2.imread('images/zebra.jpeg')
blur=cv2.blur(img,(5,5))
median=cv2.medianBlur(img,5)
gblur=cv2.GaussianBlur(img,(5,5),0)

plt.figure(figsize=(12,6))

plt.subplot(221)
plt.title('original image')
plt.imshow(img)
plt.axis("off")

plt.subplot(222)
plt.title('Blurred image')
plt.imshow(blur)
plt.axis("off")

plt.subplot(223)
plt.title('median blur')
plt.imshow(median)
plt.axis("off")

plt.subplot(224)
plt.title('Guassianblur')
plt.imshow(gblur)
plt.axis("off")

plt.tight_layout()
plt.show()