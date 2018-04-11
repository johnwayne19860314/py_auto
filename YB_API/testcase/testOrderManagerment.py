# -*- coding:utf-8 -*-
import unittest

import requests
from Common import read_config
from Common import public
import json

rc=read_config.Read_config()
login=public.Public_Method()
class Order_Management(unittest.TestCase):
    def setUp(self):
        global url,resource
        url=rc.get_http('http')
        resource=rc.get_http('resource')

    def test_createOrder(self):
        u"""创建订单"""
        try:
            self.create_url=url+"/riskeys-web-spb/spb/user/order/createOrder.action"
            #获取登陆的session，用于创建投保订单
            cookie=login.test_login()
            session=requests.session()
            headers={
                'content-type': 'application/json'
            }
            u'''设置需要的参数：商铺信息，产品信息，投保人，被保人，雇员信息，发票信息
            market: 商场位置，0：苏宁广场
            equprice:设备价格    0-50-80万   1-80-100万
            fixPrice:装修价格   0-2000-3000元   1-3000-4000元  2-4000-5000元
            stockprice：存货价值   0-50-80万   1-80-100万
            '''
            params={
                #商铺信息
                'merchant':{
                'market':'0',
                'number':'100100',
                'name':'testmerchant',
                'kind':'餐饮类无明火饮品店',
                'area':'0',
                'equPrice':'0',
                'fixPrice':'0',
                'stockPrice':'0'
                },
                'product':{
                    'productId':'yb_spb',
                    'appId':'anyi',
                    'startTime':'2017-5-27',
                    'endTime':'2018-5-27',
                    'gzzrxLevel':'5',#责任险购买方案
                    'ccxLevel':'0',
                    'guzzrxLevel':'0',
                    'count':'2',
                    "content":{
                        # "map":{"size":{"0":"≤50㎡"},
                        # "device":{"0":"≤10万"},
                        # "decoration":{"0":"≤10万"},
                        # "stock":{"0":"≤10万"},
                        # "public":{"5":{"index":5,"fee":1200,"insuranceItem":{"顾客受伤":1000000,"影响临铺":1000000}}},
                        # "wealth":{"0":{"index":0,"fee":740,"insuranceItem":{"意外事故":300000,"盗窃抢劫":300000,"店内装修":100000,"店内机器":100000,"店内存货":100000,"装修翻修":100000,"小型设备":10000,"店内现金":10000,"停业损失":10000}}},
                        # "hirer":{"0":{"index":0,"fee":160,"insuranceItem":{"员工工伤":100000,"工伤医药费住院费":10000,"工伤误工津贴":10000}}},"bill":{"1":"normal"}}
                    }
                },
                #投保人
                'applicant':{
                    'type':'3',
                    'bizName':'投保',
                    'contactName':'test',
                    'contactTelephone':'18207278423'
                # 'contactIdCard':'420654199008097656',
                # 'contactEmail':'123@163.com'
                },
                #被保人
                'insured':{
                    'insuredWithApplicant':'0',
                    'insuredType':'2    ',
                    'insuredBizName':'test',
                    'insuredContactName':'test111',
                    'insuredContactTelephone':'18938987654'
                },
                #雇员列表
                'persons':[
                    {
                        'name':'ertyu',
                        'idCard':'420637199808097656',
                        'birthday':'1998-08-09',
                        'sex':'1',
                        'post':'',
                        'email':'',
                        'telephone':''
                    },
                    {
                        'name':'erty3u',
                        'idCard':'420623198908076787',
                        'birthday':'1989-08-07',
                        'sex':'2',
                        'post':'',
                        'email':'',
                        'telephone':''
                    }
                ],
                #发票信息
                'invoice':{
                    'type':'1',
                    'title':'增值税普通发票',
                    'contactName':'韩晓青',
                    'contactTelephone':'18207278423',
                    'address':'上海市浦东',
                    'postCode':'200000',
                    'registerAddress':'',
                    'bankName':'',
                    'account':'',
                    'telephone':'',
                    'code':{ }
                }
            }
            response=session.post(self.create_url,data=json.dumps(params),headers=headers,cookies=cookie)
            print(response.status_code)
            print(response.raise_for_status())
        except requests.RequestException as e:
            raise e

    def test_orderList(self):
        try:
            list_url=url+resource+"/spb/user/order/createOrder.action"
            cookie=login.test_login()
            session=requests.session()
            headers={
                'content-type': 'application/json'
            }
            params={
                "type":"1",#1‐批增 2‐批减 3‐投保  4‐批改
                "orderStatus":"1"#1‐待支付   2‐已支付   3‐待处理    4‐已处理
            }
            response=session.post(list_url,data=json.dumps(params),headers=headers,cookies=cookie)
            print(response.status_code)
        except  requests.RequestException as e:
            raise e

if __name__ == '__main__':
    unittest.main()
