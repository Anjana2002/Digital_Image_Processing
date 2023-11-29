#contrast streching of low contrast image, histogram and fistogram equilization
import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
img = cv2.imread("images/lion.jpeg",0)

min_intensity = np.min(img)
max_intensity = np.max(img)

str_img = (((img-min_intensity)/(max_intensity-min_intensity))*255).astype(np.uint8)
hist_original = cv2.calcHist([img],[0],None,[256],[0,255])
hist_streched = cv2.calcHist([str_img],[0],None,[256],[0,255])
equalized_img = cv2.equalizeHist(img)
hist_equalized = cv2.calcHist([equalized_img],[0],None,[256],[0,255])

plt.figure(figsize=(12,8))
plt.subplot(231)
plt.title("original image")
plt.imshow(img, cmap='gray')
plt.axis('off')


plt.subplot(232)
plt.title("stetched image")
plt.imshow(str_img, cmap='gray')
plt.axis('off')

plt.subplot(233)
plt.title("equalized image")
plt.imshow(equalized_img, cmap='gray')
plt.axis('off')

plt.subplot(234)
plt.title("equilized image")
plt.plot(hist_original)
plt.xlim([0, 256])

plt.subplot(235)
plt.title("hist image")
plt.plot(hist_streched)
plt.xlim([0, 256])

plt.subplot(236)
plt.title("stetched image")
plt.plot(hist_equalized)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
