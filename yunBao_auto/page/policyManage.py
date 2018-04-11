# -*- coding:utf-8 -*-
from ..Public import operation
from ..Public import getCsv
#from ..Public import LogManager
from collections import OrderedDict

operate=operation.Common()
getcsv=getCsv.GetCsv()
#log=LogManager.LogMgr('addaccount')
class policyManage(object):

    def addpolicy(self):
        csvpath=operate.read_file('testData','policy.csv')
        csvdict=getcsv.readCsv(csvpath)
        for list in csvdict:
            #保存输入框数据
            input_policy= OrderedDict(
                [
                ('insuredName',list[1]),
                ('insuredCardId',list[2]),
                ('insurerName',list[3]),
                ('insurerCardId',list[4]),
                ('insuredPhone',list[5]),
                ('insuredAddress',list[6]),
                ('ladingNo',list[7]),
                ('creditId',list[8]),
                ('weight',list[9]),
                ('fromAddress',list[13]),
                ('toAddress',list[14]),
                ('insurance-money',list[15])
                ]
            )
            #保存下拉框数据
            select_policy=OrderedDict(
                [
                # ('form-scean',list[0]),
                ('packType',list[10]),
                ('goodsType',list[11]),
                ('transportType',list[12]),
                ]
            )
            self.policyManagement(select_policy,input_policy)

    #创建保单
    def policyManagement(self,selectdict,inputdict):
        #输入保单数据
        operate.sleep(2)
        #选择桥一物流
        operate.element_selected("value",".//*[@id='form-scean']","yb_hywl")
        #查看特别约定和保险条款
        link=(
            # './/*[@id="form-product-info"]//a[@data-target="#rules-modal"]',
            #   './/*[@id="rules-modal"]/div[2]/div/div[1]/button',
              './/*[@id="form-product-info"]//a[2]',
              './/*[@id="modal-insure-items"]//button[@class="close" and @type="button"]')
        operate.tuple_click("xpath",link)
        operate.orderedDict_input("id",inputdict)
        operate.OrderedDict_select(selectdict)
        operate.sleep(2)
        operate.mouse_pull()
        operate.sleep(2)
        #选择交通工具
        operate.element_click("xpath",".//input[@value='飞机']")
        print 22
        #输入日期
        operate.element_click("id","departureDate")
        operate.element_click("xpath","//table/tbody//td[@class='new day'][1]")
        # #确认投保
        # operate.element_click("id","btn-order")
        # #确认投保信息
        # operate.mouse_pull()
        # operate.sleep(1)
        # operate.element_click("id","form-btn-order")
        # #投保成功
        # operate.element_click("xpath",".//*[@id='anyi-modal-alert']//a[@class='modal-close']")
        # operate.sleep(2)
