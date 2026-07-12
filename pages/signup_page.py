import allure
from pages.base_page import BasePage
from locators.signup_page_locators import create_account_button, signup_page_header, email_input, password_input, last_name_input, first_name_input, username_input

class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_singup_page(self):
        self.wait_for_load_element(signup_page_header)

    @allure.step('Кликаем на Создать аккаунт')
    def click_create_account_button(self):
        self.click_page_element(create_account_button)

    @allure.step('Заполняем имя')
    def fill_first_name_input(self, first_name):
        self.fill_input(first_name_input, first_name)

    @allure.step('Заполняем фамилию')
    def fill_last_name_input(self, last_name):
        self.fill_input(last_name_input, last_name)

    @allure.step('Заполняем имя пользователя')
    def fill_username_input(self, username):
        self.fill_input(username_input, username)

    @allure.step('Заполняем имейл')
    def fill_email_input(self, email):
        self.fill_input(email_input, email)

    @allure.step('Заполняем пароль')
    def fill_password_input(self, password):
        self.fill_input(password_input, password)
