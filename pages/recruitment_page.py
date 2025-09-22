from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from base.base_page import BasePage
from selenium.webdriver.common.by import By

class RecruitmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.vacancies_path = (By.XPATH, "//a[text () = 'Vacancies']")
        self.add_btn_path = (By.XPATH, "//button[text () = ' Add ']")
    
    def navigate_to_recruitment_page(self):
        return self.get_element(self.vacancies_path).is_displayed()
    
    def click_vacancies_tab(self):
        self.get_element(self.vacancies_path).click()
    
    def click_add_btn(self):
        self.get_element(self.add_btn_path).click()

    