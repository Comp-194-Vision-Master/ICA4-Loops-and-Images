

import cv2
import numpy as np

squareImg = np.zeros((500, 500, 3), np.uint8)

squareImg[:,:] = (220, 240, 245)

squareSizes = [10, 20, 50, 55, 60, 70, 100]
# TODO: Add a for loop here

cv2.imshow("Squares", squareImg)
cv2.waitKey()
