

def test_main_user_flow(booking_page):
    booking_page.navigate_to_booking_url()
    booking_page.click_reserve_now()
    booking_page.enter_user_information("Jon", "Smith", "thisisjonsmith@gmail.com", "16142222323")
    booking_page.confirm_booking()
   # assert "Booking Confirmed" in booking_page.get_confirmation_message()
    assert "2026-04-15 - 2026-04-16" in booking_page.get_booking_dates_text()
