import pytest
import allure
from pages.web.home_page import HomePage
from pages.web.login_signup_page import LoginSignupPage
from utils.helpers import CONFIG
from playwright.sync_api import sync_playwright
import uuid

@allure.epic("Web UI Tests")
@allure.feature("Login/Signup Page")
@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        home = HomePage(page)
        login_page = LoginSignupPage(page)
        home.visit(CONFIG['base_url'])
        home.go_to_login_signup()
        yield login_page, page
        browser.close()

@allure.story("Login")
@allure.title("Login with invalid credentials")
def test_invalid_login(setup):
    login_page, page = setup
    with allure.step("Attempt login with incorrect credentials"):
        login_page.login("invalid@example.com", "wrongpass")
    with allure.step("Verify login error message is shown"):
        error = login_page.get_login_error_message()
        assert error is not None
        assert "incorrect" in error.lower()

@allure.story("Signup")
@allure.title("Signup with existing email")
def test_signup_existing_email(setup):
    login_page, page = setup
    with allure.step("Attempt signup with existing email"):
        login_page.signup("Existing User", "automationtestuser@gmail.com")
    with allure.step("Verify signup error message is shown"):
        error = login_page.get_signup_error_message()
        assert error is not None
        assert "already exist" in error.lower()

@allure.story("Signup")
@allure.title("Signup with new unique email")
def test_signup_with_new_email(setup):
    login_page, page = setup
    unique_email = f"testuser_{uuid.uuid4().hex[:6]}@mailinator.com"
    with allure.step(f"Attempt signup with new email: {unique_email}"):
        login_page.signup("New User", unique_email)
    with allure.step("Verify redirected to account info form or next step"):
        assert "/signup" in page.url or "Enter Account Information" in page.inner_text("body")
