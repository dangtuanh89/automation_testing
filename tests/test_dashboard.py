from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config_reader import ConfigReader

class TestDashboardPage(BaseTest):
    def test_verify_recruitment_menu(self):
        login_page = LoginPage(self.driver)
        login_page.verify_before_login()
        login_page.login(ConfigReader.get_user_name(), ConfigReader.get_password())

        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.navigate_to_dashboard_page() is True, "Failed to navigate to Dashboard page"
        print("Successfully navigated to Dashboard page ")

        assert dashboard_page.is_recruitment_menu_displayed() is True, "Recruitment menu is not displayed"
        print("Recruitment menu is displayed")

        dashboard_page.log_out()
        assert dashboard_page.verify_logout() is True, "Failed to logout"
        print('Logout successfully')
        