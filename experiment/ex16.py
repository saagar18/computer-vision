import cv2

img = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")
img = cv2.resize(img, (413, 531))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
