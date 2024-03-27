import pytest
from appium.webdriver.common.appiumby import AppiumBy

from utility.dataUtil import extract_number_from_string, get_formatted_number


@pytest.mark.highlight_on_failure(element_id="rewardzContainerUserPointsLabel")
def test_remaining_points_on_rewards_listing_screen(logger, datasource, target_driver, screenshot_on_failure):
    logger.info('executing : test_remaining_points_on_rewards_listing_screen')
    el1 = target_driver.find_element() #target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
    el1.click()

    dashboard_data = datasource.get_dashboard_data()
    remaining_points = dashboard_data.get("remaining_points")

    el2 = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "rewardzContainerUserPointsLabel")
    # Get the text from the label
    label_text = el2.text
    extracted_remaining_points = extract_number_from_string(label_text)
    logger.info(
        f" rewards listing screen: available points = {label_text} "
        f"extracted_remaining_points = {extracted_remaining_points} remaining_points = {remaining_points}")
    assert remaining_points == extracted_remaining_points, \
        f"Expected points '{extracted_remaining_points}'  = '{remaining_points}'"

    is_decimal_support_in_transaction_enabled = dashboard_data.get("is_decimal_support_in_transaction_enabled")
    formatted_remaining_points = get_formatted_number(is_decimal_support_in_transaction_enabled, remaining_points)
    logger.info(
        f" rewards listing screen: available points = {label_text} "
        f"extracted_remaining_points = {extracted_remaining_points} "
        f"formatted_remaining_points = {formatted_remaining_points}")
    assert formatted_remaining_points in label_text, f"Expected points '{formatted_remaining_points} in {label_text}'"


# def test_all_reward_category_properly_displayed(logger, datasource, target_driver, screenshot_on_failure):
#     el1 = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
#     el1.click()
#
#     # verify category count
#     reward_categories = datasource.get_rewards_categories_data()
#     all_reward_category_rows = target_driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionCell")
#     assert len(reward_categories) == len(all_reward_category_rows), \
#         f"number of rows in UI i.e {len(all_reward_category_rows)} == number of categories i.e {len(reward_categories)}"
#
#     # verify each row
#     for index, cell in enumerate(all_reward_category_rows):
#         label_text = cell.find_element(AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionTitle").text
#         category_name = reward_categories[index].name
#         print(f'title = {label_text} --- category_name={category_name}')
#         assert label_text == category_name, f'title = {label_text} --- category_name={category_name} should be same'
#
#         # verify reward in each row
#         rewards = reward_categories[index].rewards
#         reward_titles = cell.find_elements(AppiumBy.ACCESSIBILITY_ID, "rewardCollectionRewardTitle")
#         assert len(rewards) == len(reward_titles), \
#             (f"number of reward in UI i.e {len(reward_titles)} == number of rewards in category i.e {len(rewards)} "
#              f"category = {category_name} rewards in category = {reward_categories[index].rewards}")
#         for reward_index, reward_title in enumerate(reward_titles):
#             reward_label_text = reward_title.text
#             print(f'reward title = {rewards[reward_index].name} --- reward_label_text={reward_label_text}')
#             assert reward_label_text == rewards[reward_index].name, \
#                 (f'reward title in ui = {reward_label_text} --- reward title ={rewards[reward_index].name} should be '
#                  f'same')
