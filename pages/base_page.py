from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дожидаемся загрузки элемента на странице')
    def wait_for_load_element(self, element_locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element_locator))
    
    @allure.step('Находим элемент на странице')
    def find_element(self, element_locator):
        return self.driver.find_element(*element_locator)
    
    @allure.step('Дожидаемся, пока элемент станет кликабельным')
    def wait_for_element_to_be_clickable(self, element_locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(element_locator)
        )

    @allure.step('Кликаем по элементу')
    def click_page_element(self, element_locator):
        element = self.wait_for_load_element(element_locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Заполняем инпут')
    def fill_input(self, input_locator, value):
        self.driver.find_element(*input_locator).send_keys(value)

    @allure.step('Получаем текст элемента')
    def get_element_text(self, element_locator):
        return self.driver.find_element(*element_locator).text
    
    @allure.step('Ждём, пока текущий URL не сменитя на ожидаемый')
    def wait_for_url_change_to(self, expected_url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(expected_url),
            message=f"URL не изменился за {timeout}с. Ожидался: {expected_url}, текущий: {self.driver.current_url}"
        )
    
    @allure.step('Дожидаемся скрытия элемента')
    def wait_for_invisibility_of_element(self, element_locator):
        return WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(element_locator)
        )

    @allure.step('Дожидаемся отображения элемента')
    def wait_for_visibility_of_element(self, element_locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(element_locator)
        )
