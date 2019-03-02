import unittest
from framework.browser_engine import *
from selenium import webdriver

brower = BrowserEngine()
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

        self.driver=brower.open_browser()

    def tearDown(self):
        # self.driver.quit()
        self.driver=brower.quit_browser()