# Display Bit Planes of an Image
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('images/lion.jpeg',0)

bit_plane=[]
for i in range(8):
    planes = np.zeros_like(img, dtype=np.uint8)
    planes[img & (1<<i)!=0]=255
    bit_plane.append(planes)

plt.figure(figsize=(12,8))
for i in range(8):
    plt.subplot(2,4,i+1)
    plt.title(f'BIT PLANE {i+1}')
    plt.imshow(bit_plane[i],cmap='gray')
plt.tight_layout()
plt.show()
