import pytest
import allure
from pages.web.products_page import ProductsPage
from pages.web.product_detail_page import ProductDetailPage
from utils.helpers import CONFIG
from playwright.sync_api import sync_playwright

@allure.epic("Web UI Tests")
@allure.feature("Product Detail Page")
@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        products = ProductsPage(page)
        details = ProductDetailPage(page)

        products.visit(CONFIG['base_url'] + "/products")
        products.open_product_by_index(0)
        yield details, page
        browser.close()

@allure.story("Product Info")
@allure.title("Validate product title and price are displayed")
def test_product_title_and_price(setup):
    details, page = setup
    with allure.step("Verify product name is visible"):
        name = details.get_product_name()
        assert name and len(name) > 2
    with allure.step("Verify product price is displayed"):
        price = details.get_product_price()
        assert "$" in price or "Rs." in price

@allure.story("Cart Interaction")
@allure.title("Add product with quantity to cart")
def test_add_product_to_cart(setup):
    details, page = setup
    with allure.step("Set quantity and add to cart"):
        details.set_quantity(3)
        details.add_to_cart()
    with allure.step("Verify cart modal or redirect"):
        assert "product" in page.url or "cart" in page.url

@allure.story("Review Submission")
@allure.title("Submit a review and verify success")
def test_submit_review_on_product(setup):
    details, page = setup
    with allure.step("Fill and submit review"):
        details.submit_review(
            name="Test User",
            email="test@mail.com",
            review_text="Awesome product!"
        )
    with allure.step("Verify review submission success"):
        assert details.is_review_success_message_displayed()
