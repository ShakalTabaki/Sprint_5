from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import login


class TestNavigationButtons:


    def test_go_to_account(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        login(driver)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAVE_BUTTON))

        assert driver.find_element(*Locators.SAVE_BUTTON)


    def test_go_to_constructor_with_button(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        login(driver)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.KONSTRUCTOR_BUTTON).click()

        assert driver.find_element(*Locators.ORDER_BUTTON)


    def test_go_to_constructor_with_logo(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        login(driver)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAVE_BUTTON)) 
        driver.find_element(*Locators.LOGO).click()

        assert driver.find_element(*Locators.ORDER_BUTTON)
