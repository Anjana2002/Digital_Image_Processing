# Implemetation of image Sharpening filters and Edege Detection using Gradient Filters
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('images/lion.jpeg')
blur_img = cv2.GaussianBlur(img,(3,3,),0)
kernel = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])
sharpen_img = cv2.filter2D(img,-1,kernel)
edge = cv2.Canny(image=blur_img,threshold1=100,threshold2 = 200)

plt.figure(figsize=(12,8))
plt.subplot(221)
plt.title('original')
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('Blur Image')
plt.imshow(cv2.cvtColor(blur_img,cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('sharpen_img')
plt.imshow(cv2.cvtColor(sharpen_img,cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('Edge')
plt.imshow(cv2.cvtColor(edge,cv2.COLOR_BGR2RGB))


plt.tight_layout()
plt.show()