import pytest
import allure
import openpyxl
import os

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append(({
            "username": username,
            "password": password
        }))
    return credentials


def create_token(username, password):
    payload = {"username": username,
               "password": password
               }
    response = post_request(url=APIconstants.create_token_url(),
                            headers=Util().common_headers_json(),
                            payload=payload,
                            auth=None,
                            in_json=False)
    return response


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(os.getcwd() + "/TestData_DDTesting.xlsx"))
def test_create_auth_with_excel(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = create_token(username, password)
    print(response.status_code)
