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
def test_create_call_with_camel_case(client, comment):
    responses.add(
        responses.POST,
        re.compile(r"^.+comments$"),
        json=make_json(comment),
    )

    assert client.Comment.create(comment)


@responses.activate
def test_post_id(client, comment):
    responses.add(
        responses.GET,
        re.compile(r"^.+comments\?postId=\d+$"),
        json=[make_json(comment)],
    )

    assert client.Comment.post_id(comment.post_id) == [comment]
