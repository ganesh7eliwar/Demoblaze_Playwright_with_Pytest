from playwright.sync_api import expect
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.cart_page import CartPage
from utilities.config import Config


def test_login_and_add_product_to_cart(page):

    login_page = LoginPage(page)
    home_page = HomePage(page)
    cart_page = CartPage(page)

    # Login Page
    login_page.click_on_login_link()
    login_page.enter_username(Config.email)
    login_page.enter_password(Config.password)
    login_page.click_on_login_button()

    # Home Page
    home_page.add_product(Config.product_name)
    page.wait_for_timeout(3000)
    home_page.goto_cart()
    page.wait_for_timeout(3000)

    # Cart Page
    product_in_cart = cart_page.verify_item(Config.product_name)

    # Assertion
    expect(product_in_cart).to_be_visible()
