from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config_reader import ConfigReader
from pages.recruitment_page import RecruitmentPage

class TestRecruitmentPage(BaseTest):
    def test_verify_recruitment_menu(self):
        login_page = LoginPage(self.driver)
        login_page.verify_before_login()
        login_page.login(ConfigReader.get_user_name(), ConfigReader.get_password())

        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.navigate_to_dashboard_page() is True, "Failed to navigate to Dashboard page"
        print("Successfully navigated to Dashboard page ")

        dashboard_page.click_recruitment_menu()

        recruitment_page = RecruitmentPage(self.driver)
        assert recruitment_page.navigate_to_recruitment_page(), "Failed to navigate to Recruitment page"
        print("Successfully navigated to Recruitment page")

        recruitment_page.click_vacancies_tab()
        







        