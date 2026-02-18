from selenium.webdriver.common.by import By
from locators import Locators

EMAIL = "elenagimpel34123@yandex.ru"
PASSWORD = "qwerty"


def login(driver):
    driver.find_element(*Locators.LOGIN_BUTTON_MAINPAGE).click()
    driver.find_element(*Locators.EMAIL).send_keys(EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()


def test_go_to_account(driver):
    login(driver)
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()

    assert "account" in driver.current_url


def test_go_to_constructor_with_button(driver):
    login(driver)
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.KONSTRUCTOR_BUTTON).click()

    konstructor = driver.find_element(By.XPATH, "//*[text()='Соберите бургер']")
    assert konstructor.is_displayed()


def test_go_to_constructor_with_logo(driver):
    login(driver)
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGO).click()

    konstructor = driver.find_element(By.XPATH, "//*[text()='Соберите бургер']")
    assert konstructor.is_displayed()
