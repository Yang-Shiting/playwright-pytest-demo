# pages/base_page.py
from playwright.sync_api import Page, expect
import allure

class BasePage:
    """所有页面都会继承这个类，里面放通用操作，比如点击、输入文字等"""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        """打开网址"""
        self.page.goto(url)

    def click(self, selector: str):
        """点击某个元素"""
        self.page.click(selector)

    def fill_text(self, selector: str, text: str):
        """在输入框里填入文字"""
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """获取元素的文字内容"""
        return self.page.text_content(selector)

    def take_screenshot(self, name: str):
        """截图并保存（用于报告）"""
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)