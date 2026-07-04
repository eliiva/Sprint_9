import allure
from pages.signin_page import SigninPage
from pages.main_page import MainPage
from urls import main_page_url
from data import registered_user_data

class TestUserAuthorization:

    @allure.title('Проверка успешной авторизации пользователя')
    @allure.description('Заполняем все поля формы авторизации, нажимаем Войти и проверяем переход на главную')
    def test_user_authorization(self, driver):
        driver.get(main_page_url)

        main_page = MainPage(driver)
        main_page.click_singin_button()

        signin_page = SigninPage(driver)
        signin_page.wait_for_load_singin_page()
        signin_page.fill_email_input(registered_user_data['username'])
        signin_page.fill_password_input(registered_user_data['password'])
        signin_page.click_signin_button()

        assert signin_page.wait_for_url_change_to(main_page_url)
        assert main_page.check_exit_button_visibility()
