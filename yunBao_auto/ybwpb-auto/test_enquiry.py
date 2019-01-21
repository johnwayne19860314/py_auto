# -*- coding:utf-8 -*-
import unittest
import sys,os
import time
sys.path.append("..")
#import Public.HomePage
import HTMLTestRunner
global driver
#from yunBao_auto.Public import HomePage
# print __package__
# print os.getcwd()
# os.chdir(r'D:/Testing/Automation/UI_Auto')
# print os.getcwd()

#sys.path.insert(0, r'D:/Testing/Automation/UI_Auto')
print sys.path
#from ..Public import operation
#import yunBao_auto.Public.operation as operate
from yunBao_auto.Public import operation
from yunBao_auto.Public import LogManager
from yunBao_auto.Public import email_write

operate=operation.Common()
driver = operate.getDriver()
log=LogManager.LogMgr('login')
#定义测试路径以及测试文件报告名c
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
files = sys.path[0]
print('the files are ', files)
#reportDir=os.path.join(files, 'report')
reportfilename=os.path.join(files, 'report', 'test_result'+now+'.html')
class QueryPrice(unittest.TestCase):
    u"""用户投保流程"""
    def testEnquiry(self):
        u"""询价"""
        #打开首页并且登陆账号
       # HomePage.HomePage(self)
      #  operate.sleep(3)

        #HomePage.select_type(self,"shop")
        #operate.element_click("linktext", u"场景合作")
        #operate.element_click("linktext", u"商铺")
        #driver = HomePage.getDriver()
        #operate.sleep(1)

        #立即进入
        #operate.element_click("linktext",u"立即进入")
        #operate.element_click("xpath", "html/body/div[2]/div/a")

        #operate.sleep(4)
        #断言是否进入到首页
        # try:
        #     self.assertEqual("http://test.spb.riskeys.com/shop/index.html",
        #                      driver.current_url,
        #                      "page is error")
        # except :
        #     log.debug(u"进入首页失败")

        #登陆
       # QueryPrice.Login(self)
        #进入我要询价
        ##operate.element_click("linktext",u"我要询价")
        #operate.mouse_pull()
        #operate.sleep(1)
        #operate.element_click("xpath", ".//a[@class='copy-btn ani show']")
        driver.get("http://test.spb.riskeys.com/shop/ask.html")
        #调用ask方法，进行询价
        QueryPrice.ask(self)

    def testScheme(self):
        u"""询价方案"""
        operate.sleep(2)
        #下拉页面到
        operate.mouse_pull()
        dict={'insuranceTime':1,'perNumber':1}
        operate.dict_select(dict)
        #先清楚文本框默认数字，再输入
        operate.clear_input("staffNumber")
        operate.element_input("id","staffNumber",3)
        operate.sleep(2)
        check="//div[@class='form-content container']/div[@class='button-box']/div[@class='notice']/span[1]"
        operate.element_click("xpath",check)
        #立即投保
        operate.element_click("id","buy-btn")
        operate.sleep(1)

    def test_Insure(self):
        u"""开始投保"""
        #默认选择企业
        #输入投保机构，联系人，手机号码
        driver.get("http://test.spb.riskeys.com/shop/buyForm.html")
        insure_dict={'shopName':'TaiPingYang','contacts':'testone','insurer-phone':'18207278423'}
        operate.dict_input("id",insure_dict)
        #传入员工名单
        QueryPrice.buy_employees_input_direct(self)
        operate.sleep(2)
        #鼠标下滑到最下面
        operate.mouse_pull()
        # #选择发票类型
        QueryPrice.invoice_input_normal(self)
        # #确认投保
        operate.mouse_pull()
        # check_radio="//div[@class='button-box']/div[@class='notice']/span[@class='my-check']"
        # operate.element_click("xpath",check_radio)
        operate.is_Selected('xpath', "//div[@class='button-box']/div[@class='notice']/span[@class='my-check']")
        log.info('come to the buy page 1')
        operate.element_click("id","buy-btn")
        #确认投保信息，并判断是否是投保页面，是则确认投保，不是则刷新页面
        operate.sleep(2)
        try:
            #判断"投保确认"元素是否存在于页面
            text=driver.find_element_by_xpath("//div[@class='block-title']")
            if(text.is_displayed()==True):
                if(text.text==u'确认投保'):
                    print(u"成功进入投保确认页面")
                else:
                    operate.refresh()
            else:
                operate.refresh()
        except:
            #log.debug(u"页面元素未找到")
            self.assertEquals (1,-1,u'页面元素未找到')
        #确认页面之后确认投保
        operate.mouse_pull()
        operate.is_Selected('xpath',"//div[@class='button-box']/div[@class='notice']/span[@class='my-check']")
        #operate.is_Selected('xpath', "/html/body/div[2]/div[2]/div[4]/div[2]/span[1]")
        log.info('come to the buy page 2')
        operate.element_click("id","buy-btn")
        operate.sleep(2)
        QueryPrice.Login(self)

    def Login(self):
        #点击登陆
       # operate.element_click("id","login-btn")
        #operate.sleep(2)
        #输入用户名密码
        login_input={'account':'18207278423','password':'123456'}
        operate.dict_input("id",login_input)
        operate.element_click("id","user-login")
        operate.sleep(2)

    def ask(self):
        #判断是否是询价页面
        try:
            self.assertEqual("http://test.spb.riskeys.com/shop/ask.html",
                             driver.current_url,
                             "page is error")
        except :
            log.debug(u"进入询价页面失败")
        #使用for循环，依次输入下拉框数据
        markets=operate.elements_list("xpath", ".//*[@id='city']/select")
        for num in range(1,len(markets)+1):
            market_name=".//*[@id='city']/select["+str(num)+"]"
            operate.element_selected("index",market_name,1)
            operate.sleep(1)
        #传入字典输入商铺号以及商铺名称
        dict_v={'shopId':'SPH001','shopName':'TEST_SHOP'}
        operate.dict_input("id",dict_v)
        #输入商铺面积，设备价值，存货价值
        dict_price={'shopSize':2,'shopDeviceValue':3,'shopStockValue':2}
        operate.dict_select(dict_price)
        #输入装修合同
        operate.element_selected("index",".//*[@id='shopDecorationTotal']/select",2)
        #点击为您推荐
        operate.element_click("id","submit-answers")
        operate.sleep(2)

    def buy_employees_input_direct(self):
        check_radio="//div[@class='radio-wrap']/div[@class='radio-item']/input[@class='input-staff-select']"
        operate.element_click("xpath",check_radio)
        #name = "//div[@class='form-group has-feedback has-error has-danger']/input[@class='form-control name']"
        name = ".//*[@id='staffFromInput']/tr[1]/td[2]/div/input"
        idCard = ".//*[@id='staffFromInput']/tr[1]/td[2]/div/input"
        birthday = ".//*[@id='staffFromInput']/tr[1]/td[2]/div/input"
        dict_receiver={".//*[@id='staffFromInput']/tr[1]/td[2]/div/input":"Hanxiao",
                       ".//*[@id='staffFromInput']/tr[1]/td[3]/div/input":"429006198603143010",
                       #".//*[@id='staffFromInput']/tr[1]/td[4]/div/input":"1986-03-14"
                       }
        operate.dict_input("xpath",dict_receiver)
        dict = {".//*[@id='staffFromInput']/tr[1]/td[5]/select": 1}
        operate.dict_select_1('xpath',dict)

    def buy_employees_input_upload(self):
        #传入员工名单
        #获取excel路径
        #fpath=operate.read_file(r"\yunBao_auto\testData","mingdan.xlsx")
        fpath = operate.read_file("testData", "mingdan.xlsx")
        operate.element_input("id", "form-field-attach", fpath)

    def invoice_input_normal(self):
        xpath="//input[@type='radio' and @value='normal']"
        operate.element_click("xpath",xpath)
        dict_receiver={"receiverName":"Hanxiao","receiverTel":"18207278423","receiverPost":"200000"}
        operate.dict_input("id",dict_receiver)
        operate.element_input("id","receiverAddress",u"上海市浦东新区")
if __name__ == '__main__':
    #构造测试集
    suite=unittest.TestSuite()
   # suite.addTest(QueryPrice("testEnquiry"))
    #suite.addTest(QueryPrice("testScheme"))
    suite.addTest(QueryPrice("test_Insure"))

    #执行测试 use unittest to run
    #runner=unittest.TextTestRunner()
    #runner.run(suite)
    # use run
    email_write.write(reportfilename,
                      suite)
    # 执行发送报告
    time.sleep(10)
    email_write.sendreport(files)
    # 清除测试产生的screenshot和repot
    time.sleep(10)
    email_write.clean(files)
