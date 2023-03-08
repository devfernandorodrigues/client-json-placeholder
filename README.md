# A client wrapper for JSONPlaceholder written in Python

Just a project to practice how to create a client in Python to use the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)

## How to use 

```python3
from jsonplaceholder.client import JsonPlaceholderClient

client = JsonPlaceholderClient()
client.<ResourceName>.all()
```



### Resources availables
```
- Post
- Comment
- Album
- Photo
- Todo
- User
```

##### Get all resources
```python3
client.Post.all()
>>> [Post(id=1, user_id=1, title='sunt aut facere repellat provident occaecati excepturi optio reprehenderit', body='quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto') ...]
```

##### Get one resource
```python3
client.Post.get(1)
>>> Post(id=1, user_id=1, title='sunt aut facere repellat provident occaecati excepturi optio reprehenderit', body='quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto')
```

#### Create resource
```python3
from jsonplaceholder.schemas import Post

post = Post(user_id=1, title="my fun post title", body="my fun post body")
created_post = client.Post.create(post)
created_post
>>> Post(id=101, user_id=1, title='my fun post title', body='my fun post body')
```

##### Update resource
```python3
post = client.Post.get(1)
post.title = "My post"
updated = client.Post.update(post)
updated
>>> Post(id=1, user_id=1, title='My post', body='quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto')
```

##### Delete resource
```python3
post = client.Post.all()[0]
client.Post.delete(post.id)
```


### Todo

- [ ] Patch resource
- [ ] Filter resource by query params
