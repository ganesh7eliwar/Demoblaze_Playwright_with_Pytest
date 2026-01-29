from playwright.sync_api import expect
from page_objects.login_page import LoginPage
from utilities.config import Config


def test_login(page):

    login_page = LoginPage(page)
    login_page.click_on_login_link()
    login_page.enter_username(Config.email)
    login_page.enter_password(Config.password)
    login_page.click_on_login_button()

    expect(login_page.user_name).to_be_visible()
