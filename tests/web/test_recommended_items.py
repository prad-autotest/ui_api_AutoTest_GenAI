import pytest
import allure
from pages.web.home_page import HomePage
from utils.helpers import CONFIG
from playwright.sync_api import sync_playwright

@allure.epic("Web UI Tests")
@allure.feature("Recommended Items Section")
@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        home = HomePage(page)
        home.visit(CONFIG['base_url'])
        yield home, page
        browser.close()

@allure.story("Visibility")
@allure.title("Check that Recommended Items section is displayed")
def test_recommended_section_display(setup):
    home, page = setup
    with allure.step("Scroll to recommended section"):
        home.scroll_to_recommended_items()
    with allure.step("Verify visibility of recommended items"):
        assert home.is_recommended_section_visible()

@allure.story("Cart Integration")
@allure.title("Add a recommended item to cart")
def test_add_recommended_product_to_cart(setup):
    home, page = setup
    with allure.step("Scroll to recommended section"):
        home.scroll_to_recommended_items()
    with allure.step("Click Add to Cart for first recommended item"):
        home.add_first_recommended_product_to_cart()
    with allure.step("Wait for modal or cart update"):
        page.wait_for_timeout(2000)  # Ideally replace with modal wait
        assert "cart" in page.url or "Continue Shopping" in page.content()
