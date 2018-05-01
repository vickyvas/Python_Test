from TestObject.PageObjects.PythonHomePage import PythonHomePage
from TestUtility.CommonPage import CommonPage


class CCFile(PythonHomePage, CommonPage):

        def __init__(self, driver):
            PythonHomePage.__init__(self, driver)
            CommonPage.__init__(self, driver)
