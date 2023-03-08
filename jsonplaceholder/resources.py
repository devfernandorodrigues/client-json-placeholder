from jsonplaceholder.base import BaseResource
from jsonplaceholder.request import request
from jsonplaceholder.schemas import Album, Comment, Photo, Post, Todo

BASE_URL = "https://jsonplaceholder.typicode.com"


class PostResource(BaseResource):
    schema = Post
    ENDPOINT = f"{BASE_URL}/posts"

    def comments(self, _id: int):
        resp = request("GET", f"{self.ENDPOINT}/{_id}/comments")
        return [Comment(**data) for data in resp.json()]


class CommentResource(BaseResource):
    ENDPOINT = f"{BASE_URL}/comments"
    schema = Comment

    def post_id(self, _id: int):
        resp = request("GET", f"{self.ENDPOINT}?postId={_id}")
        return [Comment(**data) for data in resp.json()]


class AlbumResource(BaseResource):
    ENDPOINT = f"{BASE_URL}/albums"
    schema = Album


class PhotoResource(BaseResource):
    ENDPOINT = f"{BASE_URL}/photos"
    schema = Photo


class TodoResource(BaseResource):
    ENDPOINT = f"{BASE_URL}/todos"
    schema = Todo
