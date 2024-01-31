# Implemetation of Image intensity slicing technique for image enhancement
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/lion.jpeg",0)
row,column = img.shape
img1 = np.zeros_like(img,dtype=np.uint8)
min = 10
max = 60
for i in range(row):
    for j in range(column):
        if min < img[i,j] < max:
            img1[i,j]=255
        else:
            img1[i,j] = 0
plt.figure(figsize=(12,6))
plt.subplot(211)
plt.imshow(img,cmap='gray')
plt.title('original')
plt.axis('off')
plt.subplot(212)
plt.title('Sliced Image')
plt.imshow(img1,cmap='gray')
plt.axis('off')
plt.show()
