from jsonplaceholder.base import BaseResource
from jsonplaceholder.request import request
from jsonplaceholder.schemas import Comment, Post

BASE_URL = "https://jsonplaceholder.typicode.com"


class PostResource(BaseResource):
    schema = Post
    ENDPOINT = f"{BASE_URL}/posts"

    def comments(self, _id: int):
        resp = request("GET", f"{self.ENDPOINT}/{_id}/comments")
        return [Comment(**data) for data in resp.json()]


class CommentsResource(BaseResource):
    ENDPOINT = f"{BASE_URL}/comments"
    schema = Comment

    def post_id(self, _id: int):
        resp = request("GET", f"{self.ENDPOINT}?postId={_id}")
        return [Comment(**data) for data in resp.json()]


class JsonPlaceholderClient:
    Post = PostResource()
    Comment = CommentsResource()
