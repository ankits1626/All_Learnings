from appium.webdriver.common.appiumby import AppiumBy


class RewardListingCellLocators:
    iOS = {
        "all_reward_category_titles": (AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionTitle"),
        "all_rewards_in_category_rows": (AppiumBy.ACCESSIBILITY_ID, "rewardCollectionRewardTitle"),
    }

    android = {
        "all_reward_category_titles": (AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionTitle"),
    }
