import allure
from pages.base_page import BasePage
from locators.main_page_locators import main_page_header, create_recipes_link, exit_button, singin_button

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_main_page(self):
        self.wait_for_load_element(main_page_header)

    @allure.step('Кликаем на Создать рецепт')
    def click_create_recipes_link(self):
        self.click_page_element(create_recipes_link)

    @allure.step('Кликаем на Выход')
    def click_exit_button(self):
        self.click_page_element(exit_button)

    @allure.step('Кликаем на Войти')
    def click_singin_button(self):
        self.click_page_element(singin_button)

    @allure.step('Проверяем отображение кнопки Выход')
    def check_exit_button_visibility(self):
        return self.find_element(exit_button)
