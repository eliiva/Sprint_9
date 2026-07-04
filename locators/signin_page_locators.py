from selenium.webdriver.common.by import By

signin_page_header = [By.XPATH, ".//h1[text()='Войти на сайт']"]
email_input = [By.XPATH, ".//input[@name='email']"]
password_input = [By.XPATH, ".//input[@name='password']"]
signin_button = [By.XPATH, ".//button[text()='Войти']"]
create_account_button = [By.XPATH, ".//div/a[text()='Создать аккаунт']"]
singin_form = [By.XPATH, ".//form[contains(@class, 'styles_form__2nwxz')]"]
