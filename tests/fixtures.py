import pytest


@pytest.fixture()
def resource(request):
    # setup
    yield "resource"
    # teardown
