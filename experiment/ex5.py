import cv2
import matplotlib.pyplot as plt

def analyze_histogram():
    # Default remembered image path
    image_path = r"/Users/saagar/Downloads/computer vision/cvsample.jpg"

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Passport size (India) – 413 × 531 pixels
    passport_width = 413
    passport_height = 531

    # Resize image
    image = cv2.resize(image, (passport_width, passport_height))

    color_channels = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))

    for i, color in enumerate(color_channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f"{color.upper()} Channel")

    plt.xlim([0, 256])
    plt.title("Passport Size Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

# Call function
analyze_histogram()
