import logging

import appium
import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService

from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)
appium_server_url = 'http://localhost:4723'


@pytest.fixture(scope='module')
def setup(request, api_client_with_token):
    capabilities = dict(
        platformName='iOS',
        deviceName='Phone 15 Pro Max',
        udid='22BB4B4B-66AA-4029-84FD-122A8E971D60',
        bundleId='com.rewardz.iOSCerra',
        noReset=True,
        showXcodeLog=True,
        locale='en_US',
        processArguments={
            'env':
                {
                    'UITesting': 'false',
                    'token': api_client_with_token.token
                }
        }
    )
    print(f'cap = {capabilities}')
    module_name = request.module.__name__
    print("-------- rewardz app: setup module ----------")
    log.logger.info(f"-------- rewardz app: setup module {module_name}----------")
    print('start appium service')
    log.logger.info("start appium service")
    appium_service = AppiumService()
    appium_service.start()
    print('start appium driver')
    log.logger.info("start appium driver")
    driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))
    driver.implicitly_wait(10)

    yield driver, appium_service
    print('quit appium driver')
    log.logger.info("quit appium driver")
    driver.quit()
    print('stop appium service')
    log.logger.info("stop appium service")
    appium_service.stop()
    log.logger.info(f"-------- rewardz app: closing module {module_name}---------")
    print(f"-------- rewardz app: closing module {module_name}---------")
