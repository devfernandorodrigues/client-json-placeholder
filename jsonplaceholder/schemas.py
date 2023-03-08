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


class Photo(BaseModel):
    id: Optional[int]
    album_id: int = Field(..., alias="albumId")
    title: str
    url: str
    thumbnail_url: str = Field(..., alias="thumbnailUrl")

    class Config:
        alias_generator = camel
        allow_population_by_field_name = True


class Todo(BaseModel):
    id: Optional[int]
    user_id: int = Field(..., alias="userId")
    title: str
    completed: bool

    class Config:
        alias_generator = camel
        allow_population_by_field_name = True


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    geo: Geo
    street: str
    suite: str
    city: str
    zipcode: str


class Company(BaseModel):
    name: str
    catch_phrase: str = Field(None, alias="catchPhrase")
    bs: str


class User(BaseModel):
    id: Optional[int]
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company
