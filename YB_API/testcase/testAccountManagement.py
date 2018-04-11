#-*- coding:utf-8 -*-
import json
import unittest

import requests

from Common import read_config, public
from Common import public

rc=read_config.Read_config()
login= public.Public_Method()
class AccountManagement(unittest.TestCase):
    def setUp(self):
        global url,  resource
        url=rc.get_http('http')
        resource=rc.get_http('resource')

    def test_userinfo(self):
        u"""获取用户信息API"""
        try:
            self.info_url=url+resource+"/spb/user/user/userInfo.action"
            print("url:"+self.info_url)
            session=requests.session()
            cookie=login.test_login()#获取登陆接口的session
            print('cookie from login', cookie)
            headers={
                'content-type': 'application/json'
                     }
            response=session.post(self.info_url,headers=headers,cookies=cookie)
            print(response.status_code)
            print('userinfo', response.json())
        except requests.RequestException as e:
            raise e

    def test_editUser(self):
        u"""账户修改"""
        try:
            edit_url=url+resource+"/spb/user/user/editUser.action"
            session=requests.session()
            cookie=login.test_login()
            data={
                'account':'18207278423',
                'email':'xiaoqing.han@anyi-tech.com'
           }
            headers={
                'content-type': 'application/json'
            }
            response=session.post(edit_url, data=json.dumps(data),headers=headers,cookies=cookie)
            print(response.status_code)
            print(response.json())
        except requests.RequestException as e:
             raise e

    u'''获取短信平台验证码被挡住
    def test_editTelphone(self):
        u"""修改手机号"""
        try:
          tel_url=url+resource+"/spb/user/user/editTelphone.action"
          print(tel_url)
          number='18207278423'
          verifyCode=str(login.test_getMsg())
          print(verifyCode['JSESSIONID'])
          params={
              'telephone':number,
              'verifyCode':verifyCode
                  }
          headers={
                'content-type': 'application/json'
            }
          response=requests.post(tel_url,data=json.dumps(params),headers=headers)
          print(response.status_code)
        except requests.RequestException as e:
             raise e
    '''

if __name__ == '__main__':
    unittest.main()
    #AccountManagement.test_userinfo()