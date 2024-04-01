from appium.webdriver.common.appiumby import AppiumBy

from locators.base_locator import BaseLocator


class RewardDetailLocators(BaseLocator):

    def initialize_locators(self):
        if self.platform == 'iOS':
            self.iOS = {
                "reward_title": (AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRewardTitle'),
                "reward_validity": (AppiumBy.ACCESSIBILITY_ID, 'rewardDetailValidityLabel'),
                "tnc_toggle_button": (AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRedeemTNCToggleButton'),
                "tnc_text": (AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRedeemTNCTextView'),
                "redeem_button": (AppiumBy.ACCESSIBILITY_ID, "redeemViewRedeemButton"),
                "redeem_back": (AppiumBy.ACCESSIBILITY_ID, 'rfk newBackButton'),
            }
        elif self.platform == 'Android':
            self.android = {
                "reward_title": (AppiumBy.ID, "com.root.cerrasg:id/tvRewardName"),
                "reward_validity": (AppiumBy.ID, 'com.root.cerrasg:id/tvValidTill'),
                "tnc_toggle_button": (AppiumBy.ID, 'com.root.cerrasg:id/expand_iv'),
                "tnc_text": (AppiumBy.ID, 'com.root.cerrasg:id/textTC'),
                "redeem_button": (AppiumBy.ID, "com.root.cerrasg:id/btnRedeem"),
                "redeem_confirmation_title": (AppiumBy.ID, "com.root.cerrasg:id/tvLblOrderConfirmation"),
                "redeem_confirmation_cancel": (AppiumBy.ID, 'com.root.cerrasg:id/btnCancel'),
                "redeem_back": (
                    AppiumBy.XPATH,
                    "//android.widget.LinearLayout[@resource-id=\"com.root.cerrasg:id/back\"]/android.widget.ImageView"
                ),
            }
        else:
            raise ValueError("Invalid platform provided")