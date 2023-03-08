import requests

from jsonplaceholder.schemas import Comment, Post

BASE_URL = "https://jsonplaceholder.typicode.com"


def request(method, url, **kwargs):
    headers = kwargs.get("headers", {})
    headers["Content-Type"] = "application/json"
    kwargs["headers"] = headers

    resp = requests.request(method, url, **kwargs)
    resp.raise_for_status()

    return resp


class PostResource:
    ENDPOINT = f"{BASE_URL}/posts"

    def all(self):
        resp = request("GET", self.ENDPOINT)
        return [Post(**data) for data in resp.json()]

    def get(self, _id: int):
        resp = request("GET", f"{self.ENDPOINT}/{_id}")
        return Post(**resp.json())

    def create(self, post: Post):
        resp = request("POST", self.ENDPOINT, data=post.json(by_alias=True))
        return Post(**resp.json())

    def comments(self, _id: int):
        resp = request("GET", f"{self.ENDPOINT}/{_id}/comments")
        return [Comment(**data) for data in resp.json()]

    def update(self, post: Post):
        resp = request("PUT", f"{self.ENDPOINT}/{post.id}")
        return Post(**resp.json())

    def delete(self, _id: int):
        request("DELETE", f"{self.ENDPOINT}/{_id}")


class JsonPlaceholderClient:
    Post = PostResource()
