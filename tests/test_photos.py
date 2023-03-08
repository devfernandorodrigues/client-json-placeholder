import re

import responses

from jsonplaceholder.schemas import Photo


@responses.activate
def test_create_call_with_camel_case(client, faker):
    photo = Photo(
        album_id=faker.pyint(),
        title=faker.pystr(),
        thumbnail_url=faker.url(),
        url=faker.url(),
    )

    responses.add(
        responses.POST,
        re.compile(r"^.+photos$"),
        json={
            "albumId": photo.album_id,
            "id": faker.pyint(),
            "title": photo.title,
            "url": photo.url,
            "thumbnailUrl": photo.thumbnail_url,
        },
    )

    created = client.Photo.create(photo)
    assert created.album_id == photo.album_id
    assert created.title == photo.title
    assert created.url is not None
    assert created.thumbnail_url is not None
    assert created.id is not None
