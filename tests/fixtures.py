from os import environ

import pytest
from selenium import webdriver


@pytest.fixture()
def environment(request):
    # setup
    yield environ
    # teardown


@pytest.fixture()
def browser(request):
    driver = webdriver.Firefox()
    yield driver
    driver.close()
