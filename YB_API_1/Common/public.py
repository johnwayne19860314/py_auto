#-*- coding:utf-8 -*-
import unittest
import requests
import json
from Common import read_config

rc=read_config.Read_config()
global url,resource
url=rc.get_http('http')
resource=rc.get_http('resource')
class Public_Method(unittest.TestCase):

    u""" :keyword
    Login：登陆，返回session，用于其他的接口使用
    """
    def test_login(self):
        u"""登陆接API"""
        try:
            self.login_url=url+resource+"/spb/user/user/login.action"
            params={
                "account":"testone",
                "pasword":"123456"
            }
            headers={
                'content-type': 'application/json'
                }
            # with requests.session() as session:
            session=requests.session()
            data=json.dumps(params)
            response=session.post(self.login_url,data=data,headers=headers)
            #将CookieJar转为字典
            session.cookies=requests.utils.dict_from_cookiejar(response.cookies)
            # print(session.cookies)
            return session.
        except Exception as e:cookies
            raise e

    def getMsg(self):
        try:
            msg_url=url+resource+"/spb/user/system/sendMsg.action"
            print(msg_url)
            session=requests.session()
            params={'number':'18207278423'}
            headers={
                'content-type': 'application/json'
            }
            response=session.post(msg_url, params=params, headers=headers)
            print(response.status_code)
            session.cookies=requests.utils.dict_from_cookiejar(response.cookies)
            print(session.cookies['JSESSIONID'])
            return session.cookies['JSESSIONID']
        except requests.HTTPError as e:
            raise e

if __name__ == '__main__':
    unittest.main()


