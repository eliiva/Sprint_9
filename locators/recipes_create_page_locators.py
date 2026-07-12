from selenium.webdriver.common.by import By

recipes_create_page_header = [By.XPATH, ".//h1[text()='Создание рецепта']"]
recipes_name_input = [By.XPATH, ".//form/div[@class='styles_input__2Dg_j']/label/input[@class='styles_inputField__3eqTj']"]
ingredient_name_input = [By.XPATH, ".//div/label/input[contains(@class, 'styles_ingredientsInput__1zzql')]"]
ingredient_amount_input = [By.XPATH, ".//div/label/input[contains(@class, 'styles_ingredientsAmountValue__2matT')]"]
first_ingredient_in_list = [By.XPATH, ".//div[@class='styles_container__3ukwm']/div[1]"]
add_ingredient_button = [By.XPATH, ".//div[text()='Добавить ингредиент']"]
time_input = [By.XPATH, ".//div[contains(@class, 'styles_ingredientsTimeInput__3oqdd')]/label/input"]
recipes_description_input = [By.XPATH, ".//div/label/textarea[contains(@class, 'styles_textareaField__1wfhC')]"]
image_input = [By.XPATH, ".//input[@type='file']"]
create_button = (By.XPATH, "//button[text()='Создать рецепт']")
recipes_card = [By.XPATH, ".//div[@class='styles_single-card__1yTTj']"]
recipes_header = [By.XPATH, ".//h1[@class='styles_single-card__title__2QMPq']"]
