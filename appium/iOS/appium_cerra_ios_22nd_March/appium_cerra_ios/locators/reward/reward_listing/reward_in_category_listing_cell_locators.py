from appium.webdriver.common.appiumby import AppiumBy


class RewardInCategoryListingCellLocators:
    iOS = {
        "reward_title": (AppiumBy.ACCESSIBILITY_ID, "rewardCollectionRewardTitle"),
    }

    android = {
        "all_reward_category_titles": (AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionTitle"),
    }
