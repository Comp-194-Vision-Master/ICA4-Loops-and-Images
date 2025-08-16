
import cv2
import numpy as np

image = np.zeros((300, 700, 3), np.uint8)
image[:,:] = (206, 252, 202)
colors = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0), (255, 0, 255)]

# TODO: Add for loop here to draw six circles as described in activity

cv2.imshow("Circles", image)
cv2.waitKey()
