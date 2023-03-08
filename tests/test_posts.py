import re

import responses
from responses import matchers

from jsonplaceholder.schemas import Comment, Post


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
