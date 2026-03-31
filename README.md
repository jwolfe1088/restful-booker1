# Restful Booker - Hybrid UI + API Test Suite

Self-built end-to-end automation suite for the [Restful Booker](https://www.automationintesting.online) demo application using **Python, pytest, Playwright (UI)**, and **requests (API)**.

Built as part of my self-training for **Junior QA Automation Engineer** roles while transitioning from running a small business.

## About This Project

This suite demonstrates reliable hybrid testing:
- **API layer**: Authentication, full CRUD on bookings (create, read, update, partial update, delete), negative cases (not found, invalid credentials), and health checks
- **UI layer**: Complete user flow — room selection with dynamic dates, guest information input, checkout, and validation of success message and displayed dates
- Tests are designed to be re-runnable without manual data cleanup

## Technologies Used

- **Python 3.12**
- **pytest** (test framework + fixtures)
- **Playwright** (browser automation)
- **requests** (API testing)
- **GitHub Actions** (CI/CD)

## Key Features & What I Learned

- **Page Object Model (POM)** for clean separation of page logic and tests
- Reusable **pytest fixtures** in `conftest.py` to reduce duplication
- Dynamic test data (runtime dates) for reliable re-execution
- Integration of UI and API tests in one unified framework
- Robust locators (e.g., `get_by_placeholder`, `get_by_role`)
- Automated CI pipeline that runs the full suite on every push

## Project Structure
```
restful-booker1/
├── .github/workflows/      # GitHub Actions CI
├── pages/
│   └── booking_page.py     # POM implementation
├── tests/
│   ├── test_auth.py
│   ├── test_bookings.py
│   ├── test_ping.py
│   └── test_ui.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
└── screenshots/            # Failure artifacts
```

## Setup & Running Tests

1. Clone the repository
2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```
4. Create a `.env` file in the root directory:
```
BOOKER_USERNAME=admin
BOOKER_PASSWORD=password123
```
These are the standard public credentials for the Restful Booker demo app.

5. Run tests:
```bash
# All tests
pytest

# Verbose + stop on first failure
pytest -v -x

# Specific file
pytest tests/test_ui.py -v
```

## CI/CD

GitHub Actions workflow automatically runs the full test suite in headless mode on every push.

## Why This Matters for QA Roles

This project shows I can build maintainable, production-like automation that combines UI and API testing — skills directly applicable to real-world test frameworks.

