from pages.web.base_page import BasePage
import logging

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)
        self.cart_items = "tr.cart_product"
        self.delete_buttons = "a.cart_quantity_delete"
        self.proceed_to_checkout = ".check_out"

    def get_cart_items_count(self):
        count = self.page.locator(self.cart_items).count()
        self.logger.info(f"Cart contains {count} items")
        return count

    def delete_first_item(self):
        self.logger.info("Deleting first item from cart")
        if self.page.locator(self.delete_buttons).count() > 0:
            self.page.locator(self.delete_buttons).nth(0).click()

    def proceed_to_checkout_click(self):
        self.logger.info("Clicking Proceed to Checkout")
        self.page.locator(self.proceed_to_checkout).click()
