from locators import Locators

EMAIL = "elenagimpel34123@yandex.ru"
PASSWORD = "qwerty"

def test_logout(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGOUT).click()

    assert "login" in driver.current_url