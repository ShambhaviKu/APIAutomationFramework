# APIConstants - Class which contain all the endpoints. # Keep the URLs
# Static Method -> Which can be called by without the Object directly by using
# class you can call it

class APIconstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def create_token_url():
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def create_booking_url():
        return "https://restful-booker.herokuapp.com/booking"

    # Update, PUT, PATCH, DELETE - bookingId

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
