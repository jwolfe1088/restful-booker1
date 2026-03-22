import os
import pytest
import requests
from dotenv import load_dotenv
from pages.booking_page import BookingPage

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    BASE_URL = "https://restful-booker.herokuapp.com/"
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}_{rep.when}.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")