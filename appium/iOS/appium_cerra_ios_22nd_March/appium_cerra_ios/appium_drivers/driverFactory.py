from appium_drivers.android_driver import init_android_driver
from appium_drivers.ios_driver import init_ios_driver


class DriverFactory:
    @staticmethod
    def create_driver(target, datasource):
        if target == 'ios':
            return init_ios_driver(datasource)
        if target == 'android':
            return init_android_driver(datasource)

        else:
            raise ValueError(f"Invalid source type: {target}")