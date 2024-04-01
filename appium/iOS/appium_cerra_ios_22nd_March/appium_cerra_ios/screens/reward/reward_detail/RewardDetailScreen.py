from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from locators.reward.reward_detail.reward_detail_locators import RewardDetailLocators
from screens.BaseScreen import BaseScreen
from screens.reward.reward_detail.AddressSelectionScreen import AddressSelectionScreen
from screens.reward.reward_detail.RedeemConfirmationScreen import RedeemConfirmationScreen


class RewardDetailScreen(BaseScreen):
    def initialize_locator(self):
        self.locator = RewardDetailLocators(self.platform)

    def get_reward_title(self):
        title_locator = self.locator.get_locator('reward_title')
        return self.driver.find_element(*title_locator).text

    def get_reward_validity(self):
        validity_locator = self.locator.get_locator('reward_validity')
        return self.driver.find_element(*validity_locator).text.rstrip(
            '\n')

    def get_reward_redemption_tnc(self):
        tnc_toggle_button_locator = self.locator.get_locator('tnc_toggle_button')
        tnc_toggle_button = self.driver.find_element(*tnc_toggle_button_locator)
        tnc_toggle_button.click()
        tnc_text_locator = self.locator.get_locator('tnc_text')
        return self.driver.find_element(*tnc_text_locator).text

    def redeem_reward(self):
        redeem_button_locator = self.locator.get_locator('redeem_button')
        redeem_button = self.driver.find_element(*redeem_button_locator)
        redeem_button.click()

    def redeem_physical_reward(self):
        self.redeem_reward()
        return AddressSelectionScreen(self.driver, self.platform)

    def open_redeem_confirmation_drawer(self):
        self.redeem_reward()
        return RedeemConfirmationScreen(self.driver, self.platform)

    def close_reward_detail_screen(self):
        redeem_back_locator = self.locator.get_locator('redeem_back')
        self.driver.find_element(*redeem_back_locator).click()
