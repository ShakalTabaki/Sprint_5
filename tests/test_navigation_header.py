from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_go_to_account(driver, login):
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']")))

    assert driver.find_element(By.XPATH, "//button[text()='Сохранить']")


def test_go_to_constructor_with_button(driver, login):
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.KONSTRUCTOR_BUTTON).click()

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")


def test_go_to_constructor_with_logo(driver, login):
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']"))) 
    driver.find_element(*Locators.LOGO).click()

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")