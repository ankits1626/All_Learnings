from appium.options.android import UiAutomator2Options
from appium import webdriver


def init_android_driver(datasource):
    appium_server_url = 'http://localhost:4723'
    capabilities = dict(
        platformName='Android',
        deviceName='Pixel_XL_API_27',
        # udid='emulator-5554',
        udid='c3954503',
        appPackage='com.root.cerrasg',
        noReset=True,
        # showXcodeLog=True,
        language='en',
        locale='US',

        appActivity="userprofile.presentation.activity.LoginActivity",
        optionalIntentArguments=f"-e token {datasource.token}",
        ignoreHiddenApiPolicyError=True
        # processArguments={
        #     'token': datasource.token
        # }
    )
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.implicitly_wait(10)
    return driver
