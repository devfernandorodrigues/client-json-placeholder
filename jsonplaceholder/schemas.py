from typing import Optional

from humps import camelize
from pydantic import BaseModel, Field


def camel(string):
    return camelize(string)


class Post(BaseModel):
    id: Optional[int]
    user_id: int = Field(..., alias="userId")
    title: str
    body: str

    class Config:
        alias_generator = camel
        allow_population_by_field_name = True


class Comment(BaseModel):
    post_id: int = Field(..., alias="postId")
    id: Optional[int]
    name: str
    email: str
    body: str

    class Config:
        alias_generator = camel
        allow_population_by_field_name = True


class Album(BaseModel):
    id: Optional[int]
    user_id: int = Field(..., alias="userId")
    title: str

    class Config:
        alias_generator = camel
        allow_population_by_field_name = True
