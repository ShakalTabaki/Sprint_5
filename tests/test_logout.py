from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_logout(driver, login):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    login(driver)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT))
    driver.find_element(*Locators.LOGOUT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

    assert driver.find_element(Locators.LOGIN_BUTTON)