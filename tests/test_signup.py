from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_success_registration(driver, generate_email):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_BUTTON))
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.NAME).send_keys("Elena")
    driver.find_element(*Locators.EMAIL).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD).send_keys("QWERTY")
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

    assert "login" in driver.current_url


def test_registration_invalid_password(driver, generate_email):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.NAME).send_keys("Elena")
    driver.find_element(*Locators.EMAIL).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD).send_keys("Q")
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']")))

    assert driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']")
