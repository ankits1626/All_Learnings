from typing import List

from locators.reward.reward_listing.reward_listing_cell_locators import RewardListingCellLocators
from screens.reward.reward_lisiting.RewardInCategoryListingCell import RewardInCategoryListingCell


class RewardListingCell:
    def __init__(self, index, cell, platform):
        self.index = index
        self.cell = cell
        self.platform = platform

    def get_category_title(self):
        all_reward_category_rows = getattr(RewardListingCellLocators, self.platform)['all_reward_category_titles']
        return self.cell.find_element(*all_reward_category_rows).text

    def get_rewards(self) -> List[RewardInCategoryListingCell]:
        retval: List[RewardInCategoryListingCell] = []
        all_rewards_in_category_rows = getattr(RewardListingCellLocators, self.platform)['all_rewards_in_category_rows']
        rewards = self.cell.find_elements(*all_rewards_in_category_rows)
        for index, reward_cell in enumerate(rewards):
            retval.append(RewardInCategoryListingCell(index, reward_cell, self.platform))
        return retval

