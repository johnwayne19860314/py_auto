# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import os,time,sys
from yunBao_auto.Public import email_write

#定义测试路径以及测试文件报告名
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
files = sys.path[0]
print('the files are ', files)
reportfilename=os.path.join(files, 'report', 'test_result'+now+'.html')

#创建测试组件
def createsuite():
    u"""创建测试组件"""
    print(u'开始创建测试组件')
    testunit = unittest.TestSuite()     #pattern='test_*.py'
    discover = unittest.defaultTestLoader.discover(os.path.join(files,'ybwpb-auto'),
                                        pattern='test_enquiry.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
   # print testunit
    print(u'创建测试组件结束')
    return testunit

def write(filenames,names):
    #读取报告
    with open(filenames,'wb') as fp:
        #定义runner
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'测试报告',
            description=u'用例执行情况：'
            )
        #执行用例
        print(u'开始执行测试用例;')
        runner.run(names)
        print(u'执行测试用例完成;')


if __name__=="__main__":
    #执行用例、生成报告
    alltestnames=createsuite()
    write(reportfilename,
          alltestnames)
    #执行发送报告
    time.sleep(10)
    email_write.sendreport()
    #清除测试产生的screenshot和repot
    time.sleep(10)
    email_write.clean()