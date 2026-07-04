from selenium.webdriver.common.by import By

signup_page_header = [By.XPATH, ".//h1[text()='Регистрация']"]
first_name_input = [By.XPATH, ".//input[@name='first_name']"]
last_name_input = [By.XPATH, ".//input[@name='last_name']"]
username_input = [By.XPATH, ".//input[@name='username']"]
email_input = [By.XPATH, ".//input[@name='email']"]
password_input = [By.XPATH, ".//input[@name='password']"]
create_account_button = [By.XPATH, ".//button[text()='Создать аккаунт']"]
