1.
# Playwright + Pytest Quick Reference Cheat Sheet
Last updated: March 2026 – for Jon's QA automation projects

## 1. Basic Setup & Running Tests
```bash
# Create venv (do once per machine)
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run specific file
pytest tests/test_login.py

# Run with verbose output + stop on first failure
pytest -v -x

# Run with HTML report
pytest --html=report.html --self-contained-html


2. Playwright Basics (Sync API – most common for beginners)

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500) # slow_mo for debugging
    page = browser.new_page()
    
    # Go to URL
    page.goto("https://example.com")
    
    # Common locators
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username").fill("user")
    page.get_by_label("Password").fill("pass")
    page.get_by_text("Welcome").wait_for(state="visible")
    page.locator("#submit-btn").click()
    page.locator("xpath=//div[contains(text(),'Error')]").is_visible()
    
    # Assertions (prefer expect)
    expect(page.get_by_text("Success")).to_be_visible(timeout=10000)
    expect(page).to_have_title("Dashboard")
    expect(page.locator(".error-message")).to_have_text("Invalid credentials")
    
    # Screenshot & video
    page.screenshot(path="screenshot.png")
    context = browser.new_context(record_video_dir="videos/")
    
    # Close
    browser.close()

3. Pytest Fixtures (most powerful part)

# conftest.py (place in tests/ or root)
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

# Usage in test file
def test_login(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://saucedemo.com/inventory.html")

4. . Page Object Model (POM) Template

# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator(".error-message-container")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()

# tests/test_login.py
from pages.login_page import LoginPage

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.login("wrong", "wrong")
    assert "Epic sadface" in login_page.get_error_message()

5. Common Playwright Gotchas / Snippets

# Waits (avoid time.sleep!)
page.wait_for_selector("#results", state="visible", timeout=15000)
page.wait_for_load_state("networkidle")
page.wait_for_function("document.querySelector('.loaded') !== null")

# Handling dialogs/alerts
page.on("dialog", lambda dialog: dialog.accept()) # auto-accept
page.on("dialog", lambda dialog: dialog.dismiss()) # auto-dismiss

# Frames / iframes
frame = page.frame_locator("#iframe-id")
frame.get_by_role("button").click()

# Download file
with page.expect_download() as download_info:
    page.get_by_role("link", name="Download").click()
download = download_info.value
download.save_as("file.pdf")

# API testing (via request context)
api_request_context = page.request
response = api_request_context.get("https://api.example.com/users")
assert response.ok
assert response.json()[0]["name"] == "John"

6. Debugging Tips

Run with --headed and slow_mo=500: pytest --headed --slowmo 500

Trace viewer: playwright show-trace trace.zip (add --tracing on in tests)

Screenshot on failure: pytest-playwright plugin does this automatically

Breakpoint: import pdb; pdb.set_trace() or use VS Code debugger

7. Quick Reference Links (bookmark these)

Playwright Python docs: https://playwright.dev/python/docs/intro

Pytest docs: https://docs.pytest.org

Playwright locators cheat sheet: https://playwright.dev/python/docs/locators

GitHub Actions for Pytest: Search "playwright pytest github actions workflow"


## API Testing with Playwright + Pytest (Heavy Focus)

Playwright's built-in `request` context is super powerful for API testing — no need for `requests` library most of the time.

### 1. Basic API Request Setup (in conftest.py or test file)

```python
# conftest.py (recommended for reuse)
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def api_request():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="https://restful-booker.herokuapp.com", # change to your API base
            extra_http_headers={"Content-Type": "application/json"}
        )
        yield request_context
        request_context.dispose()

2. Common API Test Patterns

# tests/test_api_bookings.py
import pytest
from playwright.sync_api import expect

def test_create_booking(api_request):
    payload = {
        "firstname": "Jon",
        "lastname": "Wolfe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-04-01", "checkout": "2026-04-10"},
        "additionalneeds": "Breakfast"
    }

    response = api_request.post("/booking", data=payload)

    # Basic assertions
    assert response.ok
    assert response.status == 200
    json_data = response.json()
    assert "bookingid" in json_data
    assert json_data["booking"]["firstname"] == "Jon"

    # Playwright-style expect (more readable)
    expect(response).to_be_ok()
    expect(response).to_have_status(200)
    expect(json_data["booking"]["lastname"]).to_be("Wolfe")

3. Auth / Token Handling (Very Common in Interviews)

# Get auth token first (reusable fixture)
@pytest.fixture(scope="session")
def auth_token(api_request):
    auth_payload = {"username": "admin", "password": "password123"}
    response = api_request.post("/auth", data=auth_payload)
    assert response.ok
    return response.json()["token"]

# Use token in protected endpoint
def test_update_booking(api_request, auth_token):
    booking_id = 1 # or create one first and get ID
    update_payload = {"firstname": "UpdatedJon"}

    response = api_request.put(
        f"/booking/{booking_id}",
        data=update_payload,
        headers={"Cookie": f"token={auth_token}"}
    )

    expect(response).to_be_ok()
    expect(response.json()["firstname"]).to_be("UpdatedJon")

4. Query Params, Headers, Negative Cases

def test_get_bookings_with_query(api_request):
    response = api_request.get(
        "/booking",
        params={"firstname": "Jon", "lastname": "Wolfe"}
    )
    expect(response).to_be_ok()
    bookings = response.json()
    expect(len(bookings)).to_be_greater_than(0)

# Negative case example
def test_invalid_auth(api_request):
    response = api_request.post(
        "/booking",
        data={"firstname": "Test"},
        headers={"Authorization": "Bearer invalid-token"}
    )
    expect(response.status).to_be(403) # or 401
    expect(response.json()["error"]).to_contain("Unauthorized")
5. File Upload / Download / Multipart
# Upload file
def test_upload_file(api_request):
    with open("test_file.pdf", "rb") as file:
        response = api_request.post(
            "/upload",
            multipart={"file": ("test.pdf", file, "application/pdf")}
        )
    expect(response).to_be_ok()

# Download file
def test_download_file(api_request):
    response = api_request.get("/download/123")
    expect(response.ok)
    with open("downloaded.pdf", "wb") as f:
        f.write(response.body())

6. Common Assertions & Debugging

# Expect helpers
expect(response).to_be_ok() # status 200-299
expect(response).to_have_status(201) # exact status
expect(response.json()["id"]).to_be(42)
expect(response.json()["data"]).to_have_length(5)
expect(response.headers["content-type"]).to_contain("application/json")

# Debugging slow tests
# Add timeout=30000 (30 sec) on slow endpoints
response = api_request.get("/slow-endpoint", timeout=30000)

7. Data-Driven / Parametrized API Tests

@pytest.mark.parametrize("username, password, expected_status", [
    ("admin", "password123", 200),
    ("wrong", "wrong", 401),
    ("", "", 400),
])
def test_auth_variations(api_request, username, password, expected_status):
    response = api_request.post("/auth", data={"username": username, "password": password})
    expect(response.status).to_be(expected_status)

8. Tips for API That "Doesn't Click Yet"

Always start with response.json() or response.text() to see what you get.

Use print(response.url) and print(response.headers) when debugging.

Test one endpoint at a time — get GET working, then POST, then auth.

Use Postman/Thunder Client first to explore the API → then copy working requests to Playwright.

If stuck on auth: Print the token and manually test in browser/Postman.
