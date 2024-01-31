# Implementation of Image Smoothening Filters(Mean and Median filtering of an Image)
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/lion.jpeg')
mean_blur = cv2.blur(img,(5,5))
median_blur = cv2.medianBlur(img,5)
gaussian = cv2.GaussianBlur(img,(5,5,),0)

plt.figure(figsize=(12,8))
plt.subplot(221)
plt.title('original')
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(222)
plt.title('mean blur')
plt.imshow(cv2.cvtColor(mean_blur,cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(223)
plt.title('median blur')
plt.imshow(cv2.cvtColor(median_blur,cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(224)
plt.title('Gaussian blur')
plt.imshow(cv2.cvtColor(gaussian,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()