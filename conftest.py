import pytest
import random
from selenium import webdriver
from locators import Locators
from data import BASE_URL, EMAIL, PASSWORD

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def generate_email():
    def _generate():
        return f"elenagimpel33{random.randint(100,999)}@yandex.ru"
    return _generate


def login(driver):
    driver.find_element(*Locators.EMAIL).send_keys(EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()