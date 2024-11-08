import time

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


CAPTCHA_REGEX_URL_PATTERN = r'url\("(.+?)"\)'


def move_slider_smoothly(
    driver: Chrome | Firefox,
    slider: WebElement,
    target_position: int,
    steps: int = 5,
    delay: float = 0.3,
):
    # Define the number of steps for smoother movement
    step_length = target_position / steps
    pause_duration = delay

    # Perform the action of dragging the slider in smaller steps
    action = ActionChains(driver)
    action.click_and_hold(slider)

    # Move in smaller increments
    for _ in range(steps):
        action.move_by_offset(step_length, 0)
        action.perform()
        time.sleep(pause_duration)

    # Release the slider
    action.release().perform()