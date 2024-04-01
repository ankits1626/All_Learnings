from appium.webdriver.common.appiumby import AppiumBy

from locators.base_locator import BaseLocator


class MainTabLocators(BaseLocator):

    def initialize_locators(self):
        if self.platform == 'iOS':
            self.iOS = {
                "home": (AppiumBy.ACCESSIBILITY_ID, "mainTabBousHome"),
                "feeds": (AppiumBy.ACCESSIBILITY_ID, "mainTabFeed"),
                "reward": (AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz"),
                "history": (AppiumBy.ACCESSIBILITY_ID, "mainTabHistory"),
                "more": (AppiumBy.ACCESSIBILITY_ID, "mainTabMore")
            }
        elif self.platform == 'Android':
            self.android = {
                "home": (AppiumBy.ACCESSIBILITY_ID, "Home"),
                "feeds": (AppiumBy.ACCESSIBILITY_ID, "Feeds"),
                "reward": (AppiumBy.ACCESSIBILITY_ID, "Rewards"),
                "history": (AppiumBy.ACCESSIBILITY_ID, "History"),
                "more": (AppiumBy.ACCESSIBILITY_ID, "More Details")
            }
        else:
            raise ValueError("Invalid platform provided")