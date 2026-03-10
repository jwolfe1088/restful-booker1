import requests
from dotenv import load_dotenv
import os

load_dotenv()


def test_auth(base_url):
    username = os.getenv("BOOKER_USERNAME")
    password = os.getenv("BOOKER_PASSWORD")
    response = requests.post(f"{base_url}/auth", json={"username": username, "password": password})
    data = response.json()
    assert "token" in data
    assert data["token"] is not None

def test_invalid_credentials(base_url):
    username = os.getenv("BOOKER_USERNAME")
    password = "wrong_password"
    response = requests.post(f"{base_url}/auth", json={"username": username, "password": password})
    assert response.json()["reason"] == "Bad credentials"

def test_incomplete_credentials(base_url):
    username = ""
    password = os.getenv("BOOKER_PASSWORD")
    response = requests.post(f"{base_url}/auth", json={"username": username, "password": password})
    assert response.json()["reason"] == "Bad credentials"