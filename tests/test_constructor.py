from locators import Locators


def test_switch_to_buns(driver):
    driver.find_element(*Locators.SAUCES).click()
    driver.find_element(*Locators.BUNS).click()
    buns = driver.find_element(*Locators.BUNS)

    assert "tab_tab_type_current" in buns.get_attribute("class")

def test_switch_to_sauces(driver):
    driver.find_element(*Locators.SAUСES).click()
    sauces = driver.find_element(*Locators.SAUСES)

    assert "tab_tab_type_current" in sauces.get_attribute("class")


def test_switch_to_fillings(driver):
    driver.find_element(*Locators.FILLINGS).click()
    fillings = driver.find_element(*Locators.FILLINGS)

    assert "tab_tab_type_current" in fillings.get_attribute("class")
