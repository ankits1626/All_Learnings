from appium.webdriver.common.appiumby import AppiumBy

from locators.base_locator import BaseLocator


class RedeemedRewardLocators(BaseLocator):
    def initialize_locators(self):
        if self.platform == 'iOS':
            self.iOS = {
                "redeemed_reward_status": (AppiumBy.ACCESSIBILITY_ID, 'redeemedStatusLabel'),
                "redeemed_reward_name": (AppiumBy.ACCESSIBILITY_ID, 'redeemedRIRewardName'),
                "back_to_reward_button": (AppiumBy.ACCESSIBILITY_ID, "redeemedViewBottomButton"),
            }
        elif self.platform == 'Android':
            self.android = {
                "redeemed_reward_status": (AppiumBy.ID, "com.root.cerrasg:id/tvOrderStatus"),
                "redeemed_reward_name": (AppiumBy.ID, "com.root.cerrasg:id/tvRewardNameRedeem"),
                "back_to_reward_button": (AppiumBy.ID, "com.root.cerrasg:id/btnRedeemReward"),
            }
        else:
            raise ValueError("Invalid platform provided")