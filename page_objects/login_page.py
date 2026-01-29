from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.login_link = self.page.locator('#login2')
        self.email_input = self.page.locator('#loginusername')
        self.password_input = self.page.locator('#loginpassword')
        self.login_btn = self.page.locator('button[onclick="logIn()"]')
        self.user_name = self.page.locator('#nameofuser')

    def click_on_login_link(self):
        try:
            self.login_link.click()
        except Exception as e:
            print(f'Exception while clicking on Login Link: {e}.')
            raise

    def enter_username(self, username):
        try:
            self.email_input.fill(username)
        except Exception as e:
            print(f'Exception while entering the User Name: {e}.')

    def enter_password(self, password):
        try:
            self.password_input.fill(password)
        except Exception as e:
            print(f'Exception while entering the Password: {e}.')

    def click_on_login_button(self):
        try:
            self.login_btn.click()
        except Exception as e:
            print(f'Exception while clicking on Login button: {e}.')

    def username(self):
        try:
            return self.user_name
        except Exception as e:
            print(f'Exception while looking for username: {e}.')

    def login(self, username, password):
        self.login_link.click()
        self.email_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()
