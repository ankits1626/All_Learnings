import logging

import allure
import pytest
import requests
from allure_commons.types import AttachmentType

from Datasource.APIClient import APIClient
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="session")
def api_client_with_token():
    log.logger.info(f"preparing api_client for test")
    api_client = APIClient("https://skordev.com")  # Initialize APIClient
    api_client.login("ankit@gmail.com", "pass")
    print(f"Token: {api_client.token}")
    return api_client


@pytest.fixture
def log_test_name(request):
    def log_name():
        log.logger.info(f"started executing {request.node.name}")

    yield log_name


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


def teardown_module(module):
    print("teardown_module")
