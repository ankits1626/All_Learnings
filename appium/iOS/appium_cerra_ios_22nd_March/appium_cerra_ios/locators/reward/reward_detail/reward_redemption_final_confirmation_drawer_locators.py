from appium.webdriver.common.appiumby import AppiumBy

from locators.base_locator import BaseLocator


class RewardRedemptionFinalConfirmationDrawerLocators(BaseLocator):
    def initialize_locators(self):
        if self.platform == 'iOS':
            self.iOS = {
                "reward_name": (AppiumBy.ACCESSIBILITY_ID, "physical product demo3"),
                "available_points": (AppiumBy.ACCESSIBILITY_ID, "redeemBottomDrawerAvailablePoints"),
                "points_required": (AppiumBy.ACCESSIBILITY_ID, "redeemBottomDrawerPointsRequired"),
                "delivery_fee_in_points": (AppiumBy.ACCESSIBILITY_ID, "redeemBottomDrawerDeliveryFee"),
                "proceed_button": (AppiumBy.ACCESSIBILITY_ID, "redeemBottomDrawerProceedButton"),

            }
        elif self.platform == 'Android':
            self.android = {
                "reward_name": (AppiumBy.ID, "com.root.cerrasg:id/tvRedeemRewardName"),
                "available_points": (AppiumBy.ID, "com.root.cerrasg:id/tvAvailablePoints"),
                "points_required": (AppiumBy.ID, "com.root.cerrasg:id/tvPointsRequired"),
                "delivery_fee_in_points": (AppiumBy.ID, "com.root.cerrasg:id/tvDeliveryFeeInPoints"),
                "proceed_button": (AppiumBy.ID, "com.root.cerrasg:id/btnProceed"),
            }
        else:
            raise ValueError("Invalid platform provided")
