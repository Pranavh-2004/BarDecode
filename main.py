import cv2
from pyzbar.pyzbar import decode

def read_barcode_from_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return

    # Decode barcodes
    barcodes = decode(img)

    if not barcodes:
        print("No barcodes detected.")
    else:
        for barcode in barcodes:
            # Extract data
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            print(f"Decoded Barcode: {barcode_data} (Type: {barcode_type})")

            # Draw a rectangle around the barcode for easier identification
            x, y, w, h = barcode.rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image
    cv2.imshow('Barcode reader', img)

    # Wait for 'q' to exit and close window
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break

    # Clean up
    cv2.destroyAllWindows()

def read_barcode_from_camera():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Decode barcodes
        barcodes = decode(frame)

        for barcode in barcodes:
            # Extract data
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            print(f"Decoded Barcode: {barcode_data} (Type: {barcode_type})")

            # Draw a rectangle around the barcode for easier identification
            x, y, w, h = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Barcode reader', frame)

        # Exit by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Uncomment one of the functions to use

# For reading from an image
read_barcode_from_image('images/barcode_test.png')  
# For reading from the camera
#read_barcode_from_camera()  