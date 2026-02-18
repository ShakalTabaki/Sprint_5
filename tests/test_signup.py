from selenium.webdriver.common.by import By
from locators import Locators


def test_success_registration(driver, generate_email):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.NAME).send_keys("Elena")
    driver.find_element(*Locators.EMAIL).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD).send_keys("QWERTY")
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    assert "login" in driver.current_url


def test_registration_invalid_password(driver, generate_email):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.NAME).send_keys("Elena")
    driver.find_element(*Locators.EMAIL).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD).send_keys("Q")
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    error = driver.find_element(By.XPATH, "//*[text()='Некорректный пароль']")
    assert error.is_displayed()
