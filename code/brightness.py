import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')  # Replace with your image file

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
else:
    # --- Rotate Image ---
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Rotate 45 degrees clockwise
    rotation_matrix = cv2.getRotationMatrix2D(center, angle=45, scale=1.0)
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h))

    # --- Adjust Brightness ---
    # Increase brightness by adding a scalar value
    brightness_value = 50  # You can change this value
    brightened = cv2.convertScaleAbs(image, alpha=1.0, beta=brightness_value)

    # Save results
    cv2.imwrite('rotated.jpg', rotated)
    cv2.imwrite('brightened.jpg', brightened)

    # Display results
    cv2.imshow('Original', image)
    cv2.imshow('Rotated', rotated)
    cv2.imshow('Brightened', brightened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
