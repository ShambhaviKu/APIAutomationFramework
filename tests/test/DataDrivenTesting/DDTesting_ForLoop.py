import pytest
import openpyxl

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
    payload = {
        "username": username,
        "password": password
    }

    response = post_request(url=APIconstants.create_token_url(),
                            headers=Util().common_headers_json(),
                            payload=payload,
                            auth=None,
                            in_json= False)

    return response


def test_create_auth_with_excel():
    file_path = "C:/Users/alate/PycharmProjects/APITestAutomationFramework/tests/test/DataDrivenTesting/TestData_DDTesting.xlsx"
    credentials = read_credentials_from_excel(file_path=file_path)
    print(credentials)
    """for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = create_token(username=username, password=password)
        print(response.status_code)"""
