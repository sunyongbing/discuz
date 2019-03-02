import unittest
from selenium import webdriver
from test_discuz.test_base import BaseTestCase
from discuz.discuz import Discuz
import time

class DiscuzSearch1(BaseTestCase):
    def test_baidu_search(self):
        home_page=Discuz(self.driver)
        # home_page.get('http://127.0.0.1/forum.php')
        time.sleep(2)
        home_page.login('admin','admin')

        time.sleep(2)
        home_page.morenbankuai()
        home_page.fatie('ww','ewrstydfxdtsressdrxg')
        time.sleep(2)
        home_page.huifu('yyyyyyyyyyyyyyyyyyyyyy')
        home_page.tuichu()

if __name__=='__main__':
    unittest.main()
