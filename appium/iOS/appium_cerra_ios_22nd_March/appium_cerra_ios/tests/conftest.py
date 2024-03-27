import configparser
import os

import allure
import pytest
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy

from appium_drivers.driverFactory import DriverFactory
from appium_drivers.ios_driver import init_ios_driver
from datasource.datasourceFactory import DatasourceFactory
from utility.logger import setup_logger
from utility.configReader import read_config
from utility.screenshotUtil import take_screenshot_with_element_highlighted


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="session")
def logger():
    _logger = setup_logger()
    yield _logger
    _logger = None


@pytest.fixture(scope="session")
def datasource(logger):
    source = read_config('data', 'ground_truth_source')
    logger.info(f'ground truth datasource = {source}')
    return DatasourceFactory.create_datasource(source)


@pytest.fixture(scope="session")
def target_driver(logger, datasource):
    target = read_config('target', 'os')
    driver = DriverFactory.create_driver(target, datasource)
    logger.info(f'initiating driver {target} token = {datasource.token}')
    yield driver
    driver.quit()


@pytest.fixture()
def screenshot_on_failure(request, target_driver):
    yield
    item = request.node
    driver = target_driver
    if item.rep_call.failed:
        element_id = None
        for marker in item.iter_markers(name="highlight_on_failure"):
            element_id = marker.kwargs.get("element_id")
            break

        if element_id:
            # Find the element by XPath
            element = target_driver.find_element(AppiumBy.ACCESSIBILITY_ID, element_id)

        allure.attach(
            take_screenshot_with_element_highlighted(element, driver),
            # driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
        )



