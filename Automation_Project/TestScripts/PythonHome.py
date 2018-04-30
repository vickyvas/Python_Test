from TestRunnerAndSetup.EnvSetUp import EnvSetUp
from TestObject.ClassConfigurationFile import CCFile
from TestObject.PageObjects.PythonHomePage import PythonHomePage


class PythonHome(EnvSetUp):
    def test_Open_URL(self):
        driver = self.driver
        self.driver.get("https://www.python.org/")

        file = CCFile(driver)
        # pyhomepage = PythonHomePage(driver)
        file.clickPSF()
        file.clickDocs()
        file.goback()
        file.clickPypi()
        file.goback()
        file.clickJobs()
        file.clickCommunity()
        # pyhomepage.clickPSF()
