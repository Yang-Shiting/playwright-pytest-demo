# pages/secure_page.py
from pages.base_page import BasePage
from playwright.sync_api import expect

class SecurePage(BasePage):
    SUCCESS_MESSAGE = 'div.alert.alert-success'
    LOGOUT_BUTTON = 'a:has-text("Logout")'

    def verify_login_success(self):
        """确认登录成功提示显示正常"""
        expect(self.page.locator(self.SUCCESS_MESSAGE)).to_be_visible()
        expect(self.page.locator(self.SUCCESS_MESSAGE)).to_contain_text("You logged into a secure area!")
        return self

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)
        from pages.login_page import LoginPage
        return LoginPage(self.page)