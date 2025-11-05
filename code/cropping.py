import cv2

# Load the image
image = cv2.imread('input.jpg')  # Replace with your image file

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
else:
    # --- Color Conversions ---
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Save converted images
    cv2.imwrite('gray.jpg', gray)
    cv2.imwrite('hsv.jpg', hsv)
    cv2.imwrite('lab.jpg', lab)

    # --- Cropping ---
    # Define crop region (x1, y1) to (x2, y2)
    x1, y1 = 100, 100
    x2, y2 = 300, 300
    cropped = image[y1:y2, x1:x2]

    # Save and display cropped image
    cv2.imwrite('cropped.jpg', cropped)
    cv2.imshow('Cropped Image', cropped)

    # Display all converted images
    cv2.imshow('Original', image)
    cv2.imshow('Grayscale', gray)
    cv2.imshow('HSV', hsv)
    cv2.imshow('LAB', lab)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
