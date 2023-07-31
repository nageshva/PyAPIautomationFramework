'''
Author:Nagesh
Objective: Create and Verify Booking Request
#TC1:Verify Status code,Headers
#TC2:Verify  body--> Booking ID
#TC3: Verify JSON Schema is Valid
'''


#First let us verify create booking working properly or not,the following requirements are
  # we need baseurl
  #we need payaload
  #headers
from src.constants.apiconstants import base_url,url_create_booking
from src.helpers.wrapper import post_request
from src.helpers.payload_manager import create_booking_payload,common_header
from src.helpers.common_verifies import verify_key,verify_http_code

class TestIntegrtaion(object):

    import pytest

    def test_create_booking_tc1(self):
        # headers = {
        #     "Content-Type": "application/json",
        # }

        response=post_request(url_create_booking(),auth=None, headers=common_header() ,payload=create_booking_payload(),in_json=False)
        print(response.status_code)
        print(response.json())

        verify_http_code(response,200)
        booking_id=response.json()["bookingid"]
        verify_key(booking_id)



    # def test_create_booking_tc2(self):
    #     assert True == False
    #
    # def test_create_booking_tc3(self):
    #     assert True == True





