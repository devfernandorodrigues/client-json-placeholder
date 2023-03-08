from jsonplaceholder.resources import CommentsResource, PostResource


class JsonPlaceholderClient:
    Post = PostResource()
    Comment = CommentsResource()
