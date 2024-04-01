from appium.webdriver.common.appiumby import AppiumBy

from locators.base_locator import BaseLocator


class RewardListingLocators(BaseLocator):
    def load_param(self, param):
        self.param = param
        self.initialize_locators()

    def initialize_locators(self):
        if self.platform == 'iOS':
            self.iOS = {
                "remaining_points_label": (AppiumBy.ACCESSIBILITY_ID, "rewardzContainerUserPointsLabel"),
                "all_reward_category_rows": (AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionCell"),
                "navigate_to_reward": (
                    AppiumBy.XPATH,
                    f"//XCUIElementTypeStaticText[@name=\"rewardCollectionRewardTitle\" "
                    f"and @label=\"{self.param}\"]"
                ) if self.param else None
            }
        elif self.platform == 'Android':
            self.android = {
                "remaining_points_label": (AppiumBy.ID, "com.root.cerrasg:id/tvLblSpecialRewards"),
                "all_reward_category_rows": (AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionCell"),
                "reward_list": (
                    AppiumBy.XPATH,
                    "(//androidx.recyclerview.widget.RecyclerView"
                    "[@resource-id=\"com.root.cerrasg:id/rvBrowseAllRewards\"])[1]"
                ),
                "navigate_to_reward": (
                    AppiumBy.XPATH,
                    f"//android.widget.TextView[@resource-id=\"com.root.cerrasg:id/tvRewardName\" "
                    f"and @text=\"{self.param}\"]"
                ) if self.param else None
            }
        else:
            raise ValueError("Invalid platform provided")
