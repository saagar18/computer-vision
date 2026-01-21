import cv2

# Read image
image = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")

# Passport size
passport_image = cv2.resize(image, (413, 531))

# Scale UP (bigger)
bigger_image = cv2.resize(passport_image, None, fx=1.5, fy=1.5)

# Scale DOWN (smaller)
smaller_image = cv2.resize(passport_image, None, fx=0.5, fy=0.5)

# Display
cv2.imshow("Passport Size Image", passport_image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
