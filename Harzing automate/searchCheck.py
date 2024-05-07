import time
import pyautogui # type: ignore
def wait_for_color(x, y, target_color, timeout=500):
    """Waits until the pixel at (x, y) matches the target_color or the timeout is reached."""
    start_time = time.time()
    while True:
        if pyautogui.pixel(x, y) == target_color:
            print("Target color detected at the specified pixel.")
            break
        elif time.time() - start_time > timeout:
            print("Timeout reached without detecting the target color.")
            break
        time.sleep(1)
