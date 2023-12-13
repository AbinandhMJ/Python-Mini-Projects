import pyautogui
import time

def take_screenshot(output_filename='screenshot.png'):
    # Sleep for a moment to allow time for changing to the desired window or position
    time.sleep(1)

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Show Screenshot
    screenshot.show()

    # Save the screenshot to a file
    screenshot.save(output_filename)
    print(f'Screenshot saved as {output_filename}')

if __name__ == "__main__":
    take_screenshot()