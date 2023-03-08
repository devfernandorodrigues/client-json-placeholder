import re

import responses
from responses import matchers

from jsonplaceholder.schemas import Comment, Post


@responses.activate
def test_all(client, faker):
    title = faker.pystr()
    body = faker.pystr()
    responses.add(
        responses.GET,
        re.compile(r"^.+posts$"),
        json=[
            {
                "userId": 1,
                "id": 1,
                "title": title,
                "body": body,
            }
        ],
    )

    assert client.Post.all() == [
        Post(
            user_id=1,
            id=1,
            title=title,
            body=body,
        )
    ]


@responses.activate
def test_get(client, faker):
    title = faker.pystr()
    body = faker.pystr()
    responses.add(
        responses.GET,
        re.compile(r"^.+posts/(\d+)$"),
        json={
            "userId": 1,
            "id": 1,
            "title": title,
            "body": body,
        },
    )

    assert client.Post.get(1) == Post(
        user_id=1,
        id=1,
        title=title,
        body=body,
    )


@responses.activate
def test_create(client, faker):
    post = Post(
        body=faker.pystr(),
        title=faker.pystr(),
        user_id=faker.pyint(),
    )
    responses.add(
        responses.POST,
        re.compile(r"^.+posts$"),
        json={
            "userId": post.user_id,
            "id": faker.pyint(),
            "title": post.title,
            "body": post.body,
        },
    )

    created = client.Post.create(post)
    assert created.body == post.body
    assert created.title == post.title
    assert created.user_id == post.user_id
    assert created.id


@responses.activate
def test_create_call_with_camel_case(client, faker):
    post = Post(
        body=faker.pystr(),
        title=faker.pystr(),
        user_id=faker.pyint(),
    )
    responses.add(
        responses.POST,
        re.compile(r"^.+posts$"),
        json={
            "userId": post.user_id,
            "id": faker.pyint(),
            "title": post.title,
            "body": post.body,
        },
        match=[
            matchers.json_params_matcher(
                {
                    "userId": post.user_id,
                    "id": post.id,
                    "title": post.title,
                    "body": post.body,
                }
            )
        ],
    )

    assert client.Post.create(post)


@responses.activate
def test_comments(client, faker):
    comment = Comment(
        post_id=faker.pyint(),
        id=faker.pyint(),
        name=faker.pystr(),
        email=faker.email(),
        body=faker.pystr(),
    )

    responses.add(
        responses.GET,
        re.compile(r"^.+comments$"),
        json=[
            {
                "postId": comment.post_id,
                "id": comment.id,
                "name": comment.name,
                "email": comment.email,
                "body": comment.body,
            }
        ],
    )

    assert client.Post.comments(1) == [comment]


@responses.activate
def test_update(client, faker):
    post = Post(
        body=faker.pystr(),
        title=faker.pystr(),
        user_id=faker.pyint(),
        id=1,
    )

    responses.add(
        responses.PUT,
        re.compile(r"^.+posts/1$"),
        json={
            "title": post.title,
            "body": post.body,
            "userId": post.user_id,
            "id": post.id,
        },
    )

    assert client.Post.update(post) == post


@responses.activate
def test_delete(client):
    responses.add(responses.DELETE, re.compile(r"^.+posts/1$"), json={})

    assert client.Post.delete(1) is None
