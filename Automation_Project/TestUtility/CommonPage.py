from selenium.webdriver.common.by import By

class CommonPage(object):

    def __init__(self, driver):
        self.driver = driver

    findElement = {
        "XPATH": driver.find_element(By.XPATH, elementlocator)
    }
    def goback(self):
        return self.driver.back()

    def findElementByXpath(self, elementLocator):
        return self.driver.find_element(By.XPATH, elementLocator)

    def findElementByID(self, elementLocator):
        CommonPage.findElement.ge
        return self.driver.find_element(By.ID, elementLocator)

    def findElement(self, by, elementlocator):
