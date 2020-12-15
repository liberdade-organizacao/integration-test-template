from os import environ

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def environment(request):
    yield environ


@pytest.fixture()
def browser(request):
    # driver setup
    headless = bool(environ['HEADLESS'])

    if environ['BROWSER'] == 'chrome':
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(options=options)
    else:  # firefox as default
        options = FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(options=options)

    # provide driver
    yield driver

    # driver teardown
    driver.close()
