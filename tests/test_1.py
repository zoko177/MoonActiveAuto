import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import numpy as np

from Data.Data import MyData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_1(self, getData):
        log = self.getLog()
        assert not (np.nan in getData.values()), log.critical('Data not filled right')
        job_section = getData['Job Section']
        job_name = getData['Job Name']
        home_page = HomePage(self.driver)
        assert home_page.get_title_name().text == 'MEET\nMOON ACTIVE', log.critical('Not Correct Home Page')
        log.info('Reached Home Page')
        careers_page = home_page.get_careers_button()
        assert careers_page.get_careers_title().text == 'JOIN THE CREW', log.critical('Not Correct Careers Page')
        log.info("Entered Careers Page")
        # R&D page
        section_page = careers_page.select_job_section(job_section)
        # self.driver.find_element(by='xpath', value="//span[contains(text(),'R&D')]").click()
        self.verifyTextInElement(section_page.section_title, job_section)
        # WebDriverWait(section_page.driver, 5).until(ec.text_to_be_present_in_element(section_page.section_title, job_section))
        assert section_page.get_section_title().text == job_section, log.critical('Not Correct Job Section')
        log.info("Entered Correct Job Section")
        # Select job page Page

        job_page = section_page.click_job(job_name)
        assert job_page.get_page_title().text.lower() == job_name.lower(), log.critical('Not Correct Job')
        log.info("Entered Correct Job")
        job_page.driver.switch_to.frame("iFrameResizer0")
        job_page.get_first_name().send_keys(getData['First Name'])
        job_page.get_last_name().send_keys(getData['Last Name'])
        job_page.get_email().send_keys(getData['Email'])
        job_page.get_phone().send_keys(getData['Phone Number'])
        job_page.upload_resume(getData['Resume PC Path'])
        job_page.get_personal_note().send_keys(getData['More Info'])
        job_page.driver.switch_to.default_content()
        print('ka')

    @pytest.fixture(params=MyData.get_data())
    def getData(self, request):
        return request.param
        # self.driver.execute_script("arguments[0].click();", self.driver.find_element(by='css selector', value="a[data-id='00.71F']"))
