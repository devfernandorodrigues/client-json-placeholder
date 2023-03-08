import requests


def request(method, url, **kwargs):
    headers = kwargs.get("headers", {})
    headers["Content-Type"] = "application/json"
    kwargs["headers"] = headers

    resp = requests.request(method, url, **kwargs)
    resp.raise_for_status()

    return resp
