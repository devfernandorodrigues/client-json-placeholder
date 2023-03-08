import re

import responses

from jsonplaceholder.schemas import Todo


@responses.activate
def test_create_call_with_camel_case(client, faker):
    todo = Todo(
        user_id=faker.pyint(),
        title=faker.pystr(),
        completed=faker.pybool(),
    )

    responses.add(
        responses.POST,
        re.compile(r"^.+todos$"),
        json={
            "userId": todo.user_id,
            "id": faker.pyint(),
            "title": todo.title,
            "completed": todo.completed,
        },
    )

    created = client.Todo.create(todo)
    assert created.id
    assert created.title == todo.title
    assert created.completed == todo.completed
    assert created.user_id == todo.user_id
