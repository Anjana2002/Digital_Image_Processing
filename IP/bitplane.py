import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('images/lion.jpeg', 0)
bit_plane = []
for i in range(8):
    plane = np.zeros_like(img,dtype=np.uint8)
    plane[img & (1<<i)!=0]=255
    bit_plane.append(plane)

plt.figure(figsize=(12,6))
for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(bit_plane[i],cmap='gray')
    plt.title('bit_plane['+str(i) +']')
    plt.axis('off')
plt.tight_layout()
plt.show()
