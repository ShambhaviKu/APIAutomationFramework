import pytest
import requests
import json
import allure

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("#TC1 Create booking positive testcase")
    @allure.description("Verify Create booking")
    @allure.testcase("To verify booking id is not null and greater than zero")
    def test_create_booking_positive(self):
        response = post_request(url=APIconstants.create_booking_url(),
                                headers=Util().common_headers_json(),
                                auth=None,
                                payload=create_booking_payload(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        first_name = response.json()["booking"]["firstname"]

        verify_http_status_code(response, 200)

        verify_key_not_equal_zero(booking_id)

        verify_key_not_null(booking_id)

        verify_first_name(first_name, "Jim")

    @pytest.mark.negative
    @allure.title("#TC2 Create booking negative testcase")
    @allure.description("Verify Create booking")
    @allure.testcase("To verify booking when payload is empty")
    def test_create_booking_negative(self):
        response = post_request(url=APIconstants.create_booking_url(),
                                headers=Util().common_headers_json(),
                                auth=None,
                                payload={},
                                in_json=False)

        verify_http_status_code(response, 500)


