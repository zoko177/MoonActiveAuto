from selenium.webdriver.common.by import By

from pageObjects.CareersPage import CareersPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    title = (By.CSS_SELECTOR, "h2[class='small-title']")
    careerBut = (By.LINK_TEXT, "Careers")

    def get_title_name(self):
        return self.driver.find_element(*HomePage.title)

    def get_careers_button(self):
        self.driver.find_element(*HomePage.careerBut).click()
        return CareersPage(self.driver)

