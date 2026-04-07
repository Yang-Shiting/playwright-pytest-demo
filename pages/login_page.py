# pages/login_page.py
from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    # 定义页面上各个元素的特征（选择器）
    USERNAME_INPUT = '#username'          # 用户名输入框
    PASSWORD_INPUT = '#password'          # 密码输入框
    LOGIN_BUTTON = 'button[type="submit"]' # 登录按钮
    ERROR_MESSAGE = 'div.alert.alert-danger'   # 错误提示
    SUCCESS_MESSAGE = 'div.alert.alert-success' # 成功提示

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        """打开登录页"""
        self.navigate_to("https://practice.expandtesting.com/login")
        return self

    def enter_username(self, username: str):
        self.fill_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        self.fill_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        # 登录成功后跳转到安全页面，所以我们返回一个 SecurePage 对象
        from pages.secure_page import SecurePage
        return SecurePage(self.page)

    def login(self, username: str, password: str):
        """一步完成登录操作"""
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)