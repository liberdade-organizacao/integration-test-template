from os import environ

import pytest


@pytest.fixture()
def environment(request):
    # setup
    yield environ
    # teardown
