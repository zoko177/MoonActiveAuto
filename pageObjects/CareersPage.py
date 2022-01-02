from selenium.webdriver.common.by import By

from pageObjects.RaDPage import RaDPage


class CareersPage:

    def __init__(self, driver):
        self.driver = driver

    careers_title = (By.CLASS_NAME, "main-title")
    job_sections = (By.XPATH, "//div[@class='job-depts']/div")

    def get_careers_title(self):
        return self.driver.find_element(*CareersPage.careers_title)

    def select_job_section(self, section_name):
        jobSections = self.driver.find_elements(*CareersPage.job_sections)
        for section in jobSections:
            if section_name == section.text.split('\n')[0]:
                section.click()
                return RaDPage(self.driver)