import cv2

img = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")
img = cv2.resize(img, (413, 531))

rot90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rot180 = cv2.rotate(img, cv2.ROTATE_180)
rot270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("90 Degree", rot90)
cv2.imshow("180 Degree", rot180)
cv2.imshow("270 Degree", rot270)

cv2.waitKey(0)
cv2.destroyAllWindows()
