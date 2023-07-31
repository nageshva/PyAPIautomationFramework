#add your constants here

#adding my URL constants here

def base_url():
    return "https://restful-booker.herokuapp.com"

def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"

def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"

def url_update_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/"+ booking_id

def url_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/"+booking_id


