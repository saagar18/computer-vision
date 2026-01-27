import cv2
import numpy as np

img = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")
img = cv2.resize(img, (413, 531))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(gray, kernel)
dilation = cv2.dilate(gray, kernel)
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Top Hat", tophat)
cv2.imshow("Black Hat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
