from appium.options.ios import XCUITestOptions
from appium import webdriver


def init_ios_driver(datasource):
    appium_server_url = 'http://localhost:4723'
    print(f'<<<<<< passed token  {datasource.token}')
    capabilities = dict(
        platformName='iOS',
        deviceName='iPhone 15',
        udid='2E15D0AF-F116-4427-BA4B-96136DABDDE2',
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
