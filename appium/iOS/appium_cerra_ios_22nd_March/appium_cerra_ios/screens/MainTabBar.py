from locators.main_tab_locators import MainTabLocators
from screens.BaseScreen import BaseScreen
from screens.DashboardScreen import DashboardScreen
from screens.reward.reward_lisiting.RewardListingScreen import RewardListingScreen


class MainTabBar(BaseScreen):
    def initialize_locator(self):
        self.locator = MainTabLocators(self.platform)

    def navigate_to_reward_tab(self):
        reward_tab_locator = self.locator.get_locator('reward')
        el1 = self.driver.find_element(*reward_tab_locator)
        el1.click()
        return RewardListingScreen(self.driver, self.platform)

    def navigate_to_home_tab(self):
        home_tab_locator = self.locator.get_locator('home')
        el1 = self.driver.find_element(*home_tab_locator)  # (AppiumBy.ACCESSIBILITY_ID, "Rewards")
        el1.click()
        return DashboardScreen(self.driver, self.platform)
