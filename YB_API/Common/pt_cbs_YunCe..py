#coding=utf-8
import requests
import md5
import hashlib
import json
#from datetime import *
from datetime import datetime,timedelta
from collections import OrderedDict
import threading
import random
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
        print urlBase+url
        print json.dumps(data)
        #cookies=cookie.test_login()
        response=requests.post(urlBase+url,data=json.dumps(data),headers=headers)
        #return response
        #print response.status_code, json.loads(response.text)['data_info']['amount']
        if url == 'reckon':
            print '----  reckon-------',response.status_code, response.json()['data_info']['reckon_price']
            #total = response.json()['data_info']['amount']
            orderVerify['total'] = response.json()['data_info']['reckon_price']
        elif url == 'order/verify':
            print '------ verify -----', response.status_code, response.text
            orderConfirm['order_id'] = response.json()['data_info']['order_id']
        else:
            print '------ confirm -----', response.status_code, response.text
    # raise e and stop the reqeust if uncomment
    except requests.ConnectionError as e:
        #raise e
        print 'requests.ConnectionError' ,e
        #continue
    except requests.RequestException as e:
        #raise e
        print 'requests.RequestException',e
    except requests.Timeout as e:
        #raise e
        print 'requests.Timeout' ,e
    except :
        #continue
        print 'exception'


    #count  the no. of threads, #count_1    the no. of times to request the url,    oriIf  the request data id
def getThreads(count_thread,count_1, reqRange):
    threads = []
    j = 0
    while j < count_thread:
        print '&&&&&&&&&&&&&&&&&------the thread is ----  ',j
        t = threading.Thread(target=order_reqeusts, args=(count_1,reqRange))
        threads.append(t)
        j+=1
    return threads

def gennerator():
    codelist = [{"state":'河北省',"city":'沧州市',"district":'运河区',"code":'130903'}
                ]
    #print 'the length of code list', len(codelist)
    #id = codelist[random.randint(0,len(codelist))]['code'] #地区项
    id = codelist[0]['code']  # 地区项
    id = id + str(random.randint(1930,2013)) #年份项
    da  = date.today()+timedelta(days=random.randint(1,366)) #月份和日期项
    id = id + da.strftime('%m%d')
    id = id+ str(random.randint(100,300))#，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
    checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
    for i in range(0,len(id)):
       count = count +int(id[i])*weight[i]
    id = id + checkcode[str(count%11)] #算出校验码
    return id

def getEffectTime(n):
    now = datetime.now()
    delta = timedelta(days=n)
    n_days = now + delta
    return n_days.strftime('%Y-%m-%d')

def order_reqeusts(request_times, requestRange):
    #for i in range request_times:
    i = 0
    while i < request_times:

        try:
            print '&&&&&&&&&&&&&&&&&------the reqeust  is ------  ', i
           # n = random.choice(daysArr)
            reqeustId = str(random.randint(0, requestRange))
            orderVerify['request_id'] = reqeustId
        
            #body_post(reckon_url, orderReckon)
            body_post(verify_url, orderVerify)
            body_post(confirm_url, orderConfirm)
        except: # continue the process even exception
            continue
        i += 1

if __name__ == '__main__':

    channelName = 'anyi'
    productId = "YAIC20170629001"
    month_ = '10'
    shares_ = 1

    # orderReckon = {
    #     "appid": 'anyi',
    #     "product_id": 'YAIC20170629001',
    #     "params": {
    #         "city_code": 1222,
    #         "month": '10',
    #         "shares": 1

    #     }
    # }
    orderVerify = {

         "appid": "anyi",
        "total": "216",
        "insured": [
            {
                "name": "张测试",
                "card_id": "11010119800101007X",
                "card_type": "97"
            }
        ],
        "product": {
            "id": "HTIC20171205001",
            "amt": "1800000",
            "sign": "产品标记1",
            "end_tm": "2017-12-22 12:00:00",
            "to_area": "广州",
            "start_tm": "2017-12-20 12:00:00",
            "from_area": "上海",
            "bill_number": "ASPER B/L",
            "charge_rate": "0.11987",
            "fregiht_item": "土木材料",
            "freight_type": "SX001401",
            "original_sum": 9,
            "package_code": "A",
            "premium_prit": "02",
            "invoice_money": "2000000",
            "date_prit_type": "1",
            "freight_detail": "SX00140001",
            "traffic_number": "SD23456",
            "transport_type": "SX001501",
            "transport_detail": "08",
            "pack_and_quantity": "02*20GP",
            "survey_address_id": "900073934"
        },
        "additional": {
            "effect": "2017-12-20"
        },
        "applicant": {
            "name": "张测试",
            "phone": "11111111111111",
            "address": "sdf",
            "card_id": "11010119800101007X",
            "card_type": "97",
            "account_bank": "上海银行",
            "account_number": "erwrerte213423",
            "is_tax_invoice": 1
        },
        "request_id": "2017071x11x3141311210011"

    }
    orderConfirm = {
        "appid": channelName,
        "order_id": "12345",  # 4
        "notify_url": 'http://test.spb.riskeys.com/spb/app/certInfo/savePolicyNoByConfiraction',  # 回调地址
        # notify_url:'http://open.anyi-tech.com/spb/app/certInfo/savePolicyNoByConfiraction', #回调地址
        "pay_info": {},
        "whether": "1"
    }
   # print orderReckon
    print '-----------------------'
    print orderVerify
    urlBase = 'http://127.0.0.1:9106/'
   # reckon_url = 'reckon'
    verify_url = 'order/verify'
    confirm_url = 'order/confirm'
    #request_times = 1
   # daysArr = [50,51,52,53,54,55,56,57,58,59,40,41,42,43,44,45,46,47,48]
    numOfThreads = 5
    eachThreadLoop = 20
    threads = getThreads(numOfThreads, eachThreadLoop, 1111111111111111111111111111111111)

    dt = datetime.now()
    print '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f')
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    dt_1 = datetime.now()
    print '(%Y-%m-%d %H:%M:%S %f): ', dt_1.strftime('%Y-%m-%d %H:%M:%S %f')
    print 'it take this much time to finish  ', dt_1 - dt
    var = ("hours","minutes","seconds")
    time2sec = lambda x:int(timedelta(**{k:int(v) for k,v in zip(var,x.strip().split(":"))}).total_seconds())
    start_time_int = time2sec(dt.strftime('%H:%M:%S'))
    end_time_int = time2sec(dt_1.strftime('%H:%M:%S'))
    print 'sart_time_int', start_time_int
    print 'end_time_int', end_time_int
    print 'all loops takes time ',end_time_int - start_time_int
    print 'all loops', numOfThreads*eachThreadLoop
    print 'each loops takes time in even ',(end_time_int - start_time_int)/(numOfThreads*eachThreadLoop)

