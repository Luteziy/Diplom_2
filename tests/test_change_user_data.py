import requests
import allure
from data import Data
from helpers import create_random_email, create_random_password, create_random_name


class TestChangeUserData:
    @allure.title('Изменение данных пользователя: с авторизацией')
    @allure.description('Проверка кода 200 и текста ответа')
    def test_change_user_data(self, create_user_delete_user):
        new_user = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_name()
        }
        response = requests.patch(Data.Url_user_update_data, headers={'Authorization': create_user_delete_user[1]['accessToken']}, data=new_user)
        assert response.status_code == 200 and response.json()["success"] is True


    @allure.title('Изменение данных пользователя: без авторизации')
    @allure.description('Проверка кода 401 и текста ответа')
    def test_change_user_data_no_auth(self):
        new_user = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_name()
        }
        response = requests.patch(Data.Url_user_update_data, data=new_user)
        assert response.status_code == 401 and response.json() == {"success": False, "message": "You should be authorised"}