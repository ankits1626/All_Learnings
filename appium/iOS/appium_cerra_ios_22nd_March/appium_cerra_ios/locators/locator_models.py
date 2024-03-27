from appium.webdriver import WebElement


class LocatorModel:
    def __init__(self, target, locator_id, driver):
        self.target = target
        self.locator_id = locator_id
        self.driver = driver

    def get_element(self) -> WebElement:
        pass
