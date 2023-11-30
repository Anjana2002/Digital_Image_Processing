#print mean, S.D, correlation coefficient
import cv2
import numpy as np
img1 = cv2.imread('images/lion.jpeg',0)
img2 = cv2.imread('images/zebra.jpeg',0)

mean_img1 = np.mean(img1)
std_img1 = np.std(img1)
mean_img2 = np.mean(img2)
std_img2 = np.std(img2)

core_coeff = np.corrcoef(img1.flatten(),img2.flatten())[0,1]

print('mean of first image: ',mean_img1)
print('mean of secong image: ',mean_img2)
print('sd of first image: ',std_img1)
print('sd of second image: ',std_img2)
print('correlation coeffiecient : ',core_coeff)