from jsonplaceholder.resources import (
    AlbumResource,
    CommentResource,
    PhotoResource,
    PostResource,
    TodoResource,
)


class JsonPlaceholderClient:
    Post = PostResource()
    Comment = CommentResource()
    Album = AlbumResource()
    Photo = PhotoResource()
    Todo = TodoResource()
