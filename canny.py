import cv2
img=cv2.imread('images/cat.jpeg')
lower = 50
upper = 50
edge = cv2.Canny(img,lower,upper)
cv2.imshow('original',img)
cv2.imshow('edge',edge)
cv2.waitKey(0)