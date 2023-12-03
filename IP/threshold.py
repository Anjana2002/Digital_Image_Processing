#Apply global or adaptive thresholding to segment an image.
import cv2

# Read an image
image = cv2.imread('images/lion.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply global thresholding
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
