from base.base_page import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_path = (By.XPATH, "//h6[@class = 'oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        self.recruitment_menu_path = (By.XPATH, "//span[text () = 'Recruitment']")
        self.user_profile_path = (By.XPATH, "//p[@class = 'oxd-userdropdown-name']")
        self.log_out_path = (By.XPATH, "//a[@role = 'menuitem' and text() = 'Logout']")
        self.login_btn_path = (By.XPATH, "//button[@type = 'submit']")

    def navigate_to_dashboard_page(self):
        try:
            dashboard = self.get_element(self.dashboard_path)
            return dashboard.is_displayed()
            
        except Exception:
            return False
        
    def is_recruitment_menu_displayed(self):
        try:
            recruitment_menu = self.get_element(self.recruitment_menu_path)
            return recruitment_menu.is_displayed()
            
        except Exception:
            return False
    
    def click_recruitment_menu(self):
        self.get_element(self.recruitment_menu_path).click()

    def log_out(self):
        self.get_element(self.user_profile_path).click()
        self.get_element(self.log_out_path).click()

    def verify_logout(self):
        try:
            login_btn = self.get_element(self.login_btn_path)
            return login_btn.is_displayed()
        except Exception:
            return False

