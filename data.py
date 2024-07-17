class Data:
    Url_main_page = 'https://stellarburgers.nomoreparties.site'
    Url_create_user = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    Url_registration = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    Url_auth_login = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    Url_user_update_data = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    Url_create_order = 'https://stellarburgers.nomoreparties.site/api/orders'
    Url_get_orders = 'https://stellarburgers.nomoreparties.site/api/orders'
    Url_log_out = 'https://stellarburgers.nomoreparties.site/api/auth/logout'
    Url_delete_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    headers = {'Content-Type': 'application/json'}

class DataUsers:
    email = 'akuz_6@gmail.com'
    password = 'akuznetsova'
    incorrect_password = 'aKuzn'
    name = 'Анастасия'
    wrong_email = 'asa'

class Ingredients:
    Burger = {"ingredients": ['61c0c5a71d1f82001bdaaa6d','609646e4dc916e00276b2870']}
    Empty_burger = {'ingredients': ''}
    Wrong_burger = {'ingredients': ['61c0c5a71d1f82001bdaaa', '61c0c5a71d1f82001']}

class BurgerIngred:
    burg_0 = ['61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6c',
              '61c0c5a71d1f82001bdaaa77', '61c0c5a71d1f82001bdaaa79']
    burg_1 = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6d',
              '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa7a']
    wrong = '61c0c5a71d1f82001bdaaa'