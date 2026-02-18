from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



EMAIL = "elenagimpel34123@yandex.ru"
PASSWORD = "qwerty"

def test_logout(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "Account_button__14Yp3")))
    driver.find_element(*Locators.LOGOUT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

    assert driver.find_element(By.XPATH, "//button[text()='Войти']")