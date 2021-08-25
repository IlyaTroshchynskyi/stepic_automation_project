from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, "login is absent in current url browser"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form absent"

    def register_new_user(self, email, password):

        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_2)
        password2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
