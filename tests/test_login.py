from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


EMAIL = "elenagimpel34123@yandex.ru"
PASSWORD = "qwerty"

def login(driver):
    driver.find_element(*Locators.EMAIL).send_keys(EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()


def test_login_from_main_page(driver):
    driver.find_element(*Locators.LOGIN_BUTTON_MAINPAGE).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")


def test_login_from_account_button(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")


def test_login_from_login_button_in_reg_form(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.LOGIN_BUTTON_REG_FORM).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
    

def test_login_from_login_button_in_forgot_pass_form(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FORGOT_PASS_BUTTON))
    driver.find_element(*Locators.FORGOT_PASS_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_FORGOT_PASS_FORM))
    driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_PASS_FORM).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")