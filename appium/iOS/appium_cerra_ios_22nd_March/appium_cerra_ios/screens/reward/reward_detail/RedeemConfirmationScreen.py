from locators.reward.reward_detail.redeem_confirmation_screen_locators import RedeemConfirmationScreenLocators
from screens.BaseScreen import BaseScreen
from screens.reward.reward_detail.RewardRedemptionFinalConfirmationDrawer import RewardRedemptionFinalConfirmationDrawer


class RedeemConfirmationScreen(BaseScreen):
    def initialize_locator(self):
        self.locator = RedeemConfirmationScreenLocators(self.platform)

    def get_reward_title(self):
        redeem_confirmation_title_locator = self.locator.get_locator('redeem_confirmation_title')
        redeem_confirmation = self.driver.find_element(*redeem_confirmation_title_locator)
        return redeem_confirmation

    def close_reward_redeem_confirmation_screen(self):
        redeem_confirmation_cancel_locator = self.locator.get_locator('redeem_confirmation_cancel')
        self.driver.find_element(*redeem_confirmation_cancel_locator).click()

    def redeem_reward(self):
        redeem_confirmation_button_locator = self.locator.get_locator('redeem_button')
        self.driver.find_element(*redeem_confirmation_button_locator).click()
        return RewardRedemptionFinalConfirmationDrawer(self.driver, self.platform)
