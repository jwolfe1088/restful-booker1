BASE_URL = "https://www.automationintesting.online/"

class BookingPage():
    def  __init__(self, page):
        self.page = page

    def navigate_to_home(self):
        self.page.goto(BASE_URL)


    def navigate_to_booking_url(self):
        self.page.goto("https://automationintesting.online/reservation/1?checkin=2026-04-15&checkout=2026-04-16")
# Navigates to specific booking dates to bypass the date selector slider

    def click_reserve_now(self):
        self.page.click("#doReservation")

    def enter_user_information(self, first_name, last_name, email, phone):
        self.page.fill(".room-firstname", first_name)
        self.page.fill(".room-lastname", last_name)
        self.page.fill(".room-email", email)
        self.page.fill(".room-phone", phone)

