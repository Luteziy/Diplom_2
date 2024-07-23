import requests
import allure
import pytest
from data import Data


class TestGetOrders: #++

    @allure.title('Получение заказов конкретного пользователя: авторизованный пользователь')
    @allure.description('Код ответа 200')
    def test_get_user_orders(self, create_user_and_order_and_delete):
        headers = {"Authorization": create_user_and_order_and_delete[0]}
        response = requests.get(Data.Url_create_and_get_order, headers=headers)
        assert response.status_code == 200 and response.json()["success"] is True
    @allure.title('Получение заказов конкретного пользователя: неавторизованный пользователь')
    @allure.description('Код ответа 401, текст: "You should be authorised"')
    def test_get_not_authorizate_user_orders(self):
        response = requests.get(Data.Url_create_and_get_order, headers=Data.headers)
        assert response.status_code == 401 and response.json() == {"success": False, "message": "You should be authorised" }