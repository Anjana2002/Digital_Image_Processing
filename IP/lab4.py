# Contrast stretching of a low contrast image, Histogram, and Histogram Equalization
import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('images/lion.jpeg',0)

min_intensity = np.min(img)
max_intensity = np.max(img)
stretched_img = (((img - min_intensity)/(max_intensity - min_intensity))*255).astype(np.uint8)

hist_original = cv2.calcHist([img],[0],None,[255],[0,255])
hist_stretched = cv2.calcHist([stretched_img],[0],None,[255],[0,255])

equalized_img = cv2.equalizeHist(img)
hist_equalized_img = cv2.calcHist([equalized_img],[0],None,[255],[0,255])

plt.figure(figsize=(12,8))
plt.subplot(231)
plt.title('original')
plt.imshow(img,'Accent')
plt.axis('off')

plt.subplot(232)
plt.title('Streched Image')
plt.imshow(stretched_img,"Accent")
plt.axis()
plt.subplot(233)

plt.title('Equalized Image')
plt.imshow(equalized_img,"Accent")
plt.axis()

plt.subplot(234)
plt.title('Hist Original')
plt.plot(hist_original)
plt.xlim([0,256])

plt.subplot(235)
plt.title('Hist Streched')
plt.plot(hist_stretched)
plt.xlim([0,256])
plt.subplot(236)

plt.title('Hist Equalized')
plt.plot(hist_equalized_img)
plt.xlim([0,256])
plt.tight_layout()
plt.show()


