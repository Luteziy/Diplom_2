import requests
import allure
import pytest
from data import Data
from helpers import create_random_email, create_random_password, create_random_name

class TestCreateUser: #++

    @allure.title('Проверка создания уникального пользователя')
    def test_create_new_user_account(self):
        new_user = {
        'name': create_random_name(),
        'password': create_random_password(),
        'email': create_random_email()
    }
        response = requests.post(Data.Url_create_user, data=new_user)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Проверка создания пользователя, который уже зарегестрировался')
    @allure.description('Проверка кода 403 и текста ответа')
    def test_create_exists_user(self):
        new_user = {
            'name': create_random_name(),
            'password': create_random_password(),
            'email': create_random_email()
        }
        requests.post(Data.Url_create_user, data=new_user)
        response = requests.post(Data.Url_create_user, data=new_user)
        assert response.status_code == 403 and response.json() == {"success": False, "message": "User already exists"}

    @allure.title('Проверка создания пользователя и не заполнить одно из обязательных полей.')
    @allure.description('Проверка кода 403 и текста ответа')
    @pytest.mark.parametrize('empty_fiel', [
        {'email': '', 'password': create_random_password(), 'name': create_random_name()},
        {'email': create_random_email(), 'password': '', 'name': create_random_name()},
        {'email': create_random_email(), 'password': create_random_password(), 'name': ''}
    ])
    def test_create_user_account_with_empty_field(self, empty_fiel):
        response = requests.post(Data.Url_create_user, data=empty_fiel)
        assert response.status_code == 403 and response.json() == {"success": False, "message": "Email, password and name are required fields"}

    @classmethod
    def teardown_class(cls):
        cls.response = requests.delete(Data.Url_delete_user)