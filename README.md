# Restful Booking API + UI Test Suite

An automated testing suite targeting the booking app hosted at https://www.automationintesting.online using Python, Pytest, Playwright and Requests.

## About This Project

This project acheives end-to-end test automation for a web application. On the API side, it covers uthentication, various booking requests like: get all bookings, update booking, partial update, delete booking, as well as testing booking not found. It also includes a full UI flow from selecting a room, checking out and asserting a specific sucess message and the exact dates are displayed.

## Technologies Used

- **Python 3.12**
- **Pytest** Testing Framework
- **Playwright** Browser Automation
- **Requests** 

## Testing Coverage

- Full UI user flow, covers room selection, user information input and checkout. Includes dynamic runtime dates to allow for multiple retests. 
- API authentication tests cover successful authentication, invalid and incomplete credentials. 
- API tests for the booking function, covering retrieve, create, delete and update/partial update bookings, along with booking not found.

## Project Structure
```
restful-booker1/
├── pages/
│   ├── booking_page.py
├── tests/
│   ├── test_auth.py
│   ├── test_bookings.py
│   ├── test_ping.py
│   └── test_ui.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
