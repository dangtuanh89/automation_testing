from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage
from utils.config_reader import ConfigReader

class TestAddVacancy(BaseTest):
    def test_add_vacancy(self):
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
        recruitment_page.click_add_btn()

        vacancy_page = VacancyPage(self.driver)
        assert vacancy_page.is_add_vancancy_displayed(), "Add vacancy page is not displayed"
        print('Add vacancy page is displayed')

        vacancy_page.input_vacancy_data(ConfigReader.get_vacancy_name(), ConfigReader.get_description(), ConfigReader.get_number_of_positions())
        assert vacancy_page.click_save_btn(), "Edit vacancy is not displayed"
        print("Edit vacancy is displayed")
             


