import cv2

img = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")
img = cv2.resize(img, (413, 531))

roi = img[100:250, 100:250]
img[300:450, 150:300] = roi

cv2.imshow("ROI Operation", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
