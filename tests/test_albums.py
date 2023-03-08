import re

import responses
from responses import matchers

from jsonplaceholder.schemas import Album


@responses.activate
def test_create_call_with_camel_case(client, faker):
    album = Album(
        user_id=faker.pyint(),
        title=faker.pystr(),
    )

    responses.add(
        responses.POST,
        re.compile(r"^.+albums$"),
        json={
            "userId": faker.pyint(),
            "id": faker.pyint(),
            "title": faker.pystr(),
        },
        match=[
            matchers.json_params_matcher(
                {
                    "userId": album.user_id,
                    "title": album.title,
                    "id": album.id,
                }
            )
        ],
    )

    assert client.Album.create(album)
