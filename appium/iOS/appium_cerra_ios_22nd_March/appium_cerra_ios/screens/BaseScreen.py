from appium.webdriver.webdriver import WebDriver


class BaseScreen:
    def __init__(self, driver: WebDriver, platform):
        self.driver = driver
        self.platform = platform
        self.locator = None
        self.initialize_locator()

    def initialize_locator(self):
        raise NotImplementedError("Subclasses must implement initialize_locator method")
