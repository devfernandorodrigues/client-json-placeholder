import re
from typing import Optional

import pytest
import responses
from pydantic import BaseModel

from jsonplaceholder.base import BaseResource


class FakeSchema(BaseModel):
    id: Optional[int]
    name: str


class FakeResource(BaseResource):
    schema = FakeSchema
    ENDPOINT = "http://fakeendpoint.com/fake"


def make_json(fake_schema):
    return {
        "id": fake_schema.id,
        "name": fake_schema.name,
    }


fake_resource = FakeResource()


@pytest.fixture
def fake_schema(faker):
    return FakeSchema(id=faker.pyint(), name=faker.pystr())


@responses.activate
def test_all(fake_schema):
    responses.add(
        responses.GET,
        re.compile(r"^.+fake$"),
        json=[make_json(fake_schema)],
    )

    assert fake_resource.all() == [fake_schema]


@responses.activate
def test_get(fake_schema):
    responses.add(
        responses.GET,
        re.compile(r"^.+fake/\d+$"),
        json=make_json(fake_schema),
    )

    assert fake_resource.get(fake_schema.id) == fake_schema


@responses.activate
def test_create(fake_schema):
    responses.add(
        responses.POST,
        re.compile(r"^.+fake$"),
        json=make_json(fake_schema),
    )

    assert fake_resource.create(fake_schema) == fake_schema


@responses.activate
def test_update(fake_schema):
    responses.add(
        responses.PUT,
        re.compile(r"^.+fake/\d+$"),
        json=make_json(fake_schema),
    )

    assert fake_resource.update(fake_schema) == fake_schema


@responses.activate
def test_delete(fake_schema):
    responses.add(
        responses.DELETE,
        re.compile(r"^.+fake/\d+$"),
        json=make_json(fake_schema),
    )

    assert fake_resource.delete(fake_schema.id) is None
