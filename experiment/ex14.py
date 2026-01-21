import cv2
import numpy as np

img = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")
img = cv2.resize(img, (413, 531))

pts1 = np.float32([[0,0],[413,0],[0,531],[413,531]])
pts2 = np.float32([[50,50],[360,30],[40,500],[380,520]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (413, 531))

cv2.imshow("Perspective Transform", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
