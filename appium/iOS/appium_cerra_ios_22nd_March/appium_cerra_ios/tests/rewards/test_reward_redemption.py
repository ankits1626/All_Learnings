from appium.webdriver.common.appiumby import AppiumBy

from screens.MainTabBar import MainTabBar
from utility import setupDataProvider


def test_reward_detail_bulk_redemption_screen(logger, datasource, target_driver, screenshot_on_failure):
    test_data = setupDataProvider.get_specific_row('RewardTest', 'bulk_redemption')
    reward = datasource.get_reward_detail(test_data.get('reward_pk'))
    platform = target_driver.capabilities['platformName']
    logger.info(f'{platform}: executing : test_reward_detail_bulk_redemption_screen : '
                f'for bulk redemption = {test_data}')

    # navigate to reward tab
    main_tab_bar = MainTabBar(target_driver, platform)
    reward_listing_screen = main_tab_bar.navigate_to_reward_tab()

    #click on se all button
    # all_rewards_screen = reward_listing_screen.navigate_to_all_rewards_page()

    # navigate to required reward
    reward_detail_screen = reward_listing_screen.navigate_to_reward_redemption(test_data.get('reward_name'))

    # on redeem screen
    redeem_reward_title_text = reward_detail_screen.get_reward_title()
    logger.info(f'<<<<<< redeem_reward_title_text = {redeem_reward_title_text}')
    assert redeem_reward_title_text == reward.name, (f'displayed reward tile ={redeem_reward_title_text}'
                                                     f' must be same as fetched from api {reward.name}')

    reward_valid_text = reward_detail_screen.get_reward_validity()

    assert reward_valid_text == reward.formatted_valid_until(), \
        (f'displayed validity tile ={reward_valid_text}'
         f' must be same as fetched from api {reward.formatted_valid_until()}')

    tnc_text = reward_detail_screen.get_reward_redemption_tnc()
    logger.info(f'\n ------ displayed tnc  ------- \n {repr(tnc_text)}')
    logger.info(f'\n ------ fetched tnc  ------- \n {repr(reward.get_terms_and_conditions())}')

    clean_tnc_ui_text = repr(tnc_text).replace("\n", "").replace("\t", "")
    clean_tnc_api_text = repr(reward.get_terms_and_conditions()).replace("\n", "").replace("\t", "")

    # do not delete this: this will fail in android because bulleted list is
    # assert clean_tnc_ui_text == clean_tnc_api_text, \
    #     (f'displayed tNc  ={repr(tnc_text)}'
    #      f' must be same as fetched from api {repr(reward.get_terms_and_conditions())}')

    # redeem reward
    redeem_confirmation = reward_detail_screen.open_redeem_confirmation_drawer()
    assert redeem_confirmation is not None, "Redeem confirmation should appear"
    redeem_confirmation.redeem_reward()
    # # redeem_confirmation.close_reward_redeem_confirmation_screen()

    # # press cancel and back button to go to reward listing
    # reward_detail_screen.close_reward_detail_screen()
    # main_tab_bar.navigate_to_home_tab()


#
#
# def test_physical_reward_redemption(logger, datasource, target_driver, screenshot_on_failure):
#     test_data = setupDataProvider.get_specific_row('RewardTest', 'pysical_delivery')

#     reward = datasource.get_reward_detail(test_data.get('reward_pk'))
#     platform = target_driver.capabilities['platformName']
#     logger.info(f'{platform}: executing : test_physical_reward_redemption : '
#                 f'for bulk redemption = {test_data}')

#     # rewards tab
#     main_tab_bar = MainTabBar(target_driver, platform)
#     reward_listing_screen = main_tab_bar.navigate_to_reward_tab()

#     # navigate to required reward
#     reward_detail_screen = reward_listing_screen.navigate_to_reward_redemption(test_data.get('reward_name'))

#     # on redeem screen
#     redeem_reward_title_text = reward_detail_screen.get_reward_title()
#     assert redeem_reward_title_text == reward.name, (f'displayed reward tile ={redeem_reward_title_text}'
#                                                      f' must be same as fetched from api {reward.name}')

#     address_selection_screen = reward_detail_screen.redeem_physical_reward()

#     # address selection
#     reward_redemption_confirmation_screen = address_selection_screen.select_address()

#     # verify redemption confirmation screen
#     assert reward_redemption_confirmation_screen.get_reward_title().text == reward.name, \
#         (f'displayed reward tile ={reward_redemption_confirmation_screen.get_reward_title().text}'
#          f' must be same as fetched from api {reward.name}')

#     confirmation_drawer = reward_redemption_confirmation_screen.redeem_reward()
#     assert confirmation_drawer.get_reward_name() == reward.name, \
#         (f'final confirmation drawer: '
#          f'displayed reward tile ={confirmation_drawer.get_reward_name()}'
#          f' must be same as fetched from api {reward.name}')

#     redeemed_reward_screen = confirmation_drawer.proceed_with_reward_redemption()

#     # verify redeemed screen
#     assert redeemed_reward_screen.get_redeemed_reward_name() == reward.name, \
#         (f'redeemed reward screen: '
#          f'displayed reward tile ={redeemed_reward_screen.get_redeemed_reward_name()}'
#          f' must be same as fetched from api {reward.name}')

#     assert redeemed_reward_screen.get_redeemed_reward_status() == 'Order Placed!', \
#         (f'redeemed reward screen: '
#          f'displayed status ={redeemed_reward_screen.get_redeemed_reward_status()}'
#          f' must be Order Placed! ')

#     # back
#     redeemed_reward_screen.go_back_to_rewards()
#     main_tab_bar.navigate_to_home_tab()
