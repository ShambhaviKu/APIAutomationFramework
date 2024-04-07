# collection of all payloads

import faker
from faker import Faker

import json

faker = Faker()


def create_booking_payload():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    return payload


def create_booking_payload_dynamic():
    payload_dynamic = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "WiFi", "Extra Bed"))
    }

    return payload_dynamic


def create_token_payload():
    payload_token = {
        "username": "admin",
        "password": "password123"
    }

    return payload_token


def create_booking_payload_integration():
    payload = {
        "firstname": "yash",
        "lastname": "Alatekar",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": "Breakfast"
    }

    return payload


def patch_payload_integration():
    payload = {
        "firstname": "shambhavi",
        "lastname": "Alatekar",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": "Breakfast"
    }

    return payload

def existing_put_payload_integration():
    payload = {
        "firstname": "john",
        "lastname": "cameron",
        "totalprice": 5000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": "Breakfast"
    }

    return payload


def invalid_payload_integration():
    payload = {
        "firstname": 123,
        "lastname": "cameron",
        "totalprice": "ABC",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": "Breakfast"
    }

    return payload
