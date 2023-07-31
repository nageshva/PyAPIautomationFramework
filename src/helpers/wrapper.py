
import requests

import json



def get_request(url,auth,in_json):
    response=requests.get(url=url,auth=auth)
    if in_json is True:
        return response.json()
    return response


def post_request(url,auth,headers,payload,in_json):
    post_response=requests.post(url=url,auth=auth,headers=headers ,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response


def patch_request(url,auth,headers,payload,in_json):
    patch_response=requests.patch(url=url,auth=auth,headers=headers ,data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response


def delete_request(url,auth,headers,in_json):
    delete_response=requests.post(url=url,auth=auth,headers=headers)
    if in_json is True:
        return delete_response.json()
    return delete_response
