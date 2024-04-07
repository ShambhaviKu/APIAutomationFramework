# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.


import pytest
import allure
import json
import requests

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *


class TestBookingIntg(object):

    @pytest.fixture()
    def create_booking(self):
        response = post_request(url=APIconstants.create_booking_url(),
                                headers=Util().common_headers_json(),
                                auth=None,
                                payload=create_booking_payload_integration(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        # Bookingid verification

        verify_http_status_code(response, 200)

        verify_key_not_equal_zero(booking_id)
        verify_key_not_null(booking_id)

        return booking_id

    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIconstants.create_token_url(),
                                headers=Util().common_headers_json(),
                                payload=create_token_payload(),
                                auth=None,
                                in_json=False
                                )
        token = response.json()["token"]
        return token

    # Patch Request - Verify that firstName is updated.

    @allure.title("TC#1 Integration test: partial update booking")
    @allure.testcase("Verify that first name is updated")
    @allure.description("verifying first name updation")
    def test_patch_request(self, create_booking, create_token):
        response = patch_request(url=APIconstants.url_patch_put_delete(create_booking),
                                 headers=Util().put_patch_delete_headers_cookie(create_token),
                                 auth=None,
                                 payload=patch_payload_integration(),
                                 in_json=False)

        first_name = response.json()["firstname"]
        print(first_name)

        verify_first_name(first_name, "shambhavi")
        verify_http_status_code(response, 200)

        verify_key_not_null(first_name)