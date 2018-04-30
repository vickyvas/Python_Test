from TestObject import Locators
from selenium.webdriver.common.by import By

class PythonHomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def clickPSF(self):
        self.driver.find_element(By.XPATH, Locators.PSF).click()

    def clickDocs(self):
        self.driver.find_element(By.XPATH, Locators.DOCS).click()

    def clickPypi(self):
        self.driver.find_element(By.XPATH, Locators.PYPI).click()

    def clickJobs(self):
        self.driver.find_element(By.XPATH, Locators.JOBS).click()

    def clickCommunity(self):
        self.driver.find_element(By.XPATH, Locators.COMMUNITY).click()