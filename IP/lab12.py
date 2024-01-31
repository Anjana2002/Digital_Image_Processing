# Laplacian Edge Detection
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('images/lion.jpeg')
gblur = cv2.GaussianBlur(img,(3,3),0)
g_scale = cv2.cvtColor(gblur,cv2.COLOR_BGR2GRAY)
edges = cv2.Laplacian(g_scale,-1,ksize =3,scale=1,delta=0,borderType = cv2.BORDER_DEFAULT)

plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(132)
plt.title("Gaussian Blur of Image")
plt.imshow(cv2.cvtColor(gblur, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(133)
plt.title("Laplacian Edge of Image")
plt.imshow(edges, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.show()