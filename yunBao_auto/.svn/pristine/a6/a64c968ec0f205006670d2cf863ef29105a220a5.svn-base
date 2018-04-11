# -*- coding:utf-8 -*-
#import Driver
from ..Public  import Driver
from ..Public import operation

operate=operation.Common()
def HomePage(self):
    global driver
    #打开浏览器，进入首页
    self.driver=Driver.DriverFirefox()
    driver=self.driver
    driver.get("http://test.spb.riskeys.com")
    operate.sleep(1)
    # 判断是否是首页内容
    # try:
    #     self.assertEquals(u"安逸云保-场景化保险专家",self.driver.title)
    # except AssertionError as e:
    #     print(u"找不到这个标题")

def getDriver():
    return driver

def select_type(self,typeclass):
    # #滚动下拉条，选择场景类别
    # xpath=".//*[@id='index-main']/div"
    # operate.mouse_pull(xpath)
    #睡眠2秒，查看数据
    operate.sleep(2)
    #获取场景,根据不同的类别进入到不同的页面
    try:
        #商铺综合
        if typeclass=="shop":
            print('come to the type shop')
            operate.element_click("linktext",u"商铺综合")
        #体育运动
        if typeclass=="sports":
            operate.element_click("linktext",u"体育运动")
        #货运物流
        if typeclass=="logistics":
            operate.element_click("linktext",u"货运物流")
        #电器安装
        if typeclass=="electric":
            operate.element_click("linktext",u"电器安装")
        #小微保
        if typeclass=="umbrella":
            operate.element_click("linktext",u"小微保")
    except Exception as e:
        print(e)


