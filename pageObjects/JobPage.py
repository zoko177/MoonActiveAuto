import pyautogui
import time
from selenium.webdriver.common.by import By


class JobPage:

    def __init__(self, driver):
        self.driver = driver

    job_title = (By.CSS_SELECTOR, "div[class='position-department-name'] h1")
    first_name = (By.ID, "inputFirstName")
    last_name = (By.ID, "inputLastName")
    email = (By.ID, "inputEmail")
    phone = (By.ID, "inputTel")
    resume_butt = (By.CSS_SELECTOR, "label[class='clickableLink']")
    personal_note = (By.ID, "inputNote")

    def get_page_title(self):
        return self.driver.find_element(*JobPage.job_title)

    def get_first_name(self):
        return self.driver.find_element(*JobPage.first_name)

    def get_last_name(self):
        return self.driver.find_element(*JobPage.last_name)

    def get_email(self):
        return self.driver.find_element(*JobPage.email)

    def get_phone(self):
        return self.driver.find_element(*JobPage.phone)

    def upload_resume(self, path):
        self.driver.find_element(*JobPage.resume_butt).click()
        time.sleep(2)
        pyautogui.write(path)
        pyautogui.press('enter')

    def get_personal_note(self):
        return self.driver.find_element(*JobPage.personal_note)

