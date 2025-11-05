import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')  # Replace with your image file
if image is None:
    print("Error: Image not found.")
    exit()

# Resize for display
image = cv2.resize(image, (600, 400))

# Create a window
cv2.namedWindow('Edge Detection')

# Trackbar callback (does nothing but required)
def nothing(x):
    pass

# Create trackbars
cv2.createTrackbar('Lower Threshold', 'Edge Detection', 50, 255, nothing)
cv2.createTrackbar('Upper Threshold', 'Edge Detection', 150, 255, nothing)
cv2.createTrackbar('Blur Kernel', 'Edge Detection', 1, 20, nothing)

while True:
    # Get current positions of trackbars
    low = cv2.getTrackbarPos('Lower Threshold', 'Edge Detection')
    high = cv2.getTrackbarPos('Upper Threshold', 'Edge Detection')
    k = cv2.getTrackbarPos('Blur Kernel', 'Edge Detection')
    k = k if k % 2 == 1 else k + 1  # Ensure kernel size is odd

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(image, (k, k), 0)

    # Convert to grayscale
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, low, high)

    # Stack original and edge images side by side
    stacked = np.hstack((gray, edges))

    # Show the result
    cv2.imshow('Edge Detection', stacked)

    # Break on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
