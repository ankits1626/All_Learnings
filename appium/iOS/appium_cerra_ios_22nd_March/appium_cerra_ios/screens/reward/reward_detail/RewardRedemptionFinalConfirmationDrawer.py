from locators.reward.reward_detail.reward_redemption_final_confirmation_drawer_locators import \
    RewardRedemptionFinalConfirmationDrawerLocators
from screens.BaseScreen import BaseScreen
from screens.reward.reward_detail.RedeemedRewardScreen import RedeemedRewardScreen


class RewardRedemptionFinalConfirmationDrawer(BaseScreen):
    def initialize_locator(self):
        self.locator = RewardRedemptionFinalConfirmationDrawerLocators(self.platform)

    def get_reward_name(self):
        reward_name_locator = self.locator.get_locator('reward_name')
        return self.driver.find_element(*reward_name_locator).text

    def proceed_with_reward_redemption(self):
        proceed_button_locator = self.locator.get_locator('proceed_button')
        self.driver.find_element(*proceed_button_locator).click()
        return RedeemedRewardScreen(self.driver, self.platform)
