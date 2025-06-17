from playwright.sync_api import Page
from utils.logger import get_logger
import logging

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)
        # self.logger = logging.getLogger(self.__class__.__name__)

    def visit(self, url):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def get_title(self):
        title = self.page.title()
        self.logger.info(f"Page title: {title}")
        return title

    def click(self, selector: str, timeout: int = 10000):
        self.page.locator(selector).click(timeout=timeout)

    def double_click(self, selector: str):
        self.page.locator(selector).dblclick()

    def type(self, selector: str, text: str, clear: bool = True):
        locator = self.page.locator(selector)
        if clear:
            locator.fill("")  # clear before typing
        locator.type(text)

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def press_key(self, selector: str, key: str):
        self.page.locator(selector).press(key)

    def hover(self, selector: str):
        self.page.locator(selector).hover()

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def wait_for_selector(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def upload_file(self, selector: str, file_path: str):
        self.page.set_input_files(selector, file_path)

    def select_option(self, selector: str, value: str):
        self.page.locator(selector).select_option(value)

    def scroll_into_view(self, selector: str):
        self.page.locator(selector).scroll_into_view_if_needed()

    def get_attribute(self, selector: str, attr: str) -> str:
        return self.page.locator(selector).get_attribute(attr)

    def assert_url_contains(self, text: str):
        assert text in self.page.url
