import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    dir_path = os.path.dirname(os.path.abspath('.'))
    Chrome_path = dir_path + '/tools/chromedriver.exe'
    # firefox_path = os.path.dirname('./tools/geckodriver.exe')
    # Chrome_path = os.path.dirname(os.path.abspath('.'))+'/tools/chromedriver.exe/'
    # IE_path = os.path.dirname('./tools/IEDriverServer.exe')
    # def __init__(self,driver):
    #     self.driver=driver
    def open_browser(self):
        config = ConfigParser()
        file = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file)
        browser = config.get('browserType', 'browserName')
        logger.info('选择浏览器：%s' % browser)
        url= config.get('testServer', 'URL')
        logger.info('地址：%s' % url)
        if browser == 'Chrome':
            self.driver = webdriver.Chrome(self.Chrome_path)
            logger.info('打开Chrome浏览器')
        #
        # elif browser == 'IE':
        #     self.driver = webdriver.Ie(self.IE_path)
        #     logger.info('打开IE浏览器')
        # if browser == 'Firefox':
        #     self.driver = webdriver.Firefox(self.firefox_path)
        #     logger.info('打开火狐浏览器')
        # self.driver.get('http://www.baidu.com')
        self.driver.get(url)
        logger.info('打开网址')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return self.driver

    def quit_browser(self):
        logger.info('退出浏览器')
        self.driver.quit()