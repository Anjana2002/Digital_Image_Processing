import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
img = cv2.imread('lion.jpeg')

plt.figure(figsize=(12,8))
#original image
plt.subplot(431)
plt.title('Original image')
plt.imshow(img)
plt.axis('off')

#RGB
plt.subplot(432)
plt.title('BGR to RGB')
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB) )
plt.axis('off')


#resizing image
plt.subplot(433)
plt.title('resize')
resized = cv2.resize(img, (50,50))
plt.imshow(resized)
plt.axis('off')

#rotate by 90 degrees counterclockwise
plt.subplot(434)
plt.title('rotation to 90 degree')
rotated_image = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
plt.imshow(rotated_image)
plt.axis('off')

#again rotation
plt.subplot(435)
plt.title('again rotation to 90 degree')
rotation2 = cv2.rotate(rotated_image,cv2.ROTATE_90_CLOCKWISE)
plt.imshow(rotation2)
plt.axis('off')

#horizonatal flipping
plt.subplot(436)
plt.title('horizontal flipping')
horizontal = cv2.flip(img, 1)
plt.imshow(cv2.cvtColor(horizontal, cv2.COLOR_BGR2RGB))
plt.axis('off')

#vertical flipping
plt.subplot(437)
plt.title('vertical flipping')
vertical = cv2.flip(img, 0)
plt.imshow(cv2.cvtColor(vertical, cv2.COLOR_BGR2RGB))
plt.axis('off')

#BGR to Gray
plt.subplot(438)
plt.title('gray scale')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')
plt.axis('off')

#blur
plt.subplot(439)
plt.title("blur image")
blur_image = cv2.GaussianBlur(img,(15,15),0)
plt.imshow(blur_image)
plt.axis('off')
plt.show()