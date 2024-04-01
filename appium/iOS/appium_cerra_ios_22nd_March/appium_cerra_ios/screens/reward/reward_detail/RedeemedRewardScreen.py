from locators.reward.reward_detail.redeemed_reward_locators import RedeemedRewardLocators
from screens.BaseScreen import BaseScreen


class RedeemedRewardScreen(BaseScreen):
    def initialize_locator(self):
        self.locator = RedeemedRewardLocators(self.platform)

    def get_redeemed_reward_name(self):
        redeemed_reward_name_locator = self.locator.get_locator('redeemed_reward_name')
        return self.driver.find_element(*redeemed_reward_name_locator).text

    def get_redeemed_reward_status(self):
        status_locator = self.locator.get_locator('redeemed_reward_status')
        return self.driver.find_element(*status_locator).text

    def go_back_to_rewards(self):
        button_locator = self.locator.get_locator('back_to_reward_button')
        return self.driver.find_element(*button_locator).click()
