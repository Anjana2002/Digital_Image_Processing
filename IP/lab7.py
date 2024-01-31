# Computation of Mean,Standard Deviation,Correlation coefficient of the given image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# image1 = cv2.imread('images/lion.jpeg')
# image2 = cv2.imread('images/images.jpeg')
# img1 = cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
# img2 = cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
img1 = Image.open('images/lion.jpeg')
img2 = Image.open('images/images.jpeg')
plt.figure(figsize=(12,8))
plt.subplot(221)
plt.title('Before resize- image 1')
plt.imshow(img1)

plt.subplot(222)
plt.title('Before resize-image 2')
plt.imshow(img2)


image1 = np.array(img1)
image2 = np.array(img2)
image1 = cv2.resize(image1,(image2.shape[1],image2.shape[0]))
plt.subplot(223)
plt.title('After resize-image 1')
plt.imshow(image1)

plt.subplot(224)
plt.title('After resize-image 2')
plt.imshow(image2)
plt.show()

mean_img1 = round(np.mean(image1),2)
mean_img2 = np.mean(image2)

std_1 =np.std(image1)
std_2 =np.std(image2)

cor_coeff = np.corrcoef(image1.flatten(),image2.flatten())[0,1]

print('Mean of image 1',mean_img1)
print('Mean of image 2',mean_img2)
print('std of image 1',std_1)
print('std of image 2',std_2)
print('correaltion coeffiecient',cor_coeff)