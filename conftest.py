import pytest
import random
from selenium import webdriver
from data import BASE_URL

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