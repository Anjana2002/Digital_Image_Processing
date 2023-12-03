import cv2
import matplotlib.pyplot as plt
image = cv2.imread('images/lion.jpeg')

# Apply Gaussian blur
ksize = (5, 5)  # Kernel size (should be odd)
sigmaX = 0      # Standard deviation in the X direction (0 means auto-calculated based on kernel size)
blurred_image = cv2.GaussianBlur(image, ksize, sigmaX)

# Display the original and blurred images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image (Gaussian)')
plt.axis('off')

plt.tight_layout()
plt.show()
