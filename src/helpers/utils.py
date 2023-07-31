# This python file helps you to read the JSON  files and provide the json data

import json

def get_pay_load_auth():
    #Here we read the date from auth.json file and return that json data
    file=open("src/constants/auth.json") #here we are reading data from auth.json file
    data=json.load(file)"""This line loads the contents of the opened JSON file (file) and
                           The resulting data is stored in the variable data"""
    file.close()
    return data



def token_headers(create_token):
    temp_token = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    return headers


