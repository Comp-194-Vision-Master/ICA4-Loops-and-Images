

import cv2

image = cv2.imread("SampleImages/landscape1MuchSmaller.jpg")

xPos = 150
yPos = 50

for i in range(15):
    bgChanVal = 16 * i + 10
    cv2.line(image, (xPos, yPos), (xPos + 20, yPos + 100), (bgChanVal, bgChanVal, 0), 3)
    cv2.imshow("Lines", image)
    cv2.waitKey()
    xPos = xPos + 50
    yPos = yPos + 20
