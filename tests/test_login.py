import pytest
from tests.fixtures import resource


class TestResource:
    def test_fixture(self, resource):
        assert resource == "resource"
