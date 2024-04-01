from typing import List

from locators.reward.reward_listing.reward_listing_locators import RewardListingLocators
from screens.BaseScreen import BaseScreen
from screens.reward.reward_detail.RewardDetailScreen import RewardDetailScreen
from screens.reward.reward_lisiting.RewardCategoryListingCell import RewardListingCell


class RewardListingScreen(BaseScreen):

    def initialize_locator(self):
        self.locator = RewardListingLocators(self.platform)

    def get_reward_remaining_points(self):
        remaining_points_label_locator = self.locator.get_locator('remaining_points_label')
        el1 = self.driver.find_element(*remaining_points_label_locator)
        return el1.text

    def get_all_reward_category_rows(self) -> List[RewardListingCell]:
        all_reward_category_rows = self.locator.get_locator('all_reward_category_rows')
        rows = self.driver.find_elements(*all_reward_category_rows)
        retval: List[RewardListingCell] = []
        for index, cell in enumerate(rows):
            retval.append(RewardListingCell(index, cell, self.platform))
        return retval

    def get_all_reward_category_titles(self):
        all_reward_category_rows = self.locator.get_locator('all_reward_category_rows')
        return self.driver.find_elements(*all_reward_category_rows)

    def navigate_to_reward_redemption(self, reward_name):
        try:
            self.locator.load_param(reward_name)
            reward_title_locator = self.locator.get_locator('navigate_to_reward')
            print(f'<<<< reward_title_locator = {reward_title_locator}')
            reward_tile = self.driver.find_element(*reward_title_locator)
            reward_tile.click()
            return RewardDetailScreen(self.driver, self.platform)
        except Exception as e:
            print("An error occurred:", e)
            reward_listing_view_locator = self.locator.get_locator('reward_list')
            reward_listing_view = self.driver.find_element(*reward_listing_view_locator)
            self.driver.execute_script(
                "gesture: swipe",
                {
                    "elementId": reward_listing_view.id,
                    'percentage': 100,
                    'direction': 'up'
                }
            )
            return self.navigate_to_reward_redemption(reward_name)


