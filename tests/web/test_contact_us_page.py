import pytest
import allure
from pages.web.home_page import HomePage
from pages.web.contact_us_page import ContactUsPage
from utils.helpers import CONFIG
from pathlib import Path
from playwright.sync_api import sync_playwright

@allure.epic("Web UI Tests")
@allure.feature("Contact Us Page")
@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        home = HomePage(page)
        contact = ContactUsPage(page)
        home.visit(CONFIG['base_url'])
        home.go_to_contact_us()
        yield contact, page
        browser.close()

@allure.story("Valid Contact Submission")
@allure.title("Submit valid contact form with file upload")
def test_valid_contact_form_with_file(setup):
    contact, page = setup
    with allure.step("Fill contact form with valid data and file"):
        file_path = str(Path("test_data/sample_upload.txt").resolve())
        contact.fill_contact_form(
            name="Test User",
            email="test@mail.com",
            subject="Inquiry",
            message="This is a test message.",
            file_path=file_path
        )
    with allure.step("Submit form and verify success"):
        contact.submit_form()
        assert "Success" in contact.get_success_message()

@allure.story("Form Validation")
@allure.title("Submit contact form with missing required fields")
def test_contact_form_validation_errors(setup):
    contact, page = setup
    with allure.step("Fill contact form with empty email"):
        contact.fill_contact_form(
            name="",
            email="",
            subject="",
            message=""
        )
    with allure.step("Try to submit form and expect validation error"):
        contact.submit_form()
        assert contact.is_validation_error_visible()

@allure.story("Contact Form Basic")
@allure.title("Submit form without file attachment")
def test_contact_form_without_file(setup):
    contact, page = setup
    with allure.step("Submit valid contact form without file"):
        contact.fill_contact_form(
            name="Simple User",
            email="simple@test.com",
            subject="No file test",
            message="Message without file."
        )
    with allure.step("Submit form and verify success message"):
        contact.submit_form()
        assert "Success" in contact.get_success_message()
