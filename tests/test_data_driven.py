# tests/test_data_driven.py
import pytest
import json
import os
from pages.login_page import LoginPage

def load_data():
    # 找到 data/test_data.json 的路径
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_data.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

class TestDataDriven:
    @pytest.mark.parametrize("user", load_data()["valid_users"])
    def test_valid_users(self, page, user):
        login_page = LoginPage(page)
        secure_page = login_page.login(user["username"], user["password"])
        secure_page.verify_login_success()

    @pytest.mark.parametrize("user", load_data()["invalid_users"])
    def test_invalid_users(self, page, user):
        login_page = LoginPage(page)
        login_page.open()
        login_page.enter_username(user["username"])
        login_page.enter_password(user["password"])
        login_page.click_login()
        assert user["expected"] in login_page.get_error_message()