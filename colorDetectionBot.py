from PIL import Image
import pytesseract
import cv2
import numpy as np
import time
import pyautogui


def process_screenshot():
    top = 70
    bottom = 86

    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    image = Image.open("screenshot.png")
    image_np = np.array(image)


    # Crop the image to the ROI
    roi = image_np[top:bottom, 180:500]
     # Convert the ROI to BGR format for OpenCV
    roi_bgr = cv2.cvtColor(roi, cv2.COLOR_RGB2BGR)

    # BGR to HSV
    roi_hsv = cv2.cvtColor(roi_bgr, cv2.COLOR_BGR2HSV)

    # Define HSV color ranges for dark red and light red
    lower_dark_red = np.array([0, 50, 50]) 
    upper_dark_red = np.array([10, 255, 255])  
    lower_light_red = np.array([0, 50, 120])  
    upper_light_red = np.array([10, 255, 255]) 

    mask_dark_red = cv2.inRange(roi_hsv, lower_dark_red, upper_dark_red)
    mask_light_red = cv2.inRange(roi_hsv, lower_light_red, upper_light_red)

    # Check if light red is absent
    if cv2.countNonZero(mask_light_red) == 0:
        print("Light red is not present.")
    else:
        print("Light red is present.")

    # Test image display
    cv2.imshow("Processed Image", mask_light_red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    process_screenshot()
    time.sleep(300)  