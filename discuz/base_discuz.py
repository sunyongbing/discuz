from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from selenium import webdriver
import os

logger=Logger(logger="BasePage").getlog()

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def get(self,url):
        self.driver.get(url)
    def back(self):
        self.driver.back()
        logger.info('Click back on current page.')
    def forward(self):
        self.driver.forward()
        logger.info('Click back on current page.')
    def quit(self):
        self.driver.quit()
    def close(self):
        try:
            self.driver.close()
            logger.info('Closing and quit the browser.')
        except Exception as e:
            logger.info('Failed to quit the browser with %s' % e)
    def clear(self, *loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info('Clear text in input box before typing.')
        except Exception as e:
            logger.error('Failed to clear in input box with %s' % e)
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("find element")
            return self.driver.find_element(*loc)

        except:
            logger.error('%s页面未找到%s元素'%(self,loc))
    def get_text(self, *loc):
        try:
            str1 = self.find_element(*loc)
            str2 = str1.text
            logger.info('find %s' % str2)
            return str2
        except Exception as e:
            logger.error('element don''t find %s' % e)
    def sendkeys(self, text, *loc):
        el=self.find_element(*loc)
        # el.clear()
        try:
            el.send_keys(text)
            logger.info(text)
        except Exception as e:
            logger.error('Failed to type in input box with %s' % e)

    def click(self, *loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info('this element %s was clicked.'% el.text)
        except Exception as e:
            logger.error('Failed to click the element with %s' % e)

    def window(self):
        window = self.driver.current_window_handle
        self.driver.switch_to.window(window)

    def window_handles(self,a):
        self.driver.switch_to.window(self.driver.window_handles[a])

    def close_window(self):
        self.driver.close()

    def iframe(self,id):
        self.driver.switch_to.frame(id)

    def fanhuiiframe(self):
        self.driver.switch_to.default_content()

    # def yanzheng(self,a):
    #     assert a in self.driver.


