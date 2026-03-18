import os
import pytest
import requests
from dotenv import load_dotenv
from pages.booking_page import BookingPage

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    BASE_URL = "https://www.automationintesting.online/"
    return BASE_URL

@pytest.fixture(scope="session")
def auth_token(base_url):
    username = os.getenv("BOOKER_USERNAME")
    password = os.getenv("BOOKER_PASSWORD")
    response = requests.post(f"{base_url}/auth", json={"username": username, "password": password})
    return response.json()["token"]

@pytest.fixture()
def booking_page(page):
    return BookingPage(page)