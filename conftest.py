import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture
def driver():
    options = ChromeOptions()

    options.browser_version = "128.0"
    options.set_capability('acceptInsecureCerts', True)
    
    selenoid_options = {
        "enableVideo": False
    }
    options.set_capability("selenoid:options", selenoid_options)
    
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=options
    )
    
    driver.maximize_window()
    yield driver
    driver.quit()
