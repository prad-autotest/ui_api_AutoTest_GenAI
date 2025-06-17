import pytest
import allure
from pages.web.home_page import HomePage
from pages.web.products_page import ProductsPage
from utils.helpers import CONFIG
from playwright.sync_api import sync_playwright

@allure.epic("Web UI Tests")
@allure.feature("Products Page")
@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        home = HomePage(page)
        products = ProductsPage(page)
        home.visit(CONFIG['base_url'])
        home.go_to_products()
        yield products, page
        browser.close()

@allure.story("Search functionality")
@allure.title("Search for an existing product")
def test_search_valid_product(setup):
    products, page = setup
    with allure.step("Search for 'Jeans'"):
        products.search_product("Jeans")
    with allure.step("Verify results are displayed"):
        assert products.get_search_results_count() > 0

@allure.story("Search functionality")
@allure.title("Search for an invalid product")
def test_search_invalid_product(setup):
    products, page = setup
    with allure.step("Search for 'invalidProduct123'"):
        products.search_product("invalidProduct123")
    with allure.step("Verify no products found"):
        assert products.get_search_results_count() == 0

@allure.story("Product View")
@allure.title("View product details page from listing")
def test_view_product_details(setup):
    products, page = setup
    with allure.step("Click on first product's View Product button"):
        products.click_view_product_by_index(0)
    with allure.step("Check product details page opened"):
        assert "product_details" in page.url

@allure.story("Category filter")
@allure.title("Filter products by category")
def test_filter_by_category(setup):
    products, page = setup
    with allure.step("Select 'Women > Dress' category"):
        products.select_category_by_name("Women")
    with allure.step("Verify filtered products loaded"):
        assert products.get_search_results_count() > 0

@allure.story("Brand filter")
@allure.title("Filter products by brand")
def test_filter_by_brand(setup):
    products, page = setup
    with allure.step("Select 'Polo' brand"):
        products.select_brand_by_name("Polo")
    with allure.step("Verify brand filtered results"):
        assert products.get_search_results_count() > 0
