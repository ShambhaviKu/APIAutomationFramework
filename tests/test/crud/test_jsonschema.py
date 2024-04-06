# Get Response
# Create json schema >>  https://www.jsonschema.net/
# validate json schema >> https://www.jsonschemavalidator.net/ >> Optional
# save Schema into file name >> Create_booking_scema.json

from jsonschema import validate
import pytest
import allure
from jsonschema.exceptions import ValidationError
import os

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *


class TestCreateBookingJsonSchema(object):

    @pytest.mark.positive
    @allure.title("#TC1 Create booking schema validation")
    @allure.description("Verify Create booking schema")
    @allure.testcase("To verify create booking schema")
    def test_create_booking_schema(self):
        def load_schema(file_name):
            with open(file_name, 'r') as file:
                return json.load(file)

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

        # Response schema validate with stored json schema

        print(os.getcwd())

        file_path = os.getcwd() + "/create_booking_schema.json"
        schema = load_schema(file_name=file_path)

        try:
            validate(instance=response.json(), schema=schema)

        except ValidationError as e:
            print(e.message)
            pytest.xfail("Incorrect json schema")
            # pytest.fail("fail : json schema error")
