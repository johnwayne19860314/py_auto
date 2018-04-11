#coding=utf-8
import requests
import md5
import hashlib
import json
from datetime import *
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
            print response.status_code, response.json()['data_info']['reckon_price']
            #total = response.json()['data_info']['amount']
            orderVerify['total'] = response.json()['data_info']['reckon_price']
        elif url == 'verify':
            print response.status_code, response.text
            orderConfirm['order_id'] = response.json()['data_info']['order_id']
    except requests.ConnectionError as e:
        raise e
    except requests.RequestException as e:
        raise e
    except requests.Timeout as e:
        raise e


#count  the no. of threads, #count_1    the no. of times to request the url,    oriIf  the request data id
def getThreads(count,count_1):
    threads = []
    j = 0
    while j < count:
        t = threading.Thread(target=order_reqeusts, args=(count_1))
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

def order_reqeusts(request_times):
    print 'aaa'



citiCodeJSON = {
    "110100": {
        "city_name": "北京市",
        "city_code": 110100
    },
    "120100": {
        "city_name": "天津市",
        "city_code": 120100
    },
    "130100": {
        "city_name": "石家庄市",
        "city_code": 130100
    },
    "130200": {
        "city_name": "唐山市",
        "city_code": 130200
    },
    "130300": {
        "city_name": "秦皇岛市",
        "city_code": 130300
    },
    "130400": {
        "city_name": "邯郸市",
        "city_code": 130400
    },
    "130500": {
        "city_name": "邢台市",
        "city_code": 130500
    },
    "130600": {
        "city_name": "保定市",
        "city_code": 130600
    },
    "130700": {
        "city_name": "张家口市",
        "city_code": 130700
    },
    "130800": {
        "city_name": "承德市",
        "city_code": 130800
    },
    "130900": {
        "city_name": "沧州市",
        "city_code": 130900
    },
    "131000": {
        "city_name": "廊坊市",
        "city_code": 131000
    },
    "131100": {
        "city_name": "衡水市",
        "city_code": 131100
    },
    "140100": {
        "city_name": "太原市",
        "city_code": 140100
    },
    "140200": {
        "city_name": "大同市",
        "city_code": 140200
    },
    "140300": {
        "city_name": "阳泉市",
        "city_code": 140300
    },
    "140400": {
        "city_name": "长治市",
        "city_code": 140400
    },
    "140500": {
        "city_name": "晋城市",
        "city_code": 140500
    },
    "140600": {
        "city_name": "朔州市",
        "city_code": 140600
    },
    "140700": {
        "city_name": "晋中市",
        "city_code": 140700
    },
    "140800": {
        "city_name": "运城市",
        "city_code": 140800
    },
    "140900": {
        "city_name": "忻州市",
        "city_code": 140900
    },
    "141000": {
        "city_name": "临汾市",
        "city_code": 141000
    },
    "141100": {
        "city_name": "吕梁市",
        "city_code": 141100
    },
    "150100": {
        "city_name": "呼和浩特市",
        "city_code": 150100
    },
    "150200": {
        "city_name": "包头市",
        "city_code": 150200
    },
    "150300": {
        "city_name": "乌海市",
        "city_code": 150300
    },
    "150400": {
        "city_name": "赤峰市",
        "city_code": 150400
    },
    "150500": {
        "city_name": "通辽市",
        "city_code": 150500
    },
    "150600": {
        "city_name": "鄂尔多斯市",
        "city_code": 150600
    },
    "150700": {
        "city_name": "呼伦贝尔市",
        "city_code": 150700
    },
    "150800": {
        "city_name": "巴彦淖尔市",
        "city_code": 150800
    },
    "150900": {
        "city_name": "乌兰察布市",
        "city_code": 150900
    },
    "152200": {
        "city_name": "兴安盟",
        "city_code": 152200
    },
    "152500": {
        "city_name": "锡林郭勒盟",
        "city_code": 152500
    },
    "152900": {
        "city_name": "阿拉善盟",
        "city_code": 152900
    },
    "210100": {
        "city_name": "沈阳市",
        "city_code": 210100
    },
    "210200": {
        "city_name": "大连市",
        "city_code": 210200
    },
    "210300": {
        "city_name": "鞍山市",
        "city_code": 210300
    },
    "210400": {
        "city_name": "抚顺市",
        "city_code": 210400
    },
    "210500": {
        "city_name": "本溪市",
        "city_code": 210500
    },
    "210600": {
        "city_name": "丹东市",
        "city_code": 210600
    },
    "210700": {
        "city_name": "锦州市",
        "city_code": 210700
    },
    "210800": {
        "city_name": "营口市",
        "city_code": 210800
    },
    "210900": {
        "city_name": "阜新市",
        "city_code": 210900
    },
    "211000": {
        "city_name": "辽阳市",
        "city_code": 211000
    },
    "211100": {
        "city_name": "盘锦市",
        "city_code": 211100
    },
    "211200": {
        "city_name": "铁岭市",
        "city_code": 211200
    },
    "211300": {
        "city_name": "朝阳市",
        "city_code": 211300
    },
    "211400": {
        "city_name": "葫芦岛市",
        "city_code": 211400
    },
    "220100": {
        "city_name": "长春市",
        "city_code": 220100
    },
    "220200": {
        "city_name": "吉林市",
        "city_code": 220200
    },
    "220300": {
        "city_name": "四平市",
        "city_code": 220300
    },
    "220400": {
        "city_name": "辽源市",
        "city_code": 220400
    },
    "220500": {
        "city_name": "通化市",
        "city_code": 220500
    },
    "220600": {
        "city_name": "白山市",
        "city_code": 220600
    },
    "220700": {
        "city_name": "松原市",
        "city_code": 220700
    },
    "220800": {
        "city_name": "白城市",
        "city_code": 220800
    },
    "222400": {
        "city_name": "延边朝鲜族自治州",
        "city_code": 222400
    },
    "230100": {
        "city_name": "哈尔滨市",
        "city_code": 230100
    },
    "230200": {
        "city_name": "齐齐哈尔市",
        "city_code": 230200
    },
    "230300": {
        "city_name": "鸡西市",
        "city_code": 230300
    },
    "230400": {
        "city_name": "鹤岗市",
        "city_code": 230400
    },
    "230500": {
        "city_name": "双鸭山市",
        "city_code": 230500
    },
    "230600": {
        "city_name": "大庆市",
        "city_code": 230600
    },
    "230700": {
        "city_name": "伊春市",
        "city_code": 230700
    },
    "230800": {
        "city_name": "佳木斯市",
        "city_code": 230800
    },
    "230900": {
        "city_name": "七台河市",
        "city_code": 230900
    },
    "231000": {
        "city_name": "牡丹江市",
        "city_code": 231000
    },
    "231100": {
        "city_name": "黑河市",
        "city_code": 231100
    },
    "231200": {
        "city_name": "绥化市",
        "city_code": 231200
    },
    "232700": {
        "city_name": "大兴安岭地区",
        "city_code": 232700
    },
    "310100": {
        "city_name": "上海市",
        "city_code": 310100
    },
    "320100": {
        "city_name": "南京市",
        "city_code": 320100
    },
    "320200": {
        "city_name": "无锡市",
        "city_code": 320200
    },
    "320300": {
        "city_name": "徐州市",
        "city_code": 320300
    },
    "320400": {
        "city_name": "常州市",
        "city_code": 320400
    },
    "320500": {
        "city_name": "苏州市",
        "city_code": 320500
    },
    "320600": {
        "city_name": "南通市",
        "city_code": 320600
    },
    "320700": {
        "city_name": "连云港市",
        "city_code": 320700
    },
    "320800": {
        "city_name": "淮安市",
        "city_code": 320800
    },
    "320900": {
        "city_name": "盐城市",
        "city_code": 320900
    },
    "321000": {
        "city_name": "扬州市",
        "city_code": 321000
    },
    "321100": {
        "city_name": "镇江市",
        "city_code": 321100
    },
    "321200": {
        "city_name": "泰州市",
        "city_code": 321200
    },
    "321300": {
        "city_name": "宿迁市",
        "city_code": 321300
    },
    "330100": {
        "city_name": "杭州市",
        "city_code": 330100
    },
    "330200": {
        "city_name": "宁波市",
        "city_code": 330200
    },
    "330300": {
        "city_name": "温州市",
        "city_code": 330300
    },
    "330400": {
        "city_name": "嘉兴市",
        "city_code": 330400
    },
    "330500": {
        "city_name": "湖州市",
        "city_code": 330500
    },
    "330600": {
        "city_name": "绍兴市",
        "city_code": 330600
    },
    "330700": {
        "city_name": "金华市",
        "city_code": 330700
    },
    "330800": {
        "city_name": "衢州市",
        "city_code": 330800
    },
    "330900": {
        "city_name": "舟山市",
        "city_code": 330900
    },
    "331000": {
        "city_name": "台州市",
        "city_code": 331000
    },
    "331100": {
        "city_name": "丽水市",
        "city_code": 331100
    },
    "340100": {
        "city_name": "合肥市",
        "city_code": 340100
    },
    "340200": {
        "city_name": "芜湖市",
        "city_code": 340200
    },
    "340300": {
        "city_name": "蚌埠市",
        "city_code": 340300
    },
    "340400": {
        "city_name": "淮南市",
        "city_code": 340400
    },
    "340500": {
        "city_name": "马鞍山市",
        "city_code": 340500
    },
    "340600": {
        "city_name": "淮北市",
        "city_code": 340600
    },
    "340700": {
        "city_name": "铜陵市",
        "city_code": 340700
    },
    "340800": {
        "city_name": "安庆市",
        "city_code": 340800
    },
    "341000": {
        "city_name": "黄山市",
        "city_code": 341000
    },
    "341100": {
        "city_name": "滁州市",
        "city_code": 341100
    },
    "341200": {
        "city_name": "阜阳市",
        "city_code": 341200
    },
    "341300": {
        "city_name": "宿州市",
        "city_code": 341300
    },
    "341500": {
        "city_name": "六安市",
        "city_code": 341500
    },
    "341600": {
        "city_name": "亳州市",
        "city_code": 341600
    },
    "341700": {
        "city_name": "池州市",
        "city_code": 341700
    },
    "341800": {
        "city_name": "宣城市",
        "city_code": 341800
    },
    "350100": {
        "city_name": "福州市",
        "city_code": 350100
    },
    "350200": {
        "city_name": "厦门市",
        "city_code": 350200
    },
    "350300": {
        "city_name": "莆田市",
        "city_code": 350300
    },
    "350400": {
        "city_name": "三明市",
        "city_code": 350400
    },
    "350500": {
        "city_name": "泉州市",
        "city_code": 350500
    },
    "350600": {
        "city_name": "漳州市",
        "city_code": 350600
    },
    "350700": {
        "city_name": "南平市",
        "city_code": 350700
    },
    "350800": {
        "city_name": "龙岩市",
        "city_code": 350800
    },
    "350900": {
        "city_name": "宁德市",
        "city_code": 350900
    },
    "360100": {
        "city_name": "南昌市",
        "city_code": 360100
    },
    "360200": {
        "city_name": "景德镇市",
        "city_code": 360200
    },
    "360300": {
        "city_name": "萍乡市",
        "city_code": 360300
    },
    "360400": {
        "city_name": "九江市",
        "city_code": 360400
    },
    "360500": {
        "city_name": "新余市",
        "city_code": 360500
    },
    "360600": {
        "city_name": "鹰潭市",
        "city_code": 360600
    },
    "360700": {
        "city_name": "赣州市",
        "city_code": 360700
    },
    "360800": {
        "city_name": "吉安市",
        "city_code": 360800
    },
    "360900": {
        "city_name": "宜春市",
        "city_code": 360900
    },
    "361000": {
        "city_name": "抚州市",
        "city_code": 361000
    },
    "361100": {
        "city_name": "上饶市",
        "city_code": 361100
    },
    "370100": {
        "city_name": "济南市",
        "city_code": 370100
    },
    "370200": {
        "city_name": "青岛市",
        "city_code": 370200
    },
    "370300": {
        "city_name": "淄博市",
        "city_code": 370300
    },
    "370400": {
        "city_name": "枣庄市",
        "city_code": 370400
    },
    "370500": {
        "city_name": "东营市",
        "city_code": 370500
    },
    "370600": {
        "city_name": "烟台市",
        "city_code": 370600
    },
    "370700": {
        "city_name": "潍坊市",
        "city_code": 370700
    },
    "370800": {
        "city_name": "济宁市",
        "city_code": 370800
    },
    "370900": {
        "city_name": "泰安市",
        "city_code": 370900
    },
    "371000": {
        "city_name": "威海市",
        "city_code": 371000
    },
    "371100": {
        "city_name": "日照市",
        "city_code": 371100
    },
    "371200": {
        "city_name": "莱芜市",
        "city_code": 371200
    },
    "371300": {
        "city_name": "临沂市",
        "city_code": 371300
    },
    "371400": {
        "city_name": "德州市",
        "city_code": 371400
    },
    "371500": {
        "city_name": "聊城市",
        "city_code": 371500
    },
    "371600": {
        "city_name": "滨州市",
        "city_code": 371600
    },
    "371700": {
        "city_name": "菏泽市",
        "city_code": 371700
    },
    "410100": {
        "city_name": "郑州市",
        "city_code": 410100
    },
    "410200": {
        "city_name": "开封市",
        "city_code": 410200
    },
    "410300": {
        "city_name": "洛阳市",
        "city_code": 410300
    },
    "410400": {
        "city_name": "平顶山市",
        "city_code": 410400
    },
    "410500": {
        "city_name": "安阳市",
        "city_code": 410500
    },
    "410600": {
        "city_name": "鹤壁市",
        "city_code": 410600
    },
    "410700": {
        "city_name": "新乡市",
        "city_code": 410700
    },
    "410800": {
        "city_name": "焦作市",
        "city_code": 410800
    },
    "410900": {
        "city_name": "濮阳市",
        "city_code": 410900
    },
    "411000": {
        "city_name": "许昌市",
        "city_code": 411000
    },
    "411100": {
        "city_name": "漯河市",
        "city_code": 411100
    },
    "411200": {
        "city_name": "三门峡市",
        "city_code": 411200
    },
    "411300": {
        "city_name": "南阳市",
        "city_code": 411300
    },
    "411400": {
        "city_name": "商丘市",
        "city_code": 411400
    },
    "411500": {
        "city_name": "信阳市",
        "city_code": 411500
    },
    "411600": {
        "city_name": "周口市",
        "city_code": 411600
    },
    "411700": {
        "city_name": "驻马店市",
        "city_code": 411700
    },
    "419001": {
        "city_name": "济源",
        "city_code": 419001
    },
    "420100": {
        "city_name": "武汉市",
        "city_code": 420100
    },
    "420200": {
        "city_name": "黄石市",
        "city_code": 420200
    },
    "420300": {
        "city_name": "十堰市",
        "city_code": 420300
    },
    "420500": {
        "city_name": "宜昌市",
        "city_code": 420500
    },
    "420600": {
        "city_name": "襄樊市",
        "city_code": 420600
    },
    "420700": {
        "city_name": "鄂州市",
        "city_code": 420700
    },
    "420800": {
        "city_name": "荆门市",
        "city_code": 420800
    },
    "420900": {
        "city_name": "孝感市",
        "city_code": 420900
    },
    "421000": {
        "city_name": "荆州市",
        "city_code": 421000
    },
    "421100": {
        "city_name": "黄冈市",
        "city_code": 421100
    },
    "421200": {
        "city_name": "咸宁市",
        "city_code": 421200
    },
    "421300": {
        "city_name": "随州市",
        "city_code": 421300
    },
    "422800": {
        "city_name": "恩施土家族苗族自治州",
        "city_code": 422800
    },
    "429004": {
        "city_name": "仙桃",
        "city_code": 429004
    },
    "429005": {
        "city_name": "潜江",
        "city_code": 429005
    },
    "429006": {
        "city_name": "天门",
        "city_code": 429006
    },
    "429021": {
        "city_name": "神农架林区",
        "city_code": 429021
    },
    "430100": {
        "city_name": "长沙市",
        "city_code": 430100
    },
    "430200": {
        "city_name": "株洲市",
        "city_code": 430200
    },
    "430300": {
        "city_name": "湘潭市",
        "city_code": 430300
    },
    "430400": {
        "city_name": "衡阳市",
        "city_code": 430400
    },
    "430500": {
        "city_name": "邵阳市",
        "city_code": 430500
    },
    "430600": {
        "city_name": "岳阳市",
        "city_code": 430600
    },
    "430700": {
        "city_name": "常德市",
        "city_code": 430700
    },
    "430800": {
        "city_name": "张家界市",
        "city_code": 430800
    },
    "430900": {
        "city_name": "益阳市",
        "city_code": 430900
    },
    "431000": {
        "city_name": "郴州市",
        "city_code": 431000
    },
    "431100": {
        "city_name": "永州市",
        "city_code": 431100
    },
    "431200": {
        "city_name": "怀化市",
        "city_code": 431200
    },
    "431300": {
        "city_name": "娄底市",
        "city_code": 431300
    },
    "433100": {
        "city_name": "湘西土家族苗族自治州",
        "city_code": 433100
    },
    "440100": {
        "city_name": "广州市",
        "city_code": 440100
    },
    "440200": {
        "city_name": "韶关市",
        "city_code": 440200
    },
    "440300": {
        "city_name": "深圳市",
        "city_code": 440300
    },
    "440400": {
        "city_name": "珠海市",
        "city_code": 440400
    },
    "440500": {
        "city_name": "汕头市",
        "city_code": 440500
    },
    "440600": {
        "city_name": "佛山市",
        "city_code": 440600
    },
    "440700": {
        "city_name": "江门市",
        "city_code": 440700
    },
    "440800": {
        "city_name": "湛江市",
        "city_code": 440800
    },
    "440900": {
        "city_name": "茂名市",
        "city_code": 440900
    },
    "441200": {
        "city_name": "肇庆市",
        "city_code": 441200
    },
    "441300": {
        "city_name": "惠州市",
        "city_code": 441300
    },
    "441400": {
        "city_name": "梅州市",
        "city_code": 441400
    },
    "441500": {
        "city_name": "汕尾市",
        "city_code": 441500
    },
    "441600": {
        "city_name": "河源市",
        "city_code": 441600
    },
    "441700": {
        "city_name": "阳江市",
        "city_code": 441700
    },
    "441800": {
        "city_name": "清远市",
        "city_code": 441800
    },
    "441900": {
        "city_name": "东莞市",
        "city_code": 441900
    },
    "442000": {
        "city_name": "中山市",
        "city_code": 442000
    },
    "445100": {
        "city_name": "潮州市",
        "city_code": 445100
    },
    "445200": {
        "city_name": "揭阳市",
        "city_code": 445200
    },
    "445300": {
        "city_name": "云浮市",
        "city_code": 445300
    },
    "450100": {
        "city_name": "南宁市",
        "city_code": 450100
    },
    "450200": {
        "city_name": "柳州市",
        "city_code": 450200
    },
    "450300": {
        "city_name": "桂林市",
        "city_code": 450300
    },
    "450400": {
        "city_name": "梧州市",
        "city_code": 450400
    },
    "450500": {
        "city_name": "北海市",
        "city_code": 450500
    },
    "450600": {
        "city_name": "防城港市",
        "city_code": 450600
    },
    "450700": {
        "city_name": "钦州市",
        "city_code": 450700
    },
    "450800": {
        "city_name": "贵港市",
        "city_code": 450800
    },
    "450900": {
        "city_name": "玉林市",
        "city_code": 450900
    },
    "451000": {
        "city_name": "百色市",
        "city_code": 451000
    },
    "451100": {
        "city_name": "贺州市",
        "city_code": 451100
    },
    "451200": {
        "city_name": "河池市",
        "city_code": 451200
    },
    "451300": {
        "city_name": "来宾市",
        "city_code": 451300
    },
    "451400": {
        "city_name": "崇左市",
        "city_code": 451400
    },
    "460100": {
        "city_name": "海口市",
        "city_code": 460100
    },
    "460200": {
        "city_name": "三亚市",
        "city_code": 460200
    },
    # //"460321": {
    # //    "city_name": "三沙市",
    # //    "city_code": 460321
    # //},
    "469001": {
        "city_name": "五指山",
        "city_code": 469001
    },
    "469002": {
        "city_name": "琼海",
        "city_code": 469002
    },
    "469003": {
        "city_name": "儋州",
        "city_code": 469003
    },
    "469005": {
        "city_name": "文昌",
        "city_code": 469005
    },
    "469006": {
        "city_name": "万宁",
        "city_code": 469006
    },
    "469007": {
        "city_name": "东方",
        "city_code": 469007
    },
    "469021": {
        "city_name": "定安县",
        "city_code": 469021
    },
    "469022": {
        "city_name": "屯昌县",
        "city_code": 469022
    },
    "469023": {
        "city_name": "澄迈县",
        "city_code": 469023
    },
    "469024": {
        "city_name": "临高县",
        "city_code": 469024
    },
    "469025": {
        "city_name": "白沙黎族自治县",
        "city_code": 469025
    },
    "469026": {
        "city_name": "昌江黎族自治县",
        "city_code": 469026
    },
    "469027": {
        "city_name": "乐东黎族自治县",
        "city_code": 469027
    },
    "469028": {
        "city_name": "陵水黎族自治县",
        "city_code": 469028
    },
    "469029": {
        "city_name": "保亭县",
        "city_code": 469029
    },
    "469030": {
        "city_name": "琼中县",
        "city_code": 469030
    },
    "500100": {
        "city_name": "重庆市",
        "city_code": 500100
    },
    "510100": {
        "city_name": "成都市",
        "city_code": 510100
    },
    "510300": {
        "city_name": "自贡市",
        "city_code": 510300
    },
    "510400": {
        "city_name": "攀枝花市",
        "city_code": 510400
    },
    "510500": {
        "city_name": "泸州市",
        "city_code": 510500
    },
    "510600": {
        "city_name": "德阳市",
        "city_code": 510600
    },
    "510700": {
        "city_name": "绵阳市",
        "city_code": 510700
    },
    "510800": {
        "city_name": "广元市",
        "city_code": 510800
    },
    "510900": {
        "city_name": "遂宁市",
        "city_code": 510900
    },
    "511000": {
        "city_name": "内江市",
        "city_code": 511000
    },
    "511100": {
        "city_name": "乐山市",
        "city_code": 511100
    },
    "511300": {
        "city_name": "南充市",
        "city_code": 511300
    },
    "511400": {
        "city_name": "眉山市",
        "city_code": 511400
    },
    "511500": {
        "city_name": "宜宾市",
        "city_code": 511500
    },
    "511600": {
        "city_name": "广安市",
        "city_code": 511600
    },
    "511700": {
        "city_name": "达州市",
        "city_code": 511700
    },
    "511800": {
        "city_name": "雅安市",
        "city_code": 511800
    },
    "511900": {
        "city_name": "巴中市",
        "city_code": 511900
    },
    "512000": {
        "city_name": "资阳市",
        "city_code": 512000
    },
    "513200": {
        "city_name": "阿坝藏族羌族自治州",
        "city_code": 513200
    },
    "513300": {
        "city_name": "甘孜藏族自治州",
        "city_code": 513300
    },
    "513400": {
        "city_name": "凉山彝族自治州",
        "city_code": 513400
    },
    "520100": {
        "city_name": "贵阳市",
        "city_code": 520100
    },
    "520200": {
        "city_name": "六盘水市",
        "city_code": 520200
    },
    "520300": {
        "city_name": "遵义市",
        "city_code": 520300
    },
    "520400": {
        "city_name": "安顺市",
        "city_code": 520400
    },
    "520500": {
        "city_name": "毕节地区",
        "city_code": 520500
    },
    "520600": {
        "city_name": "铜仁地区",
        "city_code": 520600
    },
    "522300": {
        "city_name": "黔西南",
        "city_code": 522300
    },
    "522600": {
        "city_name": "黔东南苗族侗族自治州",
        "city_code": 522600
    },
    "522700": {
        "city_name": "黔南",
        "city_code": 522700
    },
    "530100": {
        "city_name": "昆明市",
        "city_code": 530100
    },
    "530300": {
        "city_name": "曲靖市",
        "city_code": 530300
    },
    "530400": {
        "city_name": "玉溪市",
        "city_code": 530400
    },
    "530500": {
        "city_name": "保山市",
        "city_code": 530500
    },
    "530600": {
        "city_name": "昭通市",
        "city_code": 530600
    },
    "530700": {
        "city_name": "丽江市",
        "city_code": 530700
    },
    "530800": {
        "city_name": "普洱市",
        "city_code": 530800
    },
    "530900": {
        "city_name": "临沧市",
        "city_code": 530900
    },
    "532300": {
        "city_name": "楚雄彝族自治州",
        "city_code": 532300
    },
    "532500": {
        "city_name": "红河哈尼族彝族自治州",
        "city_code": 532500
    },
    "532600": {
        "city_name": "文山壮族苗族自治州",
        "city_code": 532600
    },
    "532800": {
        "city_name": "西双版纳傣族自治州",
        "city_code": 532800
    },
    "532900": {
        "city_name": "大理白族自治州",
        "city_code": 532900
    },
    "533100": {
        "city_name": "德宏傣族景颇族自治州",
        "city_code": 533100
    },
    "533300": {
        "city_name": "怒江傈僳族自治州",
        "city_code": 533300
    },
    "533400": {
        "city_name": "迪庆藏族自治州",
        "city_code": 533400
    },
    "540100": {
        "city_name": "拉萨市",
        "city_code": 540100
    },
    "540200": {
        "city_name": "日喀则地区",
        "city_code": 540200
    },
    "542100": {
        "city_name": "昌都地区",
        "city_code": 542100
    },
    "542200": {
        "city_name": "山南地区",
        "city_code": 542200
    },
    "542400": {
        "city_name": "那曲地区",
        "city_code": 542400
    },
    "542500": {
        "city_name": "阿里地区",
        "city_code": 542500
    },
    "542600": {
        "city_name": "林芝地区",
        "city_code": 542600
    },
    "610100": {
        "city_name": "西安市",
        "city_code": 610100
    },
    "610200": {
        "city_name": "铜川市",
        "city_code": 610200
    },
    "610300": {
        "city_name": "宝鸡市",
        "city_code": 610300
    },
    "610400": {
        "city_name": "咸阳市",
        "city_code": 610400
    },
    "610500": {
        "city_name": "渭南市",
        "city_code": 610500
    },
    "610600": {
        "city_name": "延安市",
        "city_code": 610600
    },
    "610700": {
        "city_name": "汉中市",
        "city_code": 610700
    },
    "610800": {
        "city_name": "榆林市",
        "city_code": 610800
    },
    "610900": {
        "city_name": "安康市",
        "city_code": 610900
    },
    "611000": {
        "city_name": "商洛市",
        "city_code": 611000
    },
    "620100": {
        "city_name": "兰州市",
        "city_code": 620100
    },
    "620300": {
        "city_name": "金昌市",
        "city_code": 620300
    },
    "620400": {
        "city_name": "白银市",
        "city_code": 620400
    },
    "620500": {
        "city_name": "天水市",
        "city_code": 620500
    },
    "620600": {
        "city_name": "武威市",
        "city_code": 620600
    },
    "620700": {
        "city_name": "张掖市",
        "city_code": 620700
    },
    "620800": {
        "city_name": "平凉市",
        "city_code": 620800
    },
    "620900": {
        "city_name": "酒泉市",
        "city_code": 620900
    },
    "621000": {
        "city_name": "庆阳市",
        "city_code": 621000
    },
    "621100": {
        "city_name": "定西市",
        "city_code": 621100
    },
    "621200": {
        "city_name": "陇南市",
        "city_code": 621200
    },
    "622900": {
        "city_name": "临夏回族自治州",
        "city_code": 622900
    },
    "623000": {
        "city_name": "甘南藏族自治州",
        "city_code": 623000
    },
    "630100": {
        "city_name": "西宁市",
        "city_code": 630100
    },
    "630200": {
        "city_name": "海东地区",
        "city_code": 630200
    },
    "632200": {
        "city_name": "海北藏族自治州",
        "city_code": 632200
    },
    "632300": {
        "city_name": "黄南藏族自治州",
        "city_code": 632300
    },
    "632500": {
        "city_name": "海南藏族自治州",
        "city_code": 632500
    },
    "632600": {
        "city_name": "果洛藏族自治州",
        "city_code": 632600
    },
    "632700": {
        "city_name": "玉树藏族自治州",
        "city_code": 632700
    },
    "632800": {
        "city_name": "海西蒙古族藏族自治州",
        "city_code": 632800
    },
    "640100": {
        "city_name": "银川市",
        "city_code": 640100
    },
    "640200": {
        "city_name": "石嘴山市",
        "city_code": 640200
    },
    "640300": {
        "city_name": "吴忠市",
        "city_code": 640300
    },
    "640400": {
        "city_name": "固原市",
        "city_code": 640400
    },
    "640500": {
        "city_name": "中卫市",
        "city_code": 640500
    },
    "650100": {
        "city_name": "乌鲁木齐市",
        "city_code": 650100
    },
    "650200": {
        "city_name": "克拉玛依市",
        "city_code": 650200
    },
    "652100": {
        "city_name": "吐鲁番地区",
        "city_code": 652100
    },
    "652200": {
        "city_name": "哈密地区",
        "city_code": 652200
    },
    "652300": {
        "city_name": "昌吉回族自治州",
        "city_code": 652300
    },
    "652700": {
        "city_name": "博尔塔拉蒙古自治州",
        "city_code": 652700
    },
    "652800": {
        "city_name": "巴音郭楞蒙古自治州",
        "city_code": 652800
    },
    "652900": {
        "city_name": "阿克苏地区",
        "city_code": 652900
    },
    "653000": {
        "city_name": "克孜勒苏柯尔克孜自治州",
        "city_code": 653000
    },
    "653100": {
        "city_name": "喀什地区",
        "city_code": 653100
    },
    "653200": {
        "city_name": "和田地区",
        "city_code": 653200
    },
    "654000": {
        "city_name": "伊犁哈萨克自治州",
        "city_code": 654000
    },
    "654200": {
        "city_name": "塔城地区",
        "city_code": 654200
    },
    "654300": {
        "city_name": "阿勒泰地区",
        "city_code": 654300
    },
    "659001": {
        "city_name": "石河子",
        "city_code": 659001
    }
};
print 'citiCode JSON keys ', citiCodeJSON.keys()

