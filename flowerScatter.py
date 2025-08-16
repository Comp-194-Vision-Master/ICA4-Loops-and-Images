import cv2
import numpy as np
import random

bkgrndImg = cv2.imread("SampleImages/wildColumbine.jpg")

cx = 150
cy = 150
cv2.ellipse(bkgrndImg, (cx + 15, cy), (25, 16), 0, 0, 360, (252, 202, 252), -1)
cv2.ellipse(bkgrndImg, (cx, cy + 15), (25, 16), 90, 0, 360, (252, 170, 252), -1)
cv2.ellipse(bkgrndImg, (cx - 15, cy), (25, 16), 0, 0, 360, (252, 202, 252), -1)
cv2.ellipse(bkgrndImg, (cx, cy - 15), (25, 16), -90, 0, 360, (252, 170, 252), -1)
cv2.circle(bkgrndImg, (cx, cy), 15, (114, 236, 242), -1)

cv2.imshow("flowers", bkgrndImg)
cv2.waitKey()
