# tests/test_login.py
import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_valid_login(self, page):
        login_page = LoginPage(page)
        secure_page = login_page.login("practice", "SuperSecretPassword!")
        secure_page.verify_login_success()

    def test_invalid_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.enter_username("wrong_user")
        login_page.enter_password("wrong_password")
        login_page.click_login()
        
        # 应该出现错误提示
        error = login_page.get_error_message()
        assert "Your username is invalid!" in error