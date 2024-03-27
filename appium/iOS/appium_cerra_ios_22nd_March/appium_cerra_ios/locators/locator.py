from abc import ABC, abstractmethod

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver


class Locator(ABC):
    @abstractmethod
    def __init__(self, driver: WebDriver):
        pass

    @abstractmethod
    def get_element(self) -> WebElement:
        pass
