from locators.reward.reward_listing.reward_in_category_listing_cell_locators import RewardInCategoryListingCellLocators


class RewardInCategoryListingCell:
    def __init__(self, index, cell, platform):
        self.index = index
        self.cell = cell
        self.platform = platform

    def get_reward_title(self):
        all_reward_category_rows = getattr(RewardInCategoryListingCellLocators, self.platform)['reward_title']
        return self.cell.find_element(*all_reward_category_rows).text

