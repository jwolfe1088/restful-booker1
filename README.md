# Restful Booking API + UI Test Suite

An automated testing suite targeting the booking app hosted at https://www.automationintesting.online using Python, Pytest, Playwright and Requests.

## About This Project

This project achieves end-to-end test automation for a web application. On the API side, it covers authentication, various booking requests like: get all bookings, update booking, partial update, delete booking, as well as testing booking not found. It also includes a full UI flow from selecting a room, checking out and asserting a specific success message and the exact dates are displayed.

## Technologies Used

- **Python 3.12**
- **Pytest** Testing Framework
- **Playwright** Browser Automation
- **Requests** HTTP API Testing

## Testing Coverage

- Full UI user flow, covers room selection, user information input and checkout. Includes dynamic runtime dates to allow for multiple retests. 
- API authentication tests cover successful authentication, invalid and incomplete credentials. 
- API tests for the booking function, covering retrieve, create, delete and update/partial update bookings, along with booking not found.

## CI/CD

This project includes a GitHub Actions workflow that automatically runs the full test suite on every push.

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
## Setup Instructions

### Prerequisites 

1. Clone this repository
2. Create a virtual environment:
```bash
   python -m venv venv
```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies
```bash
   pip install -r requirements.txt
   pip uninstall pytest-base-url -y
   playwright install
```
5. Create a `.env` file in the root directory with your test credentials:
```
BOOKER_USERNAME=admin
BOOKER_PASSWORD=password123
```

## How To Run
```
# Run all tests
pytest

# Run specific file
pytest tests/test_auth.py

# Run with verbose output + stop on first failure
pytest -v -x
```
## Design Patterns

- **Page Object Model (POM)** - Each page is represented by a class in the `pages/` directory, separating test logic from page interactions
- **Fixtures** - Shared setup managed via `conftest.py` to avoid code repetition