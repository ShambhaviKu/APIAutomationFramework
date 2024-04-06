# Collection of API Methods
import json
import requests


def get_request(url, auth):
    response = requests.get(url=url, auth=auth)
    return response


def post_request(url, headers, auth, payload, in_json):
    post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response


def patch_request(url, headers, auth, payload, in_json):
    patch_response = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response


def put_request(url, headers, auth, payload, in_json):
    put_response = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response


def delete_request(url, headers, auth, payload, in_json):
    delete_response = requests.delete(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return delete_response.json()
    return delete_response
