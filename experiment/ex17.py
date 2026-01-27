import cv2
import numpy as np

# Read original image
img = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")
img = cv2.resize(img, (413, 531))

# Read watermark image
watermark = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg", cv2.IMREAD_UNCHANGED)

# Resize watermark
wm_width = 120
wm_height = 60
watermark = cv2.resize(watermark, (wm_width, wm_height))

# Split watermark channels
if watermark.shape[2] == 4:
    b, g, r, a = cv2.split(watermark)
    alpha = a / 255.0
    watermark_rgb = cv2.merge((b, g, r))
else:
    watermark_rgb = watermark
    alpha = np.ones((wm_height, wm_width))

# Position: bottom-right corner
x = img.shape[1] - wm_width - 10
y = img.shape[0] - wm_height - 10

# Blend watermark with image
for c in range(3):
    img[y:y+wm_height, x:x+wm_width, c] = (
        alpha * watermark_rgb[:, :, c] +
        (1 - alpha) * img[y:y+wm_height, x:x+wm_width, c]
    )

# Display result
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
