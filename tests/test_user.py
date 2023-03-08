import re

import responses


@responses.activate
def test_create_camel_case(client, user, faker):
    responses.add(
        responses.POST,
        re.compile(r"^.+users$"),
        json={
            "id": faker.pyint(),
            "name": user.name,
            "username": user.username,
            "email": user.email,
            "address": {
                "street": user.address.street,
                "suite": user.address.suite,
                "city": user.address.city,
                "zipcode": user.address.zipcode,
                "geo": {
                    "lat": user.address.geo.lat,
                    "lng": user.address.geo.lng,
                },
            },
            "phone": user.phone,
            "website": user.website,
            "company": {
                "name": user.company.name,
                "catchPhrase": user.company.catch_phrase,
                "bs": user.company.bs,
            },
        },
    )

    created = client.User.create(user)
    assert created.id
    assert created.company.catch_phrase == user.company.catch_phrase
