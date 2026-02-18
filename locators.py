from selenium.webdriver.common.by import By


class Locators:
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']") # Кнопка Личный Кабинет на главной
    REG_BUTTON = (By.XPATH, "//a[@href='/register']") # Кнопка "Зарегистрироваться", переход в форму решистрации из формы вход
    NAME = (By.XPATH, "//*[text()='Имя']//following-sibling::*") # Поле ввода имени для регистрации
    EMAIL = (By.XPATH, "//*[text()='Email']//following-sibling::*") # Поле ввода email
    PASSWORD = (By.XPATH, "//*[text()='Пароль']//following-sibling::*") # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться" в поле регистрации
    LOGIN_BUTTON_REG_FORM = (By.CLASS_NAME, "Auth_link__1fOlj") # Кнопка "Войти", переход на форму авторизации из формы регистрации
    LOGIN_BUTTON_MAINPAGE = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной странице
    FORGOT_PASS_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']") # Кнопка "Восстановить пароль", переход на форму восстановления пароля
    LOGIN_BUTTON_FORGOT_PASS_FORM = (By.CLASS_NAME, "Auth_link__1fOlj") # Кнопка "Войти", переход на форму авторизации из формы ворсстановления пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти" в форме авторизации
    KONSTRUCTOR_BUTTON = (By.XPATH, "//ul[@class='AppHeader_header__list__3oKJj']/li[1]/a") # Кнопка "Конструктор", переход из ЛК в конструктор
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип (переход из ЛК в конструктор)
    LOGOUT = (By.CLASS_NAME, "Account_button__14Yp3") # Кнопка "Выход", выход их аккаунта в ЛК
    BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")

