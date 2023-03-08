import pytest

from jsonplaceholder.client import JsonPlaceholderClient
from jsonplaceholder.schemas import Comment, Post


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


@pytest.fixture
def post(faker):
    return Post(
        body=faker.pystr(),
        title=faker.pystr(),
        user_id=faker.pyint(),
    )
