from pages.web.base_page import BasePage
import logging

class MyAccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)
        self.account_info_label = "h2:has-text('Account Information')"
        self.logged_in_as = "li:has-text('Logged in as')"
        self.logout_link = "a[href='/logout']"

    def is_account_info_visible(self):
        self.logger.info("Checking if Account Information is visible")
        return self.page.locator(self.account_info_label).is_visible()

    def is_logged_in_as_displayed(self, username):
        text = self.page.locator(self.logged_in_as).inner_text()
        self.logger.info(f"'Logged in as' text: {text}")
        return username.lower() in text.lower()

    def logout(self):
        self.logger.info("Clicking logout")
        self.page.click(self.logout_link)

