from typing import Type


def create_booking_payload():
    payload={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

    return payload

def common_header():

    headers = {
        "Content-Type": "application/json",
       # "Cookie": var
    }

    return headers




def common_auth():
    auth={
    "username" : "admin",
    "password" : "password123"
}
    return auth

def update_booking_payload():
    updated_payload =  {
        "firstname": "Nagesh",
        "lastname": "Vadlamudi"
    }


    return updated_payload