import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
img=cv2.imread('images/cat.jpeg')
gblur=cv2.GaussianBlur(img,(3,3),0)
kernel=np.array([[0,7,0],[-1,5,-1],[0,-1,0]])
sharpen_image=cv2.filter2D(img,-1,kernel)
edges=cv2.Canny(image=gblur,threshold1=100,threshold2=200)

plt.figure(figsize=(12,6))

plt.subplot(131)
plt.title('original image')
plt.imshow(img)
plt.axis("off")

plt.subplot(132)
plt.title('sharpend image')
plt.imshow(sharpen_image)
plt.axis("off")

plt.subplot(133)
plt.title('edged image')
plt.imshow(edges)
plt.axis("off")
plt.show()