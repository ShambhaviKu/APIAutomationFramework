# Invalid Creation - enter a wrong payload or Wrong JSON.

import pytest
import allure
import json
import requests

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *

@allure.title("TC#1 Invalid booking creation")
@allure.testcase("Verify status code")
@allure.description("verify if booking id created using invalid payload")
def test_invalid_create_booking():
    response = post_request(url=APIconstants.create_booking_url(),
                            headers=Util().common_headers_json(),
                            auth=None,
                            payload=invalid_payload_integration(),
                            in_json=False)

    #Verification
    verify_http_status_code(response, 500)
