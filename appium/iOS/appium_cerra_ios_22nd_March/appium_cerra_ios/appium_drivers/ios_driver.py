from appium.options.ios import XCUITestOptions
from appium import webdriver


def init_ios_driver(datasource):
    appium_server_url = 'http://localhost:4723'
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
                    'token': datasource.token
                }
        }
    )
    driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))
    driver.implicitly_wait(10)
    return driver
