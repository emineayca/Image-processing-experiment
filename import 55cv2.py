import cv2
import numpy as np

image = cv2.imread('resimisleme.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

harris_corners = cv2.cornerHarris(gray, 2, 3, 0.04)

threshold = 0.01 * harris_corners.max()

corner_image = np.copy(image)
corner_image[harris_corners > threshold] = [0, 0, 255]

cv2.imshow('Corner Image', corner_image)

bottom_three_rows = image[-3:]

bottom_three_rows_copy = np.copy(image[-3:])
cv2.waitKey(0)
cv2.destroyAllWindows()