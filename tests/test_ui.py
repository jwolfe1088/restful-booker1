import pytest

def test_main_user_flow(booking_page):
    booking_page.navigate_to_home()