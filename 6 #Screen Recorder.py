import cv2
import pyautogui

# Get screen width and height
screen_width, screen_height = pyautogui.size()

# Set output video filename and codec
output_filename = 'screen_record.avi'
codec = cv2.VideoWriter_fourcc(*"XVID")

# Set frames per second (FPS)
fps = 24.0

# Create video writer object
out = cv2.VideoWriter(output_filename, codec, fps, (screen_width, screen_height))

try:
    while True:
        # Capture the screen
        screenshot = pyautogui.screenshot()
        
        # Convert the screenshot to numpy array
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Write the frame to the output video
        out.write(frame)
        
        # Display the recording in real-time (optional)
        cv2.imshow("Screen Recorder", frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
            break

finally:
    # Release the video writer and close OpenCV windows
    out.release()
    cv2.destroyAllWindows()
