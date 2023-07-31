

def token_headers(create_token):
    temp_token = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    return headers