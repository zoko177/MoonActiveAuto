import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyTextInElement(self, ele, text):
        WebDriverWait(self.driver, 5).until(ec.text_to_be_present_in_element(ele, text))

    def getLog(self):
        loggerName = inspect.stack()[1][3]
        log = logging.getLogger(loggerName)
        fileH = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileH.setFormatter(formatter)

        log.addHandler(fileH)
        log.setLevel(logging.DEBUG)

        return log
