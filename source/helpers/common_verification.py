# common verification

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "error message = ER != AR"


def verify_key_not_equal_zero(key):
    assert key != 0, "error message = key = 0"
    assert key > 0, "error message = key < 0"


def verify_key_not_null(key):
    assert key is not None, "error message =  Key is Null"


def verify_first_name(key, expected_result):
    assert key == expected_result, "error message = firstname not matching"


def verify_last_name(key, expected_result):
    assert key == expected_result, "error message = lastname not matching"


def verify_delete_booking(response):
    assert "Created" in response


def verify_response_key(key, expected_data):
    assert key == expected_data

# Common Verfication
# HTTP Status Code
# Headers
# Data Verification
# JSON schema
