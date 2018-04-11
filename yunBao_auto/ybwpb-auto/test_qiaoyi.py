# -*- coding:utf-8 -*-
#from __future__ import absolute_import
import unittest
import time
from collections import OrderedDict
import sys,os
#sys.path.append("..")
sys.path.insert(0, os.path.dirname(os.getcwd()))
print 'sys path ',sys.path
#print 'python_path ', os.environ
print 'parent folder of current process ',os.path.dirname(os.getcwd())

print 'sys modules', sys.modules
#print 'sys.meta_path ', sys.meta_path
#sys.modules['zlib'].__file__

#if __name__ == "__main__" and __package__ is None:
    #__package__ = "expected.package.name"
  #  __package__ = "ybwpb-auto"

print 'name', __name__
print 'package', __package__

#project root folder as AUto_UI, so start with yunBao_auto. every parent folder with __init__.py
#name as __main__, so have to use abosolute import

#from yunBao_auto.Public import LogManager
#from ..Public import LogManager as log
#from yunBao_auto.Public import operation
from yunBao_auto.Public import operation
from yunBao_auto.page import comMethod, HomePage,policyManage,orderManagement
from collections import OrderedDict
operate=operation.Common()
pagecom=comMethod.PageCom()
policy=policyManage.policyManage()
order=orderManagement.orderManage()
#log=LogManager.LogMgr('meixing')
#accm=accountManage.accountM()
#dbconn = DbConnect.DbUnit()

class Qiaoyi(unittest.TestCase):
    def test_0login(self):
        u"""登陆"""
       # HomePage.HomePage(self)
        #登陆渠道端
        operate.element_click("xpath","//div[@class='header']//a[@data-target='#channel-login']")
        #登陆
        time.sleep(2)
        self.name='anyi_channel'
        self.password='111111'
        login_input=OrderedDict([('tel2','anyi_channel'),
            ('password2',self.password)])
        pagecom.Publiclogin(login_input,"channel-login-btn")
        operate.sleep(2)

    def test_createOrder(self):
        u"""创建保单"""
        u"""
        创建桥溢物流保单
        :return: 保单
        """
        #进入创建保单链接
        operate.element_click("xpath",".//*[@id='sidebar']/ul/li[@data-href='order.html']")
        operate.sleep(2)
        #读取csv数据，调用policyManager用于批量添加保单
        policy.addpolicy()

    # 进入保单管理，查询
    # def test_managerOrder(self):
    #     u"""查询订单和保单"""
    #     u"""
    #     进入保单管理，查询名称是是桥溢物流的数据
    #     :return: 数据
    #     """
    #     #刷新页面，进入保单管理
    #     # operate.refresh()
    #     operate.element_click("xpath",".//*[@id='sidebar']/ul/li[@data-href='policy.html']")
    #     operate.sleep(3)
    #     #搜索订单产品名称为国内水路、陆路货物运输保险
    #     order.orderByproduct(u"国内水路、陆路货物运输保险")
    #     #查看保单管理
    #     order.policyByproduct(u"国内水路、陆路货物运输保险")
        #关闭浏览器
       # homepage = HomePage.BrowserDriver()
      #  homepage.closePage()

if __name__ == '__main__':
    #创建测试集
    suite=unittest.TestSuite()
    suite.addTest(Qiaoyi("test_0login"))
    # suite.addTest(Qiaoyi("test_createOrder"))
    # suite.addTest(Qiaoyi("test_managerOrder"))

    #执行测试集
    runner=unittest.TextTestRunner()
    runner.run(suite)

