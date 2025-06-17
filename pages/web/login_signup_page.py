from pages.web.base_page import BasePage
import logging

class LoginSignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)
        # Login Locators
        self.login_email_input = "[data-qa='login-email']"
        self.login_password_input = "[data-qa='login-password']"
        self.login_button = "[data-qa='login-button']"
        self.login_error_msg = "form[action='/login'] p"

        # Signup Locators
        self.signup_name_input = "[data-qa='signup-name']"
        self.signup_email_input = "[data-qa='signup-email']"
        self.signup_button = "[data-qa='signup-button']"
        self.signup_error_msg = "form[action='/signup'] p"

    def login(self, email, password):
        self.logger.info(f"Attempting login for user: {email}")
        self.page.fill(self.login_email_input, email)
        self.page.fill(self.login_password_input, password)
        self.page.click(self.login_button)

    def signup(self, name, email):
        self.logger.info(f"Attempting signup for user: {name}, {email}")
        self.page.fill(self.signup_name_input, name)
        self.page.fill(self.signup_email_input, email)
        self.page.click(self.signup_button)

    def get_login_error_message(self):
        if self.page.locator(self.login_error_msg).is_visible():
            msg = self.page.locator(self.login_error_msg).inner_text()
            self.logger.info(f"Login error message: {msg}")
            return msg
        return None

    def get_signup_error_message(self):
        if self.page.locator(self.signup_error_msg).is_visible():
            msg = self.page.locator(self.signup_error_msg).inner_text()
            self.logger.info(f"Signup error message: {msg}")
            return msg
        return None
