from appium.webdriver.webdriver import WebDriver


class DashboardScreen:
    def __init__(self, driver: WebDriver, platform):
        self.driver = driver
        self.platform = platform
