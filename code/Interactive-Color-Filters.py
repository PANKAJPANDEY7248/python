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
cv2.namedWindow('Color Filter')

# Trackbar callback (does nothing but required)
def nothing(x):
    pass

# Create trackbars for R, G, B
cv2.createTrackbar('R', 'Color Filter', 100, 255, nothing)
cv2.createTrackbar('G', 'Color Filter', 100, 255, nothing)
cv2.createTrackbar('B', 'Color Filter', 100, 255, nothing)

while True:
    # Get current trackbar positions
    r = cv2.getTrackbarPos('R', 'Color Filter')
    g = cv2.getTrackbarPos('G', 'Color Filter')
    b = cv2.getTrackbarPos('B', 'Color Filter')

    # Create a filter matrix
    filter_matrix = np.zeros_like(image)
    filter_matrix[:, :, 0] = b
    filter_matrix[:, :, 1] = g
    filter_matrix[:, :, 2] = r

    # Blend original image with filter
    filtered = cv2.addWeighted(image, 0.5, filter_matrix, 0.5, 0)

    # Show the result
    cv2.imshow('Color Filter', filtered)

    # Break on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
