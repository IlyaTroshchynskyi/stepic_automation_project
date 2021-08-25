from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span a")
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, 'div.content > div#content_inner > p')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD_1 = (By.ID, 'id_registration-password1')
    PASSWORD_2 = (By.ID, 'id_registration-password2')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="registration_submit"]')


class ProductPageLocators:
    BTN_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PROD_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PROD_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')