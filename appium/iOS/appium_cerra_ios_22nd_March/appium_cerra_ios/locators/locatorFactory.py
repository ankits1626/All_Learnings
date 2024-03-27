from appium.webdriver.webdriver import WebDriver

from locators.android import AndroidLocator
from locators.ios import IosLocator
from locators.locator import Locator


class LocatorFactory:
    @staticmethod
    def create_locator(target, driver: WebDriver) -> Locator:
        if target == 'ios':
            return IosLocator()
        elif target == 'android':
            return AndroidLocator()
        else:
            raise ValueError(f"Invalid target: {target}")
