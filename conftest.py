import allure
import pytest
import requests
from data import Data, BurgerIngred
from helpers import create_random_name, create_random_password, create_random_email

@pytest.fixture
@allure.title('Создаем фикстуру с генерацией юзера и последующим его удалением')
def create_user_delete_user():
    new_user = {
        'name': create_random_name(),
        'password': create_random_password(),
        'email': create_random_email()
    }
    response = requests.post(Data.Url_create_and_registrate_user, data=new_user)
    response_body = response.json()

    yield new_user, response_body

    token = response_body['accessToken']
    requests.delete(Data.Url_delete_user, headers={'Authorization': token})

@pytest.fixture
@allure.title('Фикстура создает пользователя и заказ')
def create_user_and_order_and_delete(create_user_delete_user):
    access_token = create_user_delete_user[1]['accessToken']
    headers = {'Authorization': access_token}
    ingredients = {'ingredients': [BurgerIngred.burg_1]}
    response_body = requests.post(Data.Url_create_and_get_order, data=ingredients, headers=headers)
    yield access_token, response_body