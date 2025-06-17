from pages.web.base_page import BasePage
import logging

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logo_selector = "img[alt='Website for automation practice']"
        self.products_link = "a[href='/products']"
        self.login_link = "a[href='/login']"
        self.cart_link = "a[href='/view_cart']"
        self.contact_us = "a[href='/contact_us']"
        self.logout_link = "a[href='/logout']"
        self.logged_in_user = "li:has-text('Logged in as')"
        self.recommended_section = "#recommended-items"
        self.recommended_products = "#recommended-item-carousel .productinfo.text-center"
        self.recommended_add_to_cart_btn = "#recommended-item-carousel .productinfo.text-center >> text=Add to cart"

    def is_logo_displayed(self):
        visible = self.page.locator(self.logo_selector).is_visible()
        self.logger.info(f"Logo displayed: {visible}")
        return visible

    def go_to_products(self):
        self.logger.info("Clicking on Products link")
        self.page.click(self.products_link)

    def go_to_login_signup(self):
        self.logger.info("Navigating to Login/Signup page")
        self.page.click(self.login_link)

    def go_to_cart(self):
        self.logger.info("Navigating to Cart")
        self.page.click(self.cart_link)

    def go_to_contact_us(self):
        self.logger.info("Navigating to Contact Us page")
        self.page.click(self.contact_us)

    def is_logged_in(self, username):
        return self.page.locator(self.logged_in_user).inner_text().lower().__contains__(username.lower())

    def logout(self):
        self.logger.info("Clicking Logout from HomePage")
        self.page.click(self.logout_link)

    def open_product_by_index(self, index=0):
        self.logger.info(f"Opening product at index {index}")
        self.page.locator("a[href^='/product_details/']").nth(index).click()

    def scroll_to_recommended_items(self):
        self.logger.info("Scrolling to Recommended Items section")
        self.page.locator(self.recommended_section).scroll_into_view_if_needed()

    def is_recommended_section_visible(self):
        return self.page.locator(self.recommended_section).is_visible()

    def add_first_recommended_product_to_cart(self):
        self.logger.info("Adding first recommended product to cart")
        self.page.locator(self.recommended_add_to_cart_btn).first.click()
