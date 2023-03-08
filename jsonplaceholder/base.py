from jsonplaceholder.request import request


class BaseResource:
    schema = None
    ENDPOINT = None

    def all(self):
        resp = request("GET", self.ENDPOINT)
        return [self.schema(**data) for data in resp.json()]

    def get(self, _id: int):
        resp = request("GET", f"{self.ENDPOINT}/{_id}")
        return self.schema(**resp.json())

    def create(self, schema: schema):
        resp = request("POST", self.ENDPOINT, data=schema.json(by_alias=True))
        return self.schema(**resp.json())

    def update(self, schema: schema):
        resp = request(
            "PUT",
            f"{self.ENDPOINT}/{schema.id}",
            data=schema.json(by_alias=True),
        )
        return self.schema(**resp.json())

    def delete(self, _id: int):
        request("DELETE", f"{self.ENDPOINT}/{_id}")
