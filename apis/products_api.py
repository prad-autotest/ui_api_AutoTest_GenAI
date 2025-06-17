import requests
from utils.helpers import CONFIG
from utils.logger import get_logger

class ProductsAPI:
    def __init__(self):
        self.base_url = CONFIG['api_base_url']
        self.logger = get_logger("ProductsAPI")

    def get_all_products(self):
        url = f"{self.base_url}/productsList"
        self.logger.info(f"GET {url}")
        response = requests.get(url)
        return response
