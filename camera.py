import cv2
import requests
import base64
import time

# Function to encode image to Base64
def encode_image_to_base64(image):
    _, buffer = cv2.imencode('.jpg', image)
    encoded_image = base64.b64encode(buffer).decode('utf-8')
    return encoded_image

def capture_and_send_image(cap, url):
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        return

    # Resize the frame to 50x50
    resized_frame = cv2.resize(frame, (50, 50))

    # Encode the resized image to Base64
    encoded_image_data = encode_image_to_base64(resized_frame)

    # Parameters to send in the POST request
    data = {
        'image': encoded_image_data,
        'w': 50,  # width
        'h': 50   # height
    }

    # Measure the time to send the request and get the response
    start_time = time.time()

    response = requests.post(url, data=data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Response from server:")
    print(response.text)
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

    # Display the resized frame
    cv2.imshow('Camera', resized_frame)

def main():
    url = 'http://192.168.137.217:8000/recog'

    # Open the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press the spacebar to capture an image.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame
        cv2.imshow('Camera', frame)

        # Wait for the spacebar key press to capture the image
        if cv2.waitKey(1) & 0xFF == ord(' '):
            print("Image captured.")
            capture_and_send_image(cap, url)

        # Close the application when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting the application.")
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
