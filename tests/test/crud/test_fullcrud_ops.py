# create token
# create booking id
# update booking(PUT)>> token, booking id
# Delete booking

import pytest
import allure

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *


class TestCRUDBooking(object):

    # create token
    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIconstants.create_token_url(),
                                headers=Util().common_headers_json(),
                                payload=create_token_payload(),
                                auth=None,
                                in_json=False
                                )
        token = response.json()["token"]
        verify_http_status_code(response, 200)
        verify_key_not_null(token)

        return token

    # Create Booking id
    @pytest.fixture()
    def get_booking_id(self):
        response = post_request(url=APIconstants.create_booking_url(),
                                headers=Util().common_headers_json(),
                                payload=create_booking_payload(),
                                auth=None,
                                in_json=False
                                )
        bookingid = response.json()["bookingid"]
        verify_http_status_code(response, 200)
        verify_key_not_equal_zero(bookingid)
        verify_key_not_null(bookingid)

        return bookingid

    # update booking >> put

    @allure.title("CRUD operation")
    @allure.testcase("TC#1 Update booking using PUT request")
    @allure.description("Verify that full update with booking id and token is working")
    def test_update_booking_put(self, get_booking_id, create_token):
        booking_id = get_booking_id
        token = create_token

        response = put_request(url=APIconstants.url_patch_put_delete(booking_id),
                               headers=Util().put_patch_delete_headers_cookie(token),
                               auth=None,
                               payload=create_booking_payload(),
                               in_json=False)
        first_name = response.json()["firstname"]
        last_name = response.json()["lastname"]

        # Verification
        verify_key_not_null(token)
        verify_http_status_code(response, 200)
        verify_first_name(first_name, "Jim")
        verify_last_name(last_name, "Brown")

    @allure.title("CRUD Operation")
    @allure.testcase("TC#2 Delete booking using delete request")
    @allure.description("verify booking get deleted")
    def test_delete_booking(self, get_booking_id, create_token):
        booking_id = get_booking_id
        token = create_token

        response = delete_request(url=APIconstants.url_patch_put_delete(booking_id),
                                  headers=Util().put_patch_delete_headers_cookie(token),
                                  auth=None,
                                  payload=None,
                                  in_json=False)
        # verification
        verify_http_status_code(response, 400)


        verify_delete_booking(response.text)
