import cv2

# Load the image
image = cv2.imread('input.jpg')  # Replace with your image file

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
else:
    # --- Draw Shapes ---
    # Draw a red rectangle (x1, y1) to (x2, y2)
    cv2.rectangle(image, (50, 50), (200, 200), (0, 0, 255), 2)

    # Draw a green circle at center (x, y) with radius
    cv2.circle(image, (300, 150), 40, (0, 255, 0), 2)

    # Draw a blue line from point A to B
    cv2.line(image, (100, 300), (400, 300), (255, 0, 0), 2)

    # --- Add Measurements ---
    # Add text label for rectangle dimensions
    width = 200 - 50
    height = 200 - 50
    cv2.putText(image, f"{width}x{height}px", (50, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Add label near the circle
    cv2.putText(image, "Radius: 40px", (260, 140),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Save and display the annotated image
    cv2.imwrite('annotated_image.jpg', image)
    cv2.imshow('Annotated Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
