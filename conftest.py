import pytest
import allure

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *


@pytest.fixture()
def create_token(scope="session"):
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
def get_booking_id(scope="session"):
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
