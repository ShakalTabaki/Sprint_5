from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_logout(driver, login):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "Account_button__14Yp3")))
    driver.find_element(*Locators.LOGOUT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

    assert driver.find_element(By.XPATH, "//button[text()='Войти']")