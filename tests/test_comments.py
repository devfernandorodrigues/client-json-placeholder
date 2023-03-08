import re

import responses


def make_json(comment):
    return {
        "postId": comment.post_id,
        "email": comment.email,
        "id": comment.id,
        "name": comment.name,
        "body": comment.body,
    }


@responses.activate
def test_all(client, comment):
    responses.add(
        responses.GET,
        re.compile(r"^.+comments$"),
        json=[make_json(comment)],
    )

    assert client.Comment.all() == [comment]


@responses.activate
def test_get(client, comment):
    responses.add(
        responses.GET,
        re.compile(r"^.+comments/\d+$"),
        json=make_json(comment),
    )

    assert client.Comment.get(comment.id) == comment


@responses.activate
def test_create(client, comment):
    responses.add(
        responses.POST,
        re.compile(r"^.+comments$"),
        json=make_json(comment),
    )

    created = client.Comment.create(comment)

    assert created.id
    assert created.post_id == comment.post_id
    assert created.name == comment.name
    assert created.email == comment.email
    assert created.body == comment.body


@responses.activate
def test_create_call_with_camel_case(client, comment):
    responses.add(
        responses.POST,
        re.compile(r"^.+comments$"),
        json=make_json(comment),
    )

    assert client.Comment.create(comment)


@responses.activate
def test_update(client, comment):
    responses.add(
        responses.PUT,
        re.compile(r"^.+comments/\d+$"),
        json=make_json(comment),
    )

    assert client.Comment.update(comment) == comment


@responses.activate
def test_delete(client):
    responses.add(responses.DELETE, re.compile(r"^.+comments/\d+$"), json={})

    assert client.Comment.delete(1) is None


@responses.activate
def test_post_id(client, comment):
    responses.add(
        responses.GET,
        re.compile(r"^.+comments\?postId=\d+$"),
        json=[make_json(comment)],
    )

    assert client.Comment.post_id(comment.post_id) == [comment]
