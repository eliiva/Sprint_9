import allure
from pages.base_page import BasePage
from selenium.webdriver.remote.file_detector import LocalFileDetector
from locators.recipes_create_page_locators import recipes_create_page_header, recipes_name_input, ingredient_name_input, ingredient_amount_input, first_ingredient_in_list, add_ingredient_button, time_input, recipes_description_input, image_input, create_button, recipes_card, recipes_header

class RecipesCreatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_input_locator = image_input 

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_recipes_create_page(self):
        self.wait_for_load_element(recipes_create_page_header)

    @allure.step('Указать название блюда')
    def fill_name_input(self, name):
        self.fill_input(recipes_name_input, name)

    @allure.step('Указать название ингредиента')
    def fill_ingredient_name_input(self, ingredient_name):
        self.fill_input(ingredient_name_input, ingredient_name)

    @allure.step('Кликаем на ингредиент в списке')
    def click_ingredient_in_list(self):
        self.wait_for_visibility_of_element(first_ingredient_in_list)
        self.click_page_element(first_ingredient_in_list)

    @allure.step('Кликаем на Добавить ингредиент')
    def click_add_ingredient_button(self):
        self.click_page_element(add_ingredient_button)

    @allure.step('Указать количество ингредиента')
    def fill_ingredient_amount_input(self, amount):
        self.fill_input(ingredient_amount_input, amount)

    @allure.step('Указать время приготовления')
    def fill_time_input(self, time):
        self.fill_input(time_input, time)

    @allure.step('Заполнить описание рецепта')
    def fill_recipes_description_input(self, description):
        self.fill_input(recipes_description_input, description)

    @allure.step('Кликаем на Выбрать файл')
    def click_image_input(self):
        self.click_page_element(image_input)

    @allure.step('Кликаем на Создать рецепт')
    def click_create_button(self):
        self.click_page_element(create_button)

    @allure.step('Добавить ингредиент в список')
    def add_ingredient_in_list(self, name, amount):
        self.fill_ingredient_name_input(name)
        self.click_ingredient_in_list()
        self.fill_ingredient_amount_input(amount)
        self.click_add_ingredient_button()

    @allure.step('Добавить изображение')
    def upload_recipe_image(self, file_path):
        self.driver.file_detector = LocalFileDetector()
        image_element = self.driver.find_element(*self.file_input_locator)
        image_element.send_keys(file_path)

    @allure.step('Проверяем отображение карточки рецепта')
    def check_recipes_card_visibility(self):
        return self.wait_for_load_element(recipes_card)
    
    @allure.step('Проверяем отображение заголовка рецепта')
    def check_recipes_header_visibility(self):
        return self.wait_for_load_element(recipes_header)
    