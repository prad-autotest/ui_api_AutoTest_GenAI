from pages.web.base_page import BasePage
import logging

class ContactUsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)
        self.contact_form_link = "a[href='/contact_us']"
        self.name_input = "input[data-qa='name']"
        self.email_input = "input[data-qa='email']"
        self.subject_input = "input[data-qa='subject']"
        self.message_textarea = "textarea[data-qa='message']"
        self.upload_input = "input[name='upload_file']"
        self.submit_button = "input[data-qa='submit-button']"
        self.success_message = "div.status.alert.alert-success"
        self.error_message = "form#contact-us-form .form-group.has-error"

    def navigate_to_contact_form(self):
        self.logger.info("Navigating to Contact Us form")
        self.page.click(self.contact_form_link)

    def fill_contact_form(self, name, email, subject, message, file_path=None):
        self.logger.info("Filling contact form")
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)
        self.page.fill(self.subject_input, subject)
        self.page.fill(self.message_textarea, message)
        if file_path:
            self.logger.info(f"Uploading file: {file_path}")
            self.page.set_input_files(self.upload_input, file_path)

    def submit_form(self):
        self.logger.info("Submitting the contact form")
        self.page.click(self.submit_button)
        self.page.on("dialog", lambda dialog: dialog.accept())  # Accept success dialog

    def get_success_message(self):
        if self.page.locator(self.success_message).is_visible():
            msg = self.page.locator(self.success_message).inner_text()
            self.logger.info(f"Success message: {msg}")
            return msg
        return None

    def is_validation_error_visible(self):
        return self.page.locator(self.error_message).is_visible()
