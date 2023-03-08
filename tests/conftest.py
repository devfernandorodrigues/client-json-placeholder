import pytest

from jsonplaceholder.client import JsonPlaceholderClient


@pytest.fixture
def client():
    return JsonPlaceholderClient()
