import cv2
import numpy as np

# Read image
image = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")

# Resize to passport size
image = cv2.resize(image, (413, 531))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Dilation
dilated_image = cv2.dilate(gray, kernel, iterations=1)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
