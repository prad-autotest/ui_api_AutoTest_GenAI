import allure
from apis.products_api import ProductsAPI

@allure.epic("API Tests")
@allure.feature("Products API")
@allure.severity(allure.severity_level.BLOCKER)
def test_get_all_products():
    api = ProductsAPI()
    with allure.step("Get all products"):
        response = api.get_all_products()
        assert response.status_code == 200
        assert "products" in response.json()
