from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL
        )
        registration_email.send_keys(email)

        registration_password_1 = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_1
        )
        registration_password_1.send_keys(password)
        registration_password_2 = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_2
        )
        registration_password_2.send_keys(password)

        registration_submit = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_SUBMIT
        )
        registration_submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "No 'login' in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM),\
            "Registration form is not presented"
