from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class VacancyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_vacancy_path = (By.XPATH, "//h6[text () = 'Add Vacancy']")
        self.vacancy_name_path = (By.XPATH, "//label[text () = 'Vacancy Name']/following::input[@class='oxd-input oxd-input--active'][1]")
        self.job_title_select_box_path = (By.XPATH, "//label[text () = 'Job Title']/following::div[@class = 'oxd-select-wrapper']")
        self.description_path =(By.XPATH, "//textarea[@placeholder = 'Type description here']")
        self.hiring_manager_input_path = (By.XPATH, "//input[@placeholder = 'Type for hints...']")
        self.hiring_manager_dropdown_path = (By.XPATH, "//div[@role='listbox']//span")
        self.number_of_positons_path = (By.XPATH, "//label[text () = 'Number of Positions']/following::input[@class = 'oxd-input oxd-input--active']")
        self.job_title_path = (By.XPATH, "//div[@class = 'oxd-select-wrapper']//span[text () = 'Account Assistant']")
        self.login_user_path = (By.XPATH, "//p[@class = 'oxd-userdropdown-name']")    
        self.save_btn = (By.XPATH, "//button[text () = ' Save ']")
        self.edit_vacancy_path = (By.XPATH, "//h6[text () = 'Edit Vacancy']")

    def is_add_vancancy_displayed(self):
        return self.get_element(self.add_vacancy_path).is_displayed()
    
    def input_vacancy_data(self, vacany_name, description, number_of_positions):
        self.get_element(self.vacancy_name_path).send_keys(vacany_name)

        self.get_element(self.job_title_select_box_path).click()
        job_title = self.get_element(self.job_title_path).click()
        #self.driver.execute_script("arguments[0].click();", job_title)

        self.get_element(self.description_path).send_keys(description)

        login_user = self.get_element(self.login_user_path).text
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_element(self.hiring_manager_input_path))
        actions.click()
        actions.send_keys(login_user)
        self.get_element(self.hiring_manager_dropdown_path)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        self.get_element(self.number_of_positons_path).send_keys(number_of_positions)

    def click_save_btn(self): 
        self.get_element(self.save_btn).click()
        return self.get_element(self.edit_vacancy_path).is_displayed()


        



    
