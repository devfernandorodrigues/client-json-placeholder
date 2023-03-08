from jsonplaceholder.resources import (
    AlbumResource,
    CommentResource,
    PhotoResource,
    PostResource,
)


class JsonPlaceholderClient:
    Post = PostResource()
    Comment = CommentResource()
    Album = AlbumResource()
    Photo = PhotoResource()
