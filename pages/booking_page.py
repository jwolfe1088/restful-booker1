BASE_URL = "https://www.automationintesting.online/"

class BookingPage():
    def  __init__(self, page):
        self.page = page

    def navigate_to_home(self):
        self.page.goto(BASE_URL)


    def navigate_to_booking_url(self, checkin, checkout):
        self.page.goto(f"https://automationintesting.online/reservation/1?checkin={checkin}&checkout={checkout}")
        # Navigates to specific booking dates to bypass the date selector slider

    def click_reserve_now(self):
        self.page.click("#doReservation")

    def enter_user_information(self, first_name, last_name, email, phone):
        self.page.fill(".room-firstname", first_name)
        self.page.fill(".room-lastname", last_name)
        self.page.fill(".room-email", email)
        self.page.fill(".room-phone", phone)

    def confirm_booking(self):
        self.page.click(".btn-primary")

    def get_confirmation_message(self):
        return self.page.get_by_role("heading", name="Booking Confirmed").inner_text()
        

        # Need to fix both selectors 
    def get_booking_dates_text(self):
        return self.page.inner_text("p.text-center.pt-2 strong")