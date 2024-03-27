import cv2
import numpy as np


def __highlight_element(screenshot, element, driver):
    screenshot_array = np.asarray(bytearray(screenshot), dtype=np.uint8)
    screenshot_image = cv2.imdecode(screenshot_array, cv2.IMREAD_COLOR)

    # Get the location and size of the element
    location = element.location
    size = element.size

    # Translate element coordinates from screen size to screenshot image size
    screenshot_width = screenshot_image.shape[1]
    screenshot_height = screenshot_image.shape[0]
    element_x = int(location['x'] * screenshot_width / driver.get_window_size()['width'])
    element_y = int(location['y'] * screenshot_height / driver.get_window_size()['height'])
    element_width = int(size['width'] * screenshot_width / driver.get_window_size()['width'])
    element_height = int(size['height'] * screenshot_height / driver.get_window_size()['height'])

    # Calculate the coordinates of the element's bounding box
    top_left = (element_x, element_y)
    bottom_right = (element_x + element_width, element_y + element_height)

    # Draw a red rectangle around the element
    cv2.rectangle(screenshot_image, top_left, bottom_right, (0, 0, 255), thickness=2)

    # Convert the annotated image back to bytes
    retval, buffer = cv2.imencode('.png', screenshot_image)
    annotated_screenshot = buffer.tobytes()

    return annotated_screenshot


def take_screenshot_with_element_highlighted(element, driver):
    if element is None:
        driver.get_screenshot_as_png()
    else:
        return __highlight_element(driver.get_screenshot_as_png(), element, driver)
