import logging

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from Utilities import dataProvider
from Utilities.DataUtil import get_formatted_number, extract_number_from_string
from Utilities.LogUtil import Logger
from first.test_setup import setup

log = Logger(__name__, logging.INFO)


def test_remaining_points_on_rewardz_listing_screen(setup, log_test_name, api_client_with_token):
    driver, _ = setup
    log_test_name()
    print(f'test available points on rewardz main screen {driver}')

    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
    el1.click()

    dashboard_data = api_client_with_token.get_dashboard_data()
    remaining_points = dashboard_data.get("remaining_points")

    el2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "rewardzContainerUserPointsLabel")
    # Get the text from the label
    label_text = el2.text
    extracted_remaining_points = extract_number_from_string(label_text)
    log.logger.info(
        f" rewards listing screen: available points = {label_text} "
        f"extracted_remaining_points = {extracted_remaining_points} remaining_points = {remaining_points}")
    assert remaining_points == extracted_remaining_points, \
        f"Expected points '{extracted_remaining_points}'  = '{remaining_points}'"


def test_remaining_points_format_on_rewardz_listing_screen(setup, log_test_name, api_client_with_token):
    driver, _ = setup
    log_test_name()
    print(f'test available points on rewardz main screen {driver}')

    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
    el1.click()

    dashboard_data = api_client_with_token.get_dashboard_data()
    remaining_points = dashboard_data.get("remaining_points")
    is_decimal_support_in_transaction_enabled = dashboard_data.get("is_decimal_support_in_transaction_enabled")
    formatted_remaining_points = get_formatted_number(is_decimal_support_in_transaction_enabled, remaining_points)

    el2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "rewardzContainerUserPointsLabel")
    # Get the text from the label
    label_text = el2.text
    extracted_remaining_points = extract_number_from_string(label_text)
    log.logger.info(
        f" rewards listing screen: available points = {label_text} "
        f"formatted_remaining_points = {formatted_remaining_points}")
    assert formatted_remaining_points in label_text, f"Expected points '{formatted_remaining_points} in {label_text}'"


def test_all_reward_category_properly_displayed(setup, log_test_name, api_client_with_token):
    driver, _ = setup
    log_test_name()

    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
    el1.click()

    # verify category count
    reward_categories = api_client_with_token.get_rewards_categories_data()
    all_reward_category_rows = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionCell")
    assert len(reward_categories) == len(all_reward_category_rows), \
        f"number of rows in UI i.e {len(all_reward_category_rows)} == number of categories i.e {len(reward_categories)}"

    # verify each row
    for index, cell in enumerate(all_reward_category_rows):
        label_text = cell.find_element(AppiumBy.ACCESSIBILITY_ID, "rewardListingRewardCollectionTitle").text
        category_name = reward_categories[index].name
        print(f'title = {label_text} --- category_name={category_name}')
        assert label_text == category_name, f'title = {label_text} --- category_name={category_name} should be same'

        # verify reward in each row
        rewards = reward_categories[index].rewards
        reward_titles = cell.find_elements(AppiumBy.ACCESSIBILITY_ID, "rewardCollectionRewardTitle")
        assert len(rewards) == len(reward_titles), \
            f"number of reward in UI i.e {len(reward_titles)} == number of rewards in category i.e {len(rewards)}"
        for reward_index, reward_title in enumerate(reward_titles):
            reward_label_text = reward_title.text
            print(f'reward title = {rewards[reward_index].name} --- reward_label_text={reward_label_text}')
            assert reward_label_text == rewards[reward_index].name, \
                (f'reward title in ui = {reward_label_text} --- reward title ={rewards[reward_index].name} should be '
                 f'same')


def test_reward_detail_bulk_redemption_screen(setup, log_test_name, api_client_with_token):
    driver, _ = setup
    log_test_name()
    test_data = dataProvider.get_specific_row('RewardTest', 'bulk_redemption')

    reward = api_client_with_token.get_reward_detail(test_data.get('reward_pk'))
    print(f'test data for bulk redemption = {test_data}')

    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
    el1.click()
    #
    # # navigate to a reward where bulk redemption is available
    # # Demo E-Voucher LINK TYPE UG New
    reward_tile = driver.find_element(by=AppiumBy.XPATH,
                                      value="//XCUIElementTypeStaticText[@name=\"rewardCollectionRewardTitle\" and "
                                            f"@label=\"{test_data.get('reward_name')}\"]")
    reward_tile.click()

    # on redeem screen
    redeem_reward_title_text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRewardTitle').text
    assert redeem_reward_title_text == reward.name, (f'displayed reward tile ={redeem_reward_title_text}'
                                                     f' must be same as fetched from api {reward.name}')

    reward_valid_text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailValidityLabel').text.rstrip('\n')

    assert reward_valid_text == reward.formatted_valid_until(), \
        (f'displayed validity tile ={reward_valid_text}'
         f' must be same as fetched from api {reward.formatted_valid_until()}')

    tnc_toggle_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRedeemTNCToggleButton')
    tnc_toggle_button.click()
    tnc_text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRedeemTNCTextView').text
    log.logger.info(f'\n ------ displayed tnc  ------- \n {repr(tnc_text)}')
    log.logger.info(f'\n ------ fetched tnc  ------- \n {repr(reward.get_terms_and_conditions())}')

    assert tnc_text == reward.get_terms_and_conditions(), \
        (f'displayed tNc  ={repr(tnc_text)}'
         f' must be same as fetched from api {repr(reward.get_terms_and_conditions())}')

    # redeem reward
    redeem_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="redeemViewRedeemButton")
    redeem_button.click()
    redeem_confirmation = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Redeem Confirmation")
    assert redeem_confirmation is not None, "Redeem confirmation should appear"


def test_physical_reward_redemption(setup, log_test_name, api_client_with_token):
    driver, _ = setup
    log_test_name()
    test_data = dataProvider.get_specific_row('RewardTest', 'pysical_delivery')

    reward = api_client_with_token.get_reward_detail(test_data.get('reward_pk'))
    print(f'test data for bulk redemption = {test_data}')

    # rewards tab
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
    el1.click()

    # on redeem listing screen
    reward_tile = driver.find_element(by=AppiumBy.XPATH,
                                      value="//XCUIElementTypeStaticText[@name=\"rewardCollectionRewardTitle\" and "
                                            f"@label=\"{test_data.get('reward_name')}\"]")
    reward_tile.click()

    # reward detail screen
    redeem_reward_title_text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRewardTitle').text
    assert redeem_reward_title_text == reward.name, (f'displayed reward tile ={redeem_reward_title_text}'
                                                     f' must be same as fetched from api {reward.name}')

    # press redeem button
    redeem_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="redeemViewRedeemButton")
    redeem_button.click()

    # select address
    address_cell = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "selectAddressCell")[0]
    address_cell.click()

    select_address_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="selectAddressButton")
    select_address_button.click()

    # confirm redemption
    redeem_confirmation_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                                     value="redeemConfirmationDrawerRedeemButton")
    redeem_confirmation_button.click()

    # proceed for redemption
    # proceed_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "redeemBottomDrawerProceedButton")
    # proceed_button.click()
    #
    # # verify redemption screen
    # status_label_text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'redeemedStatusLabel').text
    # assert status_label_text == 'Order Placed!', 'Order should have been placed'
    #
    # redeemed_reward_text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'redeemedRIRewardName').text
    # assert redeemed_reward_text == reward.name, (f'displayed reward name on redemption screen {redeemed_reward_text}'
    #                                              f' should be {reward.name}')
