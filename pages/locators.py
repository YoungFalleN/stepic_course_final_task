from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    TITLE_IN_MESSAGE = (By.CSS_SELECTOR,
                        ".alert-success:first-child .alertinner strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
