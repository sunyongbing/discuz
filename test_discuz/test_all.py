import os
import unittest
from test_discuz.test_home1 import *
from test_discuz.test_home2 import *
from test_discuz.test_home3 import *
from test_discuz.test_home4 import *
import HTMLTestRunner


wo_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(wo_path,'report2')
if not os.path.exists(report_path): os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(DiscuzSearch1))
suite.addTest(unittest.makeSuite(DiscuzSearch2))
suite.addTest(unittest.makeSuite(DiscuzSearch3))
suite.addTest(unittest.makeSuite(DiscuzSearch4))
if __name__=='__main__':
    # unittest.main(verbosity=2)
    html_report=report_path+r'\result.html'
    fp=open(html_report,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title='单元测试报告',description='用例执行情况')
    runner.run(suite)