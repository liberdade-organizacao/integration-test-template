import pytest

from tests.fixtures import environment, browser


class TestSetup:
    def test_environment_fixture(self, environment):
        assert 'ENVIRONMENT' in environment

    def test_selenium_works(self, browser):
        browser.get("https://www.crisjr.eng.br")
        title = browser.find_element_by_class_name("splash-head")
        assert title.text == "CRIS SILVA JR."
