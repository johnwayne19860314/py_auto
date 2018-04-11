# -*- coding:utf-8 -*-
from ..Public import operation
#from ..Public import getCsv
from ..Public import LogManager
from selenium.webdriver.common.keys import Keys
import time

operate=operation.Common()
#getcsv=getCsv.GetCsv()
log=LogManager.LogMgr('order')
class orderManage():

    u"""
        保单管理公众方法
    """
    def orderByproduct(self,product):
        u"""
        查询订单
        :param product: 产品名称
        :return: 该名称的订单
        """
        #获取当前时间
        nowdata=time.strftime('%Y-%m-%d')
        #选择产品名称，查询订单
        operate.element_click("xpath",".//*[@id='prod_name1_chosen']/a")
        #输入产品名称
        input=".//*[@id='prod_name1_chosen']/div/div/input"
        operate.element_input("xpath",input,product)
        operate.element_input("xpath",input,Keys.ENTER)
        #点击查询
        operate.element_click("id","btn-select")
        #判断是否存在该产品名称的产品
        p_name=".//*[@id='dynamic-table']/tbody/tr[1]/td[7]"
        timelist=operate.getelement("xpath",p_name)
        # order=operate.getelement("xpath",".//*[@id='dynamic-table']/tbody/tr[1]/td[3]")
        # orderNo=order.text
        try:
            if nowdata in timelist.text:
                #查找到当前添加的数据，查看明细,根据订单号查找
                detail=".//*[@id='dynamic-table']/tbody/tr[1]//a"
                operate.element_click("xpath",detail)
                operate.mouse_pull()
                operate.sleep(2)
            else:
                log.debug(u"查询数据错误")
        except Exception as e:
            print(e)
        #返回保单管理
        operate.element_click("xpath",".//*[@id='sidebar']/ul/li[@data-href='policy.html']")
        operate.sleep(3)


    def policyByproduct(self,product):
        u"""
        保单查询
        :param product: 产品名称
        :return: 保单数据总量
        """
        #进入保单管理
        operate.element_click("id","policy-on")
        #选择产品名称，查询订单
        operate.element_click("xpath",".//*[@id='prod_name2_chosen']/a")
        #输入产品名称
        input=".//*[@id='prod_name2_chosen']/div/div/input"
        operate.element_input("xpath",input,product)
        operate.element_input("xpath",input,Keys.ENTER)
        #点击查询
        operate.element_click("id","btn-select2")
        #查询该产品的保单数量，大于0，通过
        policy_list=operate.elements_list("xpath",".//*[@id='dynamic-table2']/tbody/tr")
        policy_num=len(policy_list)
        if policy_num>0:
            operate.mouse_pull()
            operate.sleep(2)
            #返回到创建保单页面
            operate.element_click("xpath",".//*[@id='sidebar']/ul/li[@data-href='order.html']")
        else:
            log.debug(u"保单管理错误")