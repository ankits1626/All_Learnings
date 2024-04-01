from appium.webdriver.common.appiumby import AppiumBy

from locators.base_locator import BaseLocator


class RedeemConfirmationScreenLocators(BaseLocator):
    def initialize_locators(self):
        if self.platform == 'iOS':
            self.iOS = {
                "redeem_confirmation_title": (AppiumBy.ACCESSIBILITY_ID, "redeemConfirmationDrawerRewardName"),
                "redeem_button": (AppiumBy.ACCESSIBILITY_ID, "redeemConfirmationDrawerRedeemButton"),
                "redeem_confirmation_cancel": (AppiumBy.ACCESSIBILITY_ID, 'redeemConfirmationDrawerCancelButton'),

            }
        elif self.platform == 'Android':
            self.android = {
                "redeem_confirmation_title": (AppiumBy.ID, "com.root.cerrasg:id/tvOrderName"),
                "redeem_button": (AppiumBy.ID, 'com.root.cerrasg:id/btnPlaceYourOrder'),
                "redeem_confirmation_cancel": (AppiumBy.ID, 'com.root.cerrasg:id/btnCancel'),
            }
        else:
            raise ValueError("Invalid platform provided")
