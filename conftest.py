import pytest
import random
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru")
    yield driver
    driver.quit()


@pytest.fixture
def generate_email():
    def _generate():
        return f"elenagimpel33{random.randint(100,999)}@yandex.ru"
    return _generate