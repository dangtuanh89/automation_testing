from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

class TestLoginPage(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.verify_before_login()
        login_page.login(ConfigReader.get_user_name(), ConfigReader.get_password())

        # Thêm locators cho error messages
        self.required_error_path = (By.XPATH, "//span[contains(text(),'Required')]")
        self.invalid_credentials_path = (By.XPATH, "//p[contains(text(),'Invalid credentials')]")

    def test_navigate_to_dashboard_page(self):
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.navigate_to_dashboard_page() is True, "Failed to navigate to Dashboard page"
        print("Successfully navigated to Dashboard page ")
        
