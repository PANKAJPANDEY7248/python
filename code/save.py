import cv2

# Load the original image
image = cv2.imread('input.jpg')  # Replace 'input.jpg' with your image file

# Check if image is loaded successfully
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite('grayscale_output.jpg', gray_image)

    # Display both images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
