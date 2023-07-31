
#here we can use common verifications using functions


# HTTP status code
def verify_http_code(response_data,expected_data):
    assert response_data.status_code==expected_data


# Any key should not be zero
def verify_key(key):
    assert key!=0 # checking key is non empty or not
    assert key>0  #key should be greater than zero



