# from appium.webdriver.common.appiumby import AppiumBy
#
# from utility import setupDataProvider
#
#
# def test_reward_detail_bulk_redemption_screen(logger, datasource, target_driver, screenshot_on_failure):
#     test_data = setupDataProvider.get_specific_row('RewardTest', 'bulk_redemption')
#
#     reward = datasource.get_reward_detail(test_data.get('reward_pk'))
#     print(f'test data for bulk redemption = {test_data}')
#
#     el1 = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
#     el1.click()
#     #
#     # # navigate to a reward where bulk redemption is available
#     # # Demo E-Voucher LINK TYPE UG New
#     reward_tile = target_driver.find_element(by=AppiumBy.XPATH,
#                                              value="//XCUIElementTypeStaticText[@name=\"rewardCollectionRewardTitle\" and "
#                                                    f"@label=\"{test_data.get('reward_name')}\"]")
#     reward_tile.click()
#
#     # on redeem screen
#     redeem_reward_title_text = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRewardTitle').text
#     assert redeem_reward_title_text == reward.name, (f'displayed reward tile ={redeem_reward_title_text}'
#                                                      f' must be same as fetched from api {reward.name}')
#
#     reward_valid_text = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailValidityLabel').text.rstrip(
#         '\n')
#
#     assert reward_valid_text == reward.formatted_valid_until(), \
#         (f'displayed validity tile ={reward_valid_text}'
#          f' must be same as fetched from api {reward.formatted_valid_until()}')
#
#     tnc_toggle_button = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRedeemTNCToggleButton')
#     tnc_toggle_button.click()
#     tnc_text = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRedeemTNCTextView').text
#     logger.info(f'\n ------ displayed tnc  ------- \n {repr(tnc_text)}')
#     logger.info(f'\n ------ fetched tnc  ------- \n {repr(reward.get_terms_and_conditions())}')
#
#     assert tnc_text == reward.get_terms_and_conditions(), \
#         (f'displayed tNc  ={repr(tnc_text)}'
#          f' must be same as fetched from api {repr(reward.get_terms_and_conditions())}')
#
#     # redeem reward
#     redeem_button = target_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="redeemViewRedeemButton")
#     redeem_button.click()
#     redeem_confirmation = target_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
#                                                      value="redeemConfirmationDrawerTitle")
#     assert redeem_confirmation is not None, "Redeem confirmation should appear"
#
#     # press cancel and back button to go to reward listing
#
#     target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'redeemConfirmationDrawerCancelButton').click()
#     target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rfk newBackButton').click()
#
#
# def test_physical_reward_redemption(logger, datasource, target_driver, screenshot_on_failure):
#     test_data = setupDataProvider.get_specific_row('RewardTest', 'pysical_delivery')
#
#     reward = datasource.get_reward_detail(test_data.get('reward_pk'))
#     print(f'test data for bulk redemption = {test_data}')
#
#     # rewards tab
#     el1 = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainTabRewardz")
#     el1.click()
#
#     # on redeem listing screen
#     reward_tile = target_driver.find_element(by=AppiumBy.XPATH,
#                                              value="//XCUIElementTypeStaticText[@name=\"rewardCollectionRewardTitle\" and "
#                                                    f"@label=\"{test_data.get('reward_name')}\"]")
#     reward_tile.click()
#
#     # reward detail screen
#     redeem_reward_title_text = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'rewardDetailRewardTitle').text
#     assert redeem_reward_title_text == reward.name, (f'displayed reward tile ={redeem_reward_title_text}'
#                                                      f' must be same as fetched from api {reward.name}')
#
#     # press redeem button
#     redeem_button = target_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="redeemViewRedeemButton")
#     redeem_button.click()
#
#     # select address
#     address_cell = target_driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "selectAddressCell")[0]
#     address_cell.click()
#
#     select_address_button = target_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="selectAddressButton")
#     select_address_button.click()
#
#     # confirm redemption
#     redeem_confirmation_button = target_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
#                                                             value="redeemConfirmationDrawerRedeemButton")
#     redeem_confirmation_button.click()
#
#     # proceed for redemption
#     proceed_button = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "redeemBottomDrawerProceedButton")
#     proceed_button.click()
#
#     # verify redemption screen
#     status_label_text = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'redeemedStatusLabel').text
#     assert status_label_text == 'Order Placed!', 'Order should have been placed'
#
#     redeemed_reward_text = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'redeemedRIRewardName').text
#     assert redeemed_reward_text == reward.name, (f'displayed reward name on redemption screen {redeemed_reward_text}'
#                                                  f' should be {reward.name}')
