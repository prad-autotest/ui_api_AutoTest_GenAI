import pytest
import allure
from pages.web.home_page import HomePage
from utils.helpers import CONFIG
from playwright.sync_api import sync_playwright

@allure.epic("Web UI Tests")
@allure.feature("Home Page")
@allure.severity(allure.severity_level.CRITICAL)
def test_home_page_logo_display():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        home = HomePage(page)

        home.visit(CONFIG['base_url'])

        with allure.step("Check if logo is displayed"):
            assert home.is_logo_displayed() is True

        browser.close()
