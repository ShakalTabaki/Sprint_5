from locators import Locators

EMAIL = "elenagimpel34123@yandex.ru"
PASSWORD = "qwerty"

def login(driver):
    driver.find_element(*Locators.EMAIL).send_keys(EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()


def test_login_from_main_page(driver):
    driver.find_element(*Locators.LOGIN_BUTTON_MAINPAGE).click()
    login(driver)

    assert "account" in driver.current_url


def test_login_from_account_button(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    login(driver)

    assert "account" in driver.current_url


def test_login_from_login_button_in_reg_form(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.LOGIN_BUTTON_REG_FORM).click()
    login(driver)

    assert "account" in driver.current_url
    

def test_login_from_login_button_in_forgot_pass_form(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.FORGOT_PASS_BUTTON).click()
    driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_PASS_FORM).click()
    login(driver)

    assert "account" in driver.current_url