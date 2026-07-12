import allure
from pages.signin_page import SigninPage
from pages.main_page import MainPage
from pages.recipes_create_page import RecipesCreatePage
from pathlib import Path
from urls import signin_page_url

class TestCreateRecipes:

    @allure.title('Проверка успешного создания рецепта')
    @allure.description('Авторизуемся, заполняем поля создания рецепта, нажимаем Создать рецепт и проверяем результат')
    def test_create_recipes(self, driver):
        driver.get(signin_page_url)

        signin_page = SigninPage(driver)
        signin_page.singing_registered_user()

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_create_recipes_link()

        recipes_create_page = RecipesCreatePage(driver)
        recipes_create_page.wait_for_load_recipes_create_page()
        recipes_create_page.fill_name_input('Блинчики')
        recipes_create_page.add_ingredient_in_list('вода', '600')
        recipes_create_page.add_ingredient_in_list('мука', '300')
        recipes_create_page.add_ingredient_in_list('яйца куриные', '100')
        recipes_create_page.add_ingredient_in_list('соль', '5')
        recipes_create_page.fill_time_input('60')
        recipes_create_page.fill_recipes_description_input('Всё перемешать, подождать 20 минут, пожарить.')

        project_root = Path(__file__).resolve().parent.parent
        image_path = str(project_root / 'assets' / 'pancakes.jpg')
        recipes_create_page.upload_recipe_image(image_path)

        recipes_create_page.click_create_button()

        assert recipes_create_page.check_recipes_card_visibility()
        assert recipes_create_page.check_recipes_header_visibility()
