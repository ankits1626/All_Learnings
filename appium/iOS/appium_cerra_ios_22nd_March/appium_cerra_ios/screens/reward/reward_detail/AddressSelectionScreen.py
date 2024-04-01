from locators.reward.reward_detail.address_selection_locators import AddressSelectionLocators
from screens.BaseScreen import BaseScreen
from screens.reward.reward_detail.RedeemConfirmationScreen import RedeemConfirmationScreen


class AddressSelectionScreen(BaseScreen):
    def initialize_locator(self):
        self.locator = AddressSelectionLocators(self.platform)

    def select_address(self):
        address_row_locator = self.locator.get_locator('address_rows')
        address_cell = self.driver.find_elements(*address_row_locator)[0]
        address_cell.click()
        select_button_locator = self.locator.get_locator('select_address_button')
        select_button = self.driver.find_element(*select_button_locator)
        select_button.click()
        return RedeemConfirmationScreen(self.driver, self.platform)
