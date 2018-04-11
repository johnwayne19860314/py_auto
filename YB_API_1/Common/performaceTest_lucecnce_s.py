# -*- coding:utf-8-*-
import requests
import md5
import hashlib
import json
from datetime import *
from collections import OrderedDict
import threading
# # python2.7
# pwd = "xxx" + chr(163) + "fj"
# checkcode = hashlib.md5(pwd).hexdigest()
# print
# checkcode  # ea25a328180680aab82b2ef8c456b4ce
#
# # python3.6
# pwd = "xxx" + chr(163) + "fj"
# checkcode = hashlib.md5(pwd.encode("utf-8")).hexdigest()
# print(checkcode)  # b517e074034d1913b706829a1b9d1b67

u"""
request.post，不返回sessiong信息的方法
:param: url：连接
data: 带参数
"""
def urlReqeust(url,data,method):
    try:
        headers={
            'content-type': 'application/json'
        }
        #cookies=cookie.test_login()
        print url
        if(method == 'post'):
            response=requests.post(url,data=json.dumps(data),headers=headers)
        elif(method == 'put'):
            response = requests.put(url, data=json.dumps(data), headers=headers)
        #return response
        print response.status_code
        print response.json()
    except requests.RequestException as e:
        raise e
    except requests.Timeout as e:
        raise e





orderData = {
    "id":"410001004E5D00E966590000",
    "appid":"anyi",
    "product_id":"CCIC20170622001",
    "request_id":"6F7201004E5D00E966590000",
    "request":[
        {
            "id":"410001004E5DC9E866590000",
            "appid":"",
            "contact":{
                "phone":"18207278423",
                "name":"111111"
            },
            "product":{
                "id":"CCIC20170622001",
                "name":"",
                "product_type":"C",
                "ensure_plan":"方案一",
                "vendor_name":"保险公司"
            },
        "applicant":{
                "name":"韩晓清",
                "card_type":"身份证",
                "card_id":"",
                "sex":"男",
                "birthday":"",
                "phone":"18207278423",
                "other_contact":"",
                "email":"",
                "address":""
        },
        "insured":[
            {
            "relation":"本人",
            "profession":"",
            "name":"韩晓清",
            "card_type":"身份证",
            "card_id":"",
            "sex":"男",
            "birthday":"",
            "phone":"18207278423",
            "other_contact":"",
            "email":"",
            "address":""
            }
        ],
        "addtional":{
            "effect":"2017-07-13",
            "payment_type":"1",
            "payment_period_number":"1"
        },
        "beneficiary":'',
        "total":100,
        "premiums_receivable":1,
        "brokerage":100,
        "brokerage_ratio":"1",
        "insurance_no":"",
        "merchant":"",
        "service_staff":"服务",
        "remark":'''[{"保障计划":"A款","保障数量":"1份"}]''',
        "policy_time":"2017-07-19",
        "files":[
        ],
        "dealStatus":"processed"
        }
    ],
    "attach":[
        None
    ],
    "status":"payed",
    "created_time":"1499916544",
    "created_id":"null",
    "method_type":"C"
}


#print getMD5Sign(orderData)
#print 'the string of data is ', json.dumps(orderData,separators=(',', ':'))
id = '410001004E5D00E966590000'
id1 = '410001004E5DC9E866590000'

#reqeustUrl = 'http://127.0.0.1:9010/ws_lld/order/createOrder'

if __name__ == '__main__':
    dt = datetime.now()
    print '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f')
    i = 0
    while i < 30000:
        id_1 = id + str(i)
        id_2 = id1 + str(i)
        orderData[id] = id_1
        orderData['request'][0]['id'] = id_2
        reqeustUrl = 'http://118.178.134.70:9200/ldl_index/orderList/{0}'.format(id_1)
        urlReqeust(reqeustUrl,orderData,'put')
        i += 1
    dt_1 = datetime.now()
    print '(%Y-%m-%d %H:%M:%S %f): ', dt_1.strftime('%Y-%m-%d %H:%M:%S %f')
    print 'it take this much time to finish  ', dt_1 - dt