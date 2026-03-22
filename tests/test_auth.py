import requests
from dotenv import load_dotenv
import os

load_dotenv()


def test_auth(api_base_url):
    username = os.getenv("BOOKER_USERNAME")
    password = os.getenv("BOOKER_PASSWORD")
    response = requests.post(f"{api_base_url}/auth", json={"username": username, "password": password})
    data = response.json()
    assert "token" in data
    assert data["token"] is not None

def test_invalid_credentials(api_base_url):
    username = os.getenv("BOOKER_USERNAME")
    password = "wrong_password"
    response = requests.post(f"{api_base_url}/auth", json={"username": username, "password": password})
    assert response.json()["reason"] == "Bad credentials"

def test_incomplete_credentials(api_base_url):
    username = ""
    password = os.getenv("BOOKER_PASSWORD")
    response = requests.post(f"{api_base_url}/auth", json={"username": username, "password": password})
    assert response.json()["reason"] == "Bad credentials"