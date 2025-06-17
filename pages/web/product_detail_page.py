from pages.web.base_page import BasePage
import logging

class ProductDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_name = "div.product-information h2"
        self.product_price = "div.product-information span span"
        self.quantity_input = "#quantity"
        self.add_to_cart_button = "button.cart"
        self.review_name = "#name"
        self.review_email = "#email"
        self.review_content = "#review"
        self.review_submit = "#button-review"
        self.review_success_msg = "div#review-section .alert-success"
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_product_name(self):
        name = self.page.locator(self.product_name).inner_text()
        self.logger.info(f"Product name: {name}")
        return name

    def get_product_price(self):
        price = self.page.locator(self.product_price).inner_text()
        self.logger.info(f"Product price: {price}")
        return price

    def set_quantity(self, qty: int):
        self.logger.info(f"Setting quantity to {qty}")
        self.page.fill(self.quantity_input, str(qty))

    def add_to_cart(self):
        self.logger.info("Clicking Add to Cart")
        self.page.click(self.add_to_cart_button)

    def submit_review(self, name, email, review_text):
        self.logger.info("Submitting review")
        self.page.fill(self.review_name, name)
        self.page.fill(self.review_email, email)
        self.page.fill(self.review_content, review_text)
        self.page.click(self.review_submit)

    def is_review_success_message_displayed(self):
        visible = self.page.locator(self.review_success_msg).is_visible()
        self.logger.info(f"Review success visible: {visible}")
        return visible

