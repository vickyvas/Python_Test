from selenium import webdriver
import unittest


class EnvSetUp(unittest.TestCase):
    def setUp(self):
        print("##############Test Execution Started##########")
        self.driver = webdriver.Chrome(executable_path="D:\Selenium\Jarfiles\Drivers\chromedriver.exe")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        print("#############Test Execution stopped")
        self.driver.quit()