ins_num = 1
insured_ = []
ageRangeYear = ['4-17','18-50','51-','55-65','60-','66-69','70-74','75-140']
for i in range(0,ins_num):
    print i
    ins = {}
    ins["card_type"] = '01'
    ins["card_id"] = gennerator()
    ins["name"] = '电脑打交道'
    insured_.append(ins)
#total_ = 12345
channelName =  'anyi'
productId = "YAIC20170629001"
month_ = '10'
shares_ = 1

orderReckon = {
    "appid": 'anyi',
    "product_id": 'YAIC20170629001',
    "params": {
        "city_code": 1222,
        "month": '10',
        "shares": 1

    }
}
orderVerify ={

    "appid": channelName,
    "total": '11',
    "insured": insured_,
    "request_id": '9999',
    "product": {
        "id": productId,
        "name": "john·）",
        "package": "",
        "package_code": "A"
    },
    "addtional": {
        "effect":'2018-01-25',
        # "city_code":m.citiCode,
        "month":month_,
        "shares":shares_,
        "bank_name": 'bank_name_test',
        "bank_account": 'bank_account_test',
        "account_name":'account_name_test',
        # sex: array.getOneElement(['男', '女']),
    },
    "applicant":{
            "name": "john1",
            "email": "173035979@qq.com",
            "phone": "13819473719",
            "card_type": '01',
            # card_id: common.orderRelated.getCardIdByAgeRange(array.getOneElement(ageRangeYear)),
            # birthday: common.orderRelated.getBirthday(array.getOneElement(ageRangeYear)),
            # sex: array.getOneElement(['男', '女']),

    },

}
orderConfirm = {
    "appid": channelName,
    "order_id": "12345", #4
    "notify_url":'http://test.spb.riskeys.com/spb/app/certInfo/savePolicyNoByConfiraction', #回调地址
    #notify_url:'http://open.anyi-tech.com/spb/app/certInfo/savePolicyNoByConfiraction', #回调地址
    "pay_info": {},
    "whether": "1"
}
print orderReckon
print '-----------------------'
print orderVerify
if __name__ == '__main__':
    urlBase = 'http://test.channel.riskeys.com/ws_order/'
    reckon_url = 'reckon'
    verify_url = 'verify'
    confirm_url = 'confirm'
    request_times = 1
    daysArr = [50,51,52,53,54,55,56,57,58,59,40,41,42,43,44,45,46,47,48]
    for i in range(0, request_times):
        n = random.choice(daysArr)
        orderVerify['addtional']['effect'] = getEffectTime(n)
        citiCode = random.choice(citiCodeJSON.keys())
        orderReckon['params']['city_code'] = citiCode
        orderVerify['addtional']['city_code'] = citiCode
        reqeustId = str(random.randint(0, 1111111111111111111111111111))
        orderVerify['request_id'] = reqeustId
        orderVerify['applicant']['card_id'] = gennerator()

        body_post(reckon_url, orderReckon)
        body_post(verify_url, orderVerify)
        body_post(confirm_url, orderConfirm)

