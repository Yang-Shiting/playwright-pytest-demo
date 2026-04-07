import pytest
from playwright.sync_api import Page, expect

def test_login_success(page: Page):
    # 1. 打开新网站的登录页面
    page.goto("https://practice.expandtesting.com/login")
    
    # 2. 输入正确的用户名
    page.fill('#username', 'practice')
    
    # 3. 输入正确的密码
    page.fill('#password', 'SuperSecretPassword!')
    
    # 4. 点击登录按钮
    page.click('button[type="submit"]')
    
    # 5. 检查是否跳转到了安全页面（URL包含secure）
    expect(page).to_have_url("https://practice.expandtesting.com/secure")
    
    # 6. 检查页面上是否显示了“登录成功”的提示
    expect(page.locator('div.alert.alert-success')).to_be_visible()