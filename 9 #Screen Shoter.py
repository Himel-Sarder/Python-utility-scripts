import pyautogui

def take_screenshot(filename='screenshot.png'):
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    
    # Save the screenshot to a file
    screenshot.save(filename)
    
    print(f"Screenshot saved as {filename}")

# Example usage:
take_screenshot()

