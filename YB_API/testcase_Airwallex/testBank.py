#-*- coding:utf-8 -*-
import json
import unittest

import requests

from Common import read_config, public
from Common import public

rc=read_config.Read_config()
login= public.Public_Method()
class BankManagement(unittest.TestCase):
    def setUp(self):
        global url,  resource
        url=rc.get_http('http')
        resource=rc.get_http('resource')

    def test_bank_swift_US(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'US',
                'account_name':'John Smith',
                'account_number':'123',
                'swift_code':'ICBCUSBJ',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertEqual(response.status_code,200,'response status code not as 200')
            self.assertEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e
    def test_bank_swift_AU(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'AU',
                'account_name':'John Smith',
                'account_number':'12345678',
                'swift_code':'ICBCAUBJ',
                'bsb':'111222'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertEqual(response.status_code,200,'response status code not as 200')
            self.assertEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e

    def test_bank_swift_CN(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'CN',
                'account_name':'JiangZhi',
                'account_number':'123456789',
                'swift_code':'ICBCCNBJ',
                #'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertEqual(response.status_code,200,'response status code not as 200')
            self.assertEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e

    def test_bank_local_US(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'local',
                'bank_country_code':'US',
                'account_name':'John Smith',
                'account_number':'123',
                #'swift_code':'ICBCUSBJ',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertEqual(response.status_code,200,'response status code not as 200')
            self.assertEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e

    def test_bank_paymentMethodInvalid(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'Something',
                'bank_country_code':'US',
                'account_name':'John Smith',
                'account_number':'123',
                'swift_code':'ICBCUSBJ',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertNotEqual(response.status_code,200,'response status code not as 200')
            self.assertNotEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e
    def test_bank_swift_US_missAba(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'US',
                'account_name':'John Smith',
                'account_number':'123',
                'swift_code':'ICBCUSBJ',
                #'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertNotEqual(response.status_code,200,'response status code not as 200')
            self.assertNotEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e

    def test_bank_swift_US_A.N._outOfBoundary(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'US',
                'account_name':'John Smith',
                'account_number':'1234567890123456789',
                'swift_code':'ICBCUSBJ',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertNotEqual(response.status_code,200,'response status code not as 200')
            self.assertNotEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e
    def test_bank_swift_US_missSwiftCode(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'US',
                'account_name':'John Smith',
                'account_number':'123',
                #'swift_code':'ICBCUSBJ',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertNotEqual(response.status_code,200,'response status code not as 200')
            self.assertNotEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e

    def test_bank_swift_US_swiftCodeInvalid(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'US',
                'account_name':'John Smith',
                'account_number':'123',
                'swift_code':'ICBCUTSBJ',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertNotEqual(response.status_code,200,'response status code not as 200')
            self.assertNotEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e

    def test_bank_swift_US_swiftCodeInvalid_outOfBoundary(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'US',
                'account_name':'John Smith',
                'account_number':'123',
                'swift_code':'ICBCUSBJkdsfksdk',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertNotEqual(response.status_code,200,'response status code not as 200')
            self.assertNotEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e

    def test_bank_swift_countryCodeInvalid(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'USHK',
                'account_name':'John Smith',
                'account_number':'123',
                'swift_code':'ICBCUSBJ',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertNotEqual(response.status_code,200,'response status code not as 200')
            self.assertNotEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e

    def test_bank_swift_accountNameInvalid(self):
        u"""Bank信息API"""
        try:
            self.info_url=url+resoure
            print("url:"+self.info_url)
            data={
                'payment_method':'SWIFT',
                'bank_country_code':'US',
                'account_name':'John Smithsldfjkl;ajfelkja',
                'account_number':'123',
                'swift_code':'ICBCUSBJ',
                'aba':'11122233A'
            }
            print('input data for bank is ', data)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,data=json.dumps(data),headers=headers)
            print(response.status_code)
            print('API response', response.json())
            self.assertNotEqual(response.status_code,200,'response status code not as 200')
            self.assertNotEqual(response.json.success, 'Bank Detail saved')
        except requests.RequestException as e:
            raise e


    

if __name__ == '__main__':
    unittest.main()
    #AccountManagement.test_API response()