import allure
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from urls import signin_page_url
from helpers import generate_new_user_data

class TestCreateAccount:

    @allure.title('Проверка успешного создания аккаунта')
    @allure.description('Заполняем все поля формы, нажимаем Создать аккаунт и проверяем переход на страницу авторизации')
    def test_create_account(self, driver):
        new_user = generate_new_user_data()
        driver.get(signin_page_url)

        signin_page = SigninPage(driver)
        signin_page.click_create_account_button()
        
        singup_page = SignupPage(driver)
        singup_page.wait_for_load_singup_page()
        singup_page.fill_first_name_input(new_user['first_name'])
        singup_page.fill_last_name_input(new_user['last_name'])
        singup_page.fill_username_input(new_user['username'])
        singup_page.fill_email_input(new_user['email'])
        singup_page.fill_password_input(new_user['password'])
        singup_page.click_create_account_button()

        assert singup_page.wait_for_url_change_to(signin_page_url)
        assert signin_page.wait_form_visibility()
