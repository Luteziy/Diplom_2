import requests
import allure
import pytest
from data import Data, Ingredients, BurgerIngred


class TestCreateOrders:

    @allure.title('Создание заказа: с авторизацией и с ингредиентами')
    @allure.description('Проверка кода 200 и текста ответа')
    def test_create_order_loged_in(self, create_user_delete_user):
        headers = {'Authorization': create_user_delete_user[1]['accessToken']}
        burg = {'ingredients': [BurgerIngred.burg_0]}
        response = requests.post(Data.Url_create_order, data=burg, headers=headers)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание заказа: без авторизации')
    @allure.description('Проверка кода 400')
    def test_create_order_without_login(self):
        burg = {'ingredients': [BurgerIngred.burg_0]}
        response = requests.post(Data.Url_create_order, data=burg, headers=Data.headers)
        assert response.status_code == 400

    @allure.title('Создание заказа: без ингредиентов')
    @allure.description('Проверка кода 400 и текста ответа')
    def test_create_order_without_ingredients(self, create_user_delete_user):
        headers = {'Authorization': create_user_delete_user[1]['accessToken']}
        burg = {'ingredients': []}
        response = requests.post(Data.Url_create_order, data=burg, headers=headers)
        assert response.status_code == 400 and response.json() == {"success": False, "message": "Ingredient ids must be provided"}

    @allure.title('Создание заказа: с неверным хешем ингредиентов')
    @allure.description('Проверка кода 500')
    def test_create_order_with_wrong_ingredients_name(self, create_user_delete_user):
        headers = {'Authorization': create_user_delete_user[1]['accessToken']}
        burg = {'ingredients': [BurgerIngred.wrong]}
        response = requests.post(Data.Url_create_order, data=burg, headers=headers)
        assert response.status_code == 500