from pages.web.base_page import BasePage
import logging

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_box = "input#search_product"
        self.search_button = "button#submit_search"
        self.product_list = ".features_items .product-image-wrapper"
        self.add_to_cart_buttons = ".product-overlay a[title='Add to cart']"
        self.view_product_links = ".productinfo.text-center p ~ a"
        self.category_sidebar = ".panel-group .panel-title a"
        self.brand_sidebar = ".brands-name a"
        self.logger = logging.getLogger(self.__class__.__name__)

        self.products_header = "h2.title.text-center"
        self.category_block = ".left-sidebar .panel-group.category-products"
        self.category_toggle = "//a[contains(text(),'Women')]"  # can parametrize later
        self.sub_category = "//a[contains(text(),'Dress')]"  # can parametrize later
        self.brand_section = ".brands_products"
        self.brand_filter = "//a[contains(text(),'Polo')]"
        self.filtered_product_names = ".features_items .productinfo.text-center p"

    def search_product(self, keyword):
        self.logger.info(f"Searching for product: {keyword}")
        self.page.fill(self.search_box, keyword)
        self.page.click(self.search_button)

    def get_search_results_count(self):
        count = self.page.locator(self.product_list).count()
        self.logger.info(f"Search result count: {count}")
        return count

    def click_view_product_by_index(self, index=0):
        self.logger.info(f"Clicking view product at index {index}")
        self.page.locator(self.view_product_links).nth(index).click()

    def select_category_by_name(self, category_name):
        self.logger.info(f"Selecting category: {category_name}")
        categories = self.page.locator(self.category_sidebar)
        count = categories.count()
        for i in range(count):
            if category_name.lower() in categories.nth(i).inner_text().lower():
                categories.nth(i).click()
                break

    def select_brand_by_name(self, brand_name):
        self.logger.info(f"Selecting brand: {brand_name}")
        brands = self.page.locator(self.brand_sidebar)
        count = brands.count()
        for i in range(count):
            if brand_name.lower() in brands.nth(i).inner_text().lower():
                brands.nth(i).click()
                break

    def expand_category(self, category_name):
        self.logger.info(f"Expanding category: {category_name}")
        self.page.locator(f"//a[contains(text(),'{category_name}')]").click()

    def select_sub_category(self, sub_cat_name):
        self.logger.info(f"Clicking sub-category: {sub_cat_name}")
        self.page.locator(f"//a[contains(text(),'{sub_cat_name}')]").click()

    def filter_by_brand(self, brand_name):
        self.logger.info(f"Filtering by brand: {brand_name}")
        self.page.locator(f"//a[contains(text(),'{brand_name}')]").click()

    def get_visible_product_names(self):
        names = self.page.locator(self.filtered_product_names).all_inner_texts()
        self.logger.info(f"Visible filtered products: {names}")
        return names

