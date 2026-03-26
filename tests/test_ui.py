from datetime import date, timedelta
import time

# added varience to checkin and checkout dates to allow multiple tests in a row and avoidthe timeout issue.
def test_main_user_flow(booking_page):
    checkin = date.today() + timedelta(days=30 + (int(time.time()) % 30))
    checkout = checkin + timedelta(days=1)
    expected_dates_text = f"{checkin} - {checkout}"
    booking_page.navigate_to_booking_url(str(checkin), str(checkout))
    booking_page.click_reserve_now()
    booking_page.enter_user_information("Jon", "Smith", "thisisjonsmith@gmail.com", "16142222323")
    booking_page.confirm_booking()
    assert "Booking Confirmed" in booking_page.get_confirmation_message()
    assert expected_dates_text in booking_page.get_booking_dates_text()