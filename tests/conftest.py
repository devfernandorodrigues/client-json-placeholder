import pytest

from jsonplaceholder.client import JsonPlaceholderClient
from jsonplaceholder.schemas import Comment


@pytest.fixture
def client():
    return JsonPlaceholderClient()


@pytest.fixture
def comment(faker):
    return Comment(
        body=faker.pystr(),
        email=faker.email(),
        id=faker.pyint(),
        name=faker.pystr(),
        postId=faker.pyint(),
    )
