import cv2

image = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")

# Passport size (India) at 300 DPI
passport_width = 413
passport_height = 531

# Resize image
passport_image = cv2.resize(image, (passport_width, passport_height))

# Optional: blur
blurred_image = cv2.GaussianBlur(passport_image, (15, 15), 0)

cv2.imshow("Passport Size Image", passport_image)
cv2.imshow("Blurred Passport Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
