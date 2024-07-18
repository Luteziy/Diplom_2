import requests
import allure
import pytest
from data import Data, DataUsers
from helpers import create_random_email, create_random_password, create_random_name

class TestLoginUser: #++
    @allure.title('Логин под существующим пользователем')
    @allure.description('Проверка кода 200 и текста ответа')
    def test_login_as_exist_user(self):
        payload = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_name()
        }
        requests.post(Data.Url_create_and_registrate_user, data=payload)
        response = requests.post(Data.Url_auth_login, data=payload)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Вход с неверным логином и паролем.')
    @allure.description('Проверка кода 401 и текста ответа')
    @pytest.mark.parametrize('wrong', [
        {'email': DataUsers.wrong_email, 'password': create_random_password()},
        {'email': create_random_email(), 'password': DataUsers.incorrect_password}
    ])
    def test_wrong_login_or_password(self, wrong):
        response = requests.post(Data.Url_auth_login, data=wrong)
        assert response.status_code == 401 and response.json() == {"success": False, "message": "email or password are incorrect"}