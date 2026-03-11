import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_get_all_bookings(base_url):
    username = os.getenv("BOOKER_USERNAME")
    password = os.getenv("BOOKER_PASSWORD")
    response = requests.get(f"{base_url}/booking", json={"username": username, "password": password})
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_booking(base_url):
    response = requests.get(f"{base_url}/booking")
    first_booking_id = response.json()[0]["bookingid"]
    booking_response = requests.get(f"{base_url}/booking/{first_booking_id}")
    assert booking_response.status_code == 200
    assert "firstname" in booking_response.json()
    assert "lastname" in booking_response.json()

def test_get_booking_not_found(base_url):
    booking_response = requests.get(f"{base_url}/booking/{999999}")
    assert booking_response.status_code == 404

def test_create_booking(base_url):
    response = requests.post(f"{base_url}/booking", json={"firstname": "John", "lastname": "Doe", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"}, "additionalneeds": "Breakfast"})
    assert response.status_code == 200

def test_create_booking_returns_data(base_url):
    response = requests.post(f"{base_url}/booking", json={"firstname": "John", "lastname": "Doe", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"}, "additionalneeds": "Breakfast"})
    assert "bookingid" in response.json()
    assert "firstname" in response.json()["booking"]

def test_update_booking(base_url, auth_token):
    response = requests.get(f"{base_url}/booking")
    first_booking_id = response.json()[0]["bookingid"]
    booking_response = requests.put(f"{base_url}/booking/{first_booking_id}", json={"firstname": "James", "lastname": "Doe", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"}, "additionalneeds": "Breakfast"}, headers={"Cookie": f"token={auth_token}"})
    assert booking_response.status_code == 200
    assert "firstname" in booking_response.json()
    assert "lastname" in booking_response.json()

def test_partial_update_booking(base_url, auth_token):
    response = requests.get(f"{base_url}/booking")
    first_booking_id = response.json()[0]["bookingid"]
    booking_response = requests.patch(f"{base_url}/booking/{first_booking_id}", json={"lastname": "Wolfe"}, headers={"Cookie": f"token={auth_token}"})
    assert booking_response.status_code == 200
    assert "lastname" in booking_response.json()

def test_delete_booking(base_url, auth_token):
    create_response = requests.post(f"{base_url}/booking", json={"firstname": "Jon", "lastname": "Wolfe", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"}, "additionalneeds": "Breakfast"})
    booking_id = create_response.json()["bookingid"]
    delete_booking = requests.delete(f"{base_url}/booking/{booking_id}", headers={"Cookie": f"token={auth_token}"})
    assert delete_booking.status_code == 201
    check_delete = requests.get(f"{base_url}/booking/{booking_id}", headers={"Cookie": f"token={auth_token}"})
    assert check_delete.status_code == 404