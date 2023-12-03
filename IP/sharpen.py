import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('images/lion.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Laplacian filter for edge detection
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

# Convert the Laplacian result to the same data type as the original image
laplacian = np.uint8(np.abs(laplacian))

# Add the Laplacian result back to the original image to sharpen it
sharpened_image = cv2.addWeighted(gray_image, 1.5, laplacian, -0.5, 0)

# Display the original and sharpened images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Image')
plt.axis('off')

plt.tight_layout()
plt.show()
