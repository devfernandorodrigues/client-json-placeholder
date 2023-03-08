import pytest

from jsonplaceholder.client import JsonPlaceholderClient
from jsonplaceholder.schemas import Address, Comment, Company, Geo, Post, User


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


@pytest.fixture
def user(faker):
    address = Address(
        street=faker.pystr(),
        suite=faker.pystr(),
        city=faker.pystr(),
        zipcode=faker.pystr(),
        geo=Geo(
            lat=faker.pystr(),
            lng=faker.pystr(),
        ),
    )

    company = Company(
        name=faker.pystr(),
        catch_phrase=faker.pystr(),
        bs=faker.pystr(),
    )

    user = User(
        id=faker.pyint(),
        name=faker.name(),
        username=faker.user_name(),
        email=faker.email(),
        address=address,
        phone=faker.phone_number(),
        website=faker.url(),
        company=company,
    )

    return user
