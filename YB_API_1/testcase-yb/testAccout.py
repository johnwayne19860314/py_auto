# -*- coding:utf-8 -*-
import unittest
from Common import read_excel,read_config
from Common import logManage,operation

rc=read_config.Read_config()
log=logManage.LogMgr("account")
class MyTestCase(unittest.TestCase):
    def test_account(self):
        try:
            u"""账号管理"""
            #读取excel数据，获取list集合
            testdata=read_excel.read_Excel("Sheet1")
            #读取配置文件，获取url
            http_url=rc.get_http("http")
            for i in range(len(testdata)):
                name=testdata[i][0]
                url=testdata[i][1]
                data=testdata[i][2]
                type=testdata[i][3]
                api_url=http_url+url
                #print(name,url,data,type)
                if type=="post" and data=="null":
                    response=operation.post(api_url,name)
                    if response.status_code==200:
                        print(name,"执行成功",response.text)
                    else:
                        log.debug(response.raise_for_status())
                else:
                    operation.body_post(api_url,data,name)
                    if response.status_code==200:
                        print(name,"执行成功",response.json())
                    else:
                        log.debug(response.raise_for_status())

        except Exception as e:
            raise log.debug(e)




if __name__ == '__main__':
    unittest.main()
