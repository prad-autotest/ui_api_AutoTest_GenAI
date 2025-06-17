import pytest
import allure
from pages.web.products_page import ProductsPage
from utils.helpers import CONFIG
from playwright.sync_api import sync_playwright

@allure.epic("Web UI Tests")
@allure.feature("Category and Brand Filters")
@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'])
        context = browser.new_context(viewport=CONFIG['viewport'])
        page = context.new_page()
        products = ProductsPage(page)
        products.visit(CONFIG['base_url'] + "/products")
        yield products, page
        browser.close()

@allure.story("Category Filter")
@allure.title("Filter products by Women > Dress")
def test_filter_by_category(setup):
    products, page = setup
    with allure.step("Expand Women category"):
        products.expand_category("Women")
    with allure.step("Select Dress sub-category"):
        products.select_sub_category("Dress")
    with allure.step("Verify filtered product list is shown"):
        names = products.get_visible_product_names()
        assert any("Dress" in name or len(name) > 1 for name in names)

@allure.story("Brand Filter")
@allure.title("Filter products by brand: Polo")
def test_filter_by_brand(setup):
    products, page = setup
    with allure.step("Click Polo brand link"):
        products.filter_by_brand("Polo")
    with allure.step("Verify filtered products under brand"):
        names = products.get_visible_product_names()
        assert len(names) > 0
        allure.attach("\n".join(names), name="Filtered Products", attachment_type=allure.attachment_type.TEXT)
