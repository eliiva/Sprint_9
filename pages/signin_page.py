import allure
from pages.base_page import BasePage
from locators.signin_page_locators import create_account_button, signin_page_header, email_input, password_input, signin_button, singin_form
from data import registered_user_data

class SigninPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_singin_page(self):
        self.wait_for_load_element(signin_page_header)

    @allure.step('Кликаем на Создать аккаунт')
    def click_create_account_button(self):
        self.click_page_element(create_account_button)

    @allure.step('Кликаем на Войти')
    def click_signin_button(self):
        self.click_page_element(signin_button)

    @allure.step('Заполняем имейл')
    def fill_email_input(self, email):
        self.fill_input(email_input, email)

    @allure.step('Заполняем пароль')
    def fill_password_input(self, password):
        self.fill_input(password_input, password)

    @allure.step('Дожидаемся отображения формы')
    def wait_form_visibility(self):
        return self.wait_for_visibility_of_element(singin_form)

    @allure.step('Входим зарегистрированным пользователем')
    def singing_registered_user(self):
        self.fill_email_input(registered_user_data['username'])
        self.fill_password_input(registered_user_data['password'])
        self.click_signin_button()
