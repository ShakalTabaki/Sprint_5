from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import login


def test_login_from_main_page(driver):
    driver.find_element(*Locators.LOGIN_BUTTON_MAINPAGE).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert driver.find_element(*Locators.ORDER_BUTTON)


def test_login_from_account_button(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert driver.find_element(*Locators.ORDER_BUTTON)


def test_login_from_login_button_in_reg_form(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.LOGIN_BUTTON_REG_FORM).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert driver.find_element(*Locators.ORDER_BUTTON)
    

def test_login_from_login_button_in_forgot_pass_form(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FORGOT_PASS_BUTTON))
    driver.find_element(*Locators.FORGOT_PASS_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_FORGOT_PASS_FORM))
    driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_PASS_FORM).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert driver.find_element(*Locators.ORDER_BUTTON)