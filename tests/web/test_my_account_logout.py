import pytest
import allure
from pages.web.home_page import HomePage
from pages.web.login_signup_page import LoginSignupPage
from pages.web.my_account_page import MyAccountPage
from utils.helpers import CONFIG
from playwright.sync_api import sync_playwright

@allure.epic("Web UI Tests")
@allure.feature("My Account & Logout")
@pytest.fixture(scope="function")
def setup_logged_in():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        home = HomePage(page)
        login_page = LoginSignupPage(page)
        my_account = MyAccountPage(page)

        home.visit(CONFIG['base_url'])
        home.go_to_login_signup()
        login_page.login("automationtestuser@gmail.com", "automation123")
        yield home, my_account, page
        browser.close()

@allure.story("Account Info")
@allure.title("Verify My Account page after login")
def test_account_info_visible(setup_logged_in):
    home, my_account, page = setup_logged_in
    with allure.step("Check 'Logged in as' is visible"):
        assert home.is_logged_in("automationtestuser")
    with allure.step("Navigate to My Account section and verify details"):
        page.click("a[href='/account_created']")  # or account if available
        assert my_account.is_account_info_visible()

@allure.story("Logout Flow")
@allure.title("Logout after login and verify redirect")
def test_logout_functionality(setup_logged_in):
    home, my_account, page = setup_logged_in
    with allure.step("Trigger logout action"):
        my_account.logout()
    with allure.step("Verify redirect to login or homepage"):
        assert "/login" in page.url or "Login" in page.inner_text("body")

@allure.story("Logout without Login")
@allure.title("Attempt to logout without being logged in")
def test_logout_without_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        home = HomePage(page)

        home.visit(CONFIG['base_url'])
        home.logout()
        with allure.step("Check if redirected to login"):
            assert "/login" in page.url or "Login" in page.inner_text("body")
        browser.close()
