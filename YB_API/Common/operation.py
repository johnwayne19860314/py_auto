# -*- coding:utf-8-*-
import requests
import json
from Common import public
from Common import logManage

log=logManage.LogMgr("Logs")
cookie=public.Public_Method()

u"""
request.get: get请求
url： 请求的url
params:请求参数
"""
def get(url,params=None):
    try:
        response=requests.get(url,params=params,timeout=1)
        return response
    except ConnectionError as e:
        raise log.info(e)
    except requests.RequestException as e:
        raise log.info(e)
    except requests.Timeout as e:
        raise log.info(e)

u"""
request.post，不返回sessiong信息的方法
:param: url：连接
data: 带参数
"""
def body_post(url,data,method):
    try:
        headers={
        'content-type': 'application/json'
            }
        cookies=cookie.test_login()
        response=requests.post(url,data=json.dumps(data),headers=headers,cookies=cookies)
        return response
    except ConnectionError as e:
        raise log.info(e)
    except requests.RequestException as e:
        raise log.info(e)
    except requests.Timeout as e:
        raise log.info(e)

u"""
不带参数的post方法
"""
def post(url,method):
    try:
        headers={
        'content-type': 'application/json'
        }
        cookies=cookie.test_login()
        response=requests.post(url,headers=headers,cookies=cookies)
        return response
    except ConnectionError as e:
        raise log.info(e)
    except requests.RequestException as e:
        raise log.info(e)
    except requests.Timeout as e:
        raise log.info(e)
