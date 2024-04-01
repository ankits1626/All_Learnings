import pytest
from appium.webdriver.common.appiumby import AppiumBy

from screens.MainTabBar import MainTabBar
from utility.dataUtil import extract_number_from_string, get_formatted_number


# @pytest.mark.highlight_on_failure(element_id="rewardzContainerUserPointsLabel")
# def test_remaining_points_on_rewards_listing_screen(logger, datasource, target_driver, screenshot_on_failure):
#     platform = target_driver.capabilities['platformName']
#     logger.info(f'{platform}: executing : test_remaining_points_on_rewards_listing_screen')
#
#     # navigate to reward tab
#     main_tab_bar = MainTabBar(target_driver, platform)
#     reward_listing_screen = main_tab_bar.navigate_to_reward_tab()
#     label_text = reward_listing_screen.get_reward_remaining_points()
#     extracted_remaining_points = extract_number_from_string(label_text)
#
#     # fetch data from api
#     dashboard_data = datasource.get_dashboard_data()
#     remaining_points = dashboard_data.get("remaining_points")
#
#     logger.info(
#         f" rewards listing screen: available points = {label_text} "
#         f"extracted_remaining_points = {extracted_remaining_points} remaining_points = {remaining_points}")
#     assert remaining_points == extracted_remaining_points, \
#         f"Expected points '{extracted_remaining_points}'  = '{remaining_points}'"
#
#     is_decimal_support_in_transaction_enabled = dashboard_data.get("is_decimal_support_in_transaction_enabled")
#     formatted_remaining_points = get_formatted_number(is_decimal_support_in_transaction_enabled, remaining_points)
#     logger.info(
#         f" rewards listing screen: available points = {label_text} "
#         f"extracted_remaining_points = {extracted_remaining_points} "
#         f"formatted_remaining_points = {formatted_remaining_points}")
#     assert formatted_remaining_points in label_text, f"Expected points '{formatted_remaining_points} in {label_text}'"
#     main_tab_bar.navigate_to_home_tab()


# def test_all_reward_category_properly_displayed(logger, datasource, target_driver, screenshot_on_failure):
#     platform = target_driver.capabilities['platformName']
#     logger.info(f'{platform}: executing : test_all_reward_category_properly_displayed')
#
#     # navigate to reward tab
#     main_tab_bar = MainTabBar(target_driver, platform)
#     reward_listing_screen = main_tab_bar.navigate_to_reward_tab()
#     all_reward_category_rows = reward_listing_screen.get_all_reward_category_rows()
#
#     # verify category count
#     reward_categories = datasource.get_rewards_categories_data()
#     assert len(reward_categories) == len(all_reward_category_rows), \
#         f"number of rows in UI i.e {len(all_reward_category_rows)} == number of categories i.e {len(reward_categories)}"
#
#     # verify each row
#     for row in all_reward_category_rows:
#         label_text = row.get_category_title()
#         category_name = reward_categories[row.index].name
#         logger.info(f'title = {label_text} --- category_name={category_name}')
#         assert label_text == category_name, f'title = {label_text} --- category_name={category_name} should be same'
#
#         # # verify reward in each row
#         # rewards_in_category = reward_categories[row.index].rewards
#         # assert len(rewards_in_category) == len(row.get_rewards()), \
#         #     (f"number of reward in UI i.e {len(row.get_rewards())} == number of rewards in category i.e "
#         #      f"{len(rewards_in_category)} category = {category_name} rewards "
#         #      f"in category = {reward_categories[row.index].rewards}")
#         # for reward_cell in row.get_rewards():
#         #     reward_label_text = reward_cell.get_reward_title()
#         #     logger.info(f'reward title = {rewards_in_category[reward_cell.index].name} --- '
#         #           f'reward_label_text={reward_label_text}')
#         #     assert reward_label_text == rewards_in_category[reward_cell.index].name, \
#         #         (f'reward title in ui = {reward_label_text} --- '
#         #          f'reward title ={rewards_in_category[reward_cell.index].name} should be same')
#
#     main_tab_bar.navigate_to_home_tab()
