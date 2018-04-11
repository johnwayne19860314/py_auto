#coding=utf-8
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
def body_post(url,data):
    try:
        headers={
        'content-type': 'application/json'
            }
        #cookies=cookie.test_login()
        response=requests.post(url,data=json.dumps(data),headers=headers)
        #return response
        print response.status_code
    except requests.ConnectionError as e:
        raise e
    except requests.RequestException as e:
        raise e
    except requests.Timeout as e:
        raise e

def getMD5Sign(orderData):
    src = json.dumps(orderData,separators=(',', ':')) + secKey
    #src = secKey
    #m1 = md5.new()
    m1 = hashlib.md5()
    m1.update(src)
    sign_ = m1.hexdigest().upper()
    #sign_ = m1.hex().upper()
    return sign_

def lldCreateOrder(count, oriId):
    i = 0
    while i < count:
        print 'it is the time %s   '%oriId ,i
        orderData['id'] = oriId + str(i)
        sign_ = getMD5Sign(orderData)
        createOrderInputData = {
            'appId': "lld",
            'data': orderData,
            'sign': sign_  # 签名 (需加密,加密规则见demo) 说明：   md5(data+key).toUpperCase()
        }
        body_post(reqeustUrl, createOrderInputData)
        i += 1



# orderData = OrderedDict([(),(),(),(),()]){
#     'id':"id111222",			      #唯一标识id（必要）
#     'name':"abc",   			#借款人名称(必要)
#     'phone':"18070254856",     #借款人电话(必要)
#     'cardNo':"310115188548586",#借款人证件号(必要)
#     'lendingTime':"2015-12-1 12:25:22",#放款时间,
#     'rate':1
# }



#print getMD5Sign(orderData)
#print 'the string of data is ', json.dumps(orderData,separators=(',', ':'))

#reqeustUrl = 'http://127.0.0.1:9010/ws_lld/order/createOrder'

#count  the no. of threads, #count_1    the no. of times to request the url,    oriIf  the request data id
def getThreads(count,count_1, oriId):
    threads = []
    j = 0
    while j < count:
        t = threading.Thread(target=lldCreateOrder, args=(count_1,oriId+ str(j)))
        threads.append(t)
        j+=1
    return threads


if __name__ == '__main__':
    #seems like the thread count max limit is 1000
    threads = getThreads(800,500,u'ATX777')

    orderData = OrderedDict([('id', "id111222"), ('name', "abc"), ('phone', "18070254856"),
                             ('cardNo', "310115188548586"), ('lendingTime', "2015-12-1 12:25:22"), ('rate', 1)])
    secKey = 'AsD35LtGk'
    reqeustUrl = 'http://120.27.145.6:9010/ws_lld/order/createOrder'

    dt = datetime.now()
    print '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f')
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    dt_1 = datetime.now()
    print '(%Y-%m-%d %H:%M:%S %f): ', dt_1.strftime('%Y-%m-%d %H:%M:%S %f')
    print 'it take this much time to finish  ', dt_1 - dt