from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from locators.locator import Locator


class IosLocator(Locator):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element(self) -> WebElement:
        pass

