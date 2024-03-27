from enum import Enum

from appium.webdriver.webdriver import WebDriver

from locators.locator import Locator
from screens.RewardListingScreen import RewardListingScreen


class MainTabType(Enum):
    Home = 'home'
    Feeds = 'feeds'
    Reward = 'reward'
    History = 'history'
    More = 'more'


class MainTab:
    def __init__(self, driver: WebDriver, locator: Locator):
        self.driver = driver
        self.locator = locator

    def navigate_to_rewards(self):
        reward_tab = self.locator.get_element()
        return RewardListingScreen(self.driver)
