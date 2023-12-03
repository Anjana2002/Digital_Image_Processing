#program to perform basic arithmetic operation and logical operation on images
import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread('images/lion.jpeg')
image2 = cv2.imread('images/zebra.jpeg')
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Basic Arithmetic Operations
addition_result = cv2.add(image1, image2)
subtraction_result = cv2.subtract(image1, image2)
multiplication_result = cv2.multiply(image1, image2)
division_result = cv2.divide(image1, image2)

# Logical Operations
# Convert images to grayscale for logical operations
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Logical AND, OR, XOR, NOT
logical_and_result = cv2.bitwise_and(gray_image1, gray_image2)
logical_or_result = cv2.bitwise_or(gray_image1, gray_image2)
logical_xor_result = cv2.bitwise_xor(gray_image1, gray_image2)
logical_not_result1 = cv2.bitwise_not(gray_image1)
logical_not_result2 = cv2.bitwise_not(gray_image2)

plt.figure(figsize=(12, 8))

# Display images using subplots
plt.subplot(3, 3, 1)
plt.imshow(cv2.cvtColor(addition_result, cv2.COLOR_BGR2RGB))
plt.title('Addition Result')
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(cv2.cvtColor(subtraction_result, cv2.COLOR_BGR2RGB))
plt.title('Subtraction Result')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.imshow(cv2.cvtColor(multiplication_result, cv2.COLOR_BGR2RGB))
plt.title('Multiplication Result')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.imshow(cv2.cvtColor(division_result, cv2.COLOR_BGR2RGB))
plt.title('Division Result')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.imshow(logical_and_result, cmap='gray')
plt.title('Logical AND Result')
plt.axis('off')

plt.subplot(3, 3, 6)
plt.imshow(logical_xor_result, cmap='gray')
plt.title('Logical XOR Result')
plt.axis('off')

plt.subplot(3, 3, 7)
plt.imshow(logical_or_result, cmap='gray')
plt.title('Logical OR Result')
plt.axis('off')

plt.subplot(3, 3, 8)
plt.imshow(logical_not_result1, cmap='gray')
plt.title('Logical NOT Result (Image 1)')
plt.axis('off')

plt.subplot(3, 3, 9)
plt.imshow(logical_not_result2, cmap='gray')
plt.title('Logical NOT Result (Image 2)')
plt.axis('off')

plt.tight_layout()
plt.show()
