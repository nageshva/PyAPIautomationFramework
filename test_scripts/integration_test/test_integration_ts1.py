
import pytest

from src.constants.apiconstants import url_create_booking, url_create_token, url_update_booking,url_delete_booking
from src.helpers.common_verifies import verify_key, verify_http_code
from src.helpers.payload_manager import create_booking_payload, common_header, common_auth, update_booking_payload
from src.helpers.wrapper import post_request, patch_request,delete_request
from src.helpers.token import token_headers

class TestIntegrationTC1(object):

    #@pytest.fixture
    def test_verify_create_booking(self):
        global booking_id
        response1 = post_request(url_create_booking(), auth=None, headers=common_header(),
                                payload=create_booking_payload(), in_json=False)
        print(response1.status_code)
        print(response1.json())
        verify_http_code(response1, 200)
        booking_id = response1.json()["bookingid"]
        verify_key(booking_id)
        print(booking_id)
        print(response1.json())

    @pytest.fixture
    def test_verify_create_token(self):
        response2=post_request(url_create_token(),auth=None,headers=common_header(),payload=common_auth(),in_json=False)
        print(response2.status_code)
        verify_http_code(response2,200)
        print(response2.text)
        token=response2.json()["token"]
        print(token)
        return token


    def test_verify_update_booking(self,test_verify_create_token):
        global booking_id
        response3=patch_request(url_update_booking(str(booking_id)),auth=None,headers=token_headers(test_verify_create_token),payload=update_booking_payload(),in_json=False)
        print(response3.status_code)
        verify_http_code(response3, 200)
        print(response3.text)
        print(response3.json())



    def test_verify_delete_booking(self,test_verify_create_token):
        global booking_id
        response4=delete_request(url_delete_booking(str(booking_id)),auth=None,headers=token_headers(test_verify_create_token),in_json=False)
        print(response4.status_code)
        verify_http_code(response4, 404)
        print(response4.text)
