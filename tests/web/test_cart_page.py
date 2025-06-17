import pytest
import allure
from pages.web.home_page import HomePage
from pages.web.products_page import ProductsPage
from pages.web.cart_page import CartPage
from utils.helpers import CONFIG
from playwright.sync_api import sync_playwright

@allure.epic("Web UI Tests")
@allure.feature("Cart Page")
@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        home = HomePage(page)
        products = ProductsPage(page)
        cart = CartPage(page)

        # Navigate to base
        home.visit(CONFIG['base_url'])

        # Add a product to cart
        home.go_to_products()
        page.hover(".features_items .product-image-wrapper:nth-child(1)")
        page.click(".features_items .product-overlay a[title='Add to cart']")
        page.click("a[href='/view_cart']")  # direct to cart after modal

        yield cart, page
        browser.close()

@allure.story("Cart Functionality")
@allure.title("Verify product added to cart")
def test_cart_has_item(setup):
    cart, page = setup
    with allure.step("Verify at least one item is in the cart"):
        assert cart.get_cart_items_count() >= 1

@allure.story("Cart Functionality")
@allure.title("Remove product from cart")
def test_remove_item_from_cart(setup):
    cart, page = setup
    with allure.step("Remove first item from cart"):
        cart.delete_first_item()
        page.wait_for_timeout(2000)  # Wait for DOM update
        assert cart.get_cart_items_count() == 0

@allure.story("Cart Functionality")
@allure.title("Proceed to checkout from cart")
def test_proceed_to_checkout(setup):
    cart, page = setup
    with allure.step("Click on Proceed to Checkout"):
        cart.proceed_to_checkout_click()
    with allure.step("Verify navigated to login/checkout page"):
        assert "checkout" in page.url or "login" in page.url
