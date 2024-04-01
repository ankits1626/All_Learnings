from appium.webdriver.common.appiumby import AppiumBy

from locators.base_locator import BaseLocator


class AddressSelectionLocators(BaseLocator):
    def initialize_locators(self):
        if self.platform == 'iOS':
            self.iOS = {
                "address_rows": (AppiumBy.ACCESSIBILITY_ID, "selectAddressCell"),
                "select_address_button": (AppiumBy.ACCESSIBILITY_ID, "selectAddressButton"),

            }
        elif self.platform == 'Android':
            self.android = {
                "address_rows": (AppiumBy.ID, "com.root.cerrasg:id/address_cv"),
                "select_address_button": (AppiumBy.ID, "com.root.cerrasg:id/btnProceed"),
            }
        else:
            raise ValueError("Invalid platform provided")