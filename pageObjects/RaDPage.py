from selenium.webdriver.common.by import By

from pageObjects.JobPage import JobPage


class RaDPage:

    def __init__(self, driver):
        self.driver = driver

    section_title = (By.CSS_SELECTOR, "div[data-dept='r-d'] span[class='dept-name']")
    jobs_list = (By.CSS_SELECTOR, "li[class='job-item']")

    def get_section_title(self):
        return self.driver.find_element(*RaDPage.section_title)

    def click_job(self, job_name):
        jobs = self.driver.find_elements(*RaDPage.jobs_list)
        for job in jobs:
            if job.text.split('\n')[0] == job_name:
                self.driver.execute_script("arguments[0].click();", job.find_element(by='css selector', value="a"))
                return JobPage(self.driver)
