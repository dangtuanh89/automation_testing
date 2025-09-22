from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_path = (By.XPATH, "//input[@name = 'username']")
        self.password_path = (By.XPATH, "//input[@name = 'password']")
        self.login_btn_path = (By.XPATH, "//button[@type = 'submit']")

    def verify_before_login(self):
        assert self.get_element(self.username_path).is_displayed(), "Username field is not displayed"
        print("Username field is displayed")
        assert self.get_element(self.password_path).is_displayed(), "Password field is not displayed"
        print("Password field is displayed")
        assert self.get_element(self.login_btn_path).is_displayed(), "Login button is not displayed"
        print("Login button is displayed")

    def login(self, username, password):
        self.get_element(self.username_path).send_keys(username)
        self.get_element(self.password_path).send_keys(password)
        self.get_element(self.login_btn_path).click()

    
