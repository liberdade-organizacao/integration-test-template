import pytest

from tests.fixtures import environment


class TestFixtures:
    def test_environment_fixture(self, environment):
        assert 'ENVIRONMENT' in environment
