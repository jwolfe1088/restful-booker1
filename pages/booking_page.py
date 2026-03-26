BASE_URL = "https://www.automationintesting.online/"

class BookingPage():
    def  __init__(self, page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("Firstname")
        self.last_name_input = page.get_by_placeholder("Lastname")
        self.email_input = page.get_by_placeholder("Email")
        self.phone_input = page.get_by_placeholder("Phone")
        self.reserve_now = page.get_by_role("button", name="Reserve Now")
        self.confirmation_message = page.get_by_role("heading", name="Booking Confirmed")
    
    def navigate_to_home(self):
        self.page.goto(BASE_URL)


    def navigate_to_booking_url(self, checkin, checkout):
        self.page.goto(f"https://automationintesting.online/reservation/1?checkin={checkin}&checkout={checkout}")
        # Navigates to specific booking dates to bypass the date selector slider

    def click_reserve_now(self):
        self.reserve_now.click()

    def enter_user_information(self, first_name, last_name, email, phone):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.phone_input.fill(phone)

    def confirm_booking(self):
        self.reserve_now.click()

    def get_confirmation_message(self):
        return self.confirmation_message.inner_text()
        

    def get_booking_dates_text(self):
        return self.page.inner_text("p.text-center.pt-2 strong")