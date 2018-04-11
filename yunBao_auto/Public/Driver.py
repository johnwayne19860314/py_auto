# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os,sys
#from ..Public import operation
#Chorme_file = os.path.join(sys.path[1], 'resource', 'chromedriver.exe')
#print Chorme_file
def DriverFirefox():
   # driver=webdriver.Firefox()
   #//C:\Users\Anyi-tech\AppData\Roaming\Mozilla\Firefox\Profiles\kj93kq6l.default
    #配置文件地址
    profile_directory = r'C:\Users\Anyi-tech\AppData\Roaming\Mozilla\Firefox\Profiles\lwteu6fo.firefox51'
    #profile_directory = r'C:\Users\Anyi-tech\AppData\Roaming\Mozilla\Firefox\Profiles\tfr7iv91.john'
    # 加载配置配置
    profile = webdriver.FirefoxProfile(profile_directory)
    # 启动浏览器配置
    driver = webdriver.Firefox(profile)

    # binary = FirefoxBinary(r'D:\Tools\Firefox51')
    # driver = webdriver.Firefox(firefox_binary=binary)
    driver.maximize_window()
    return driver


def Chorme():
    WIDTH = 414
    HEIGHT = 672
    PIXEL_RATIO = 5.0
    option = webdriver.ChromeOptions()
    mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}}
    option.add_argument("--user-agent=mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0")
    option.add_experimental_option('mobileEmulation', mobileEmulation)
    Chorme_file = os.path.join(sys.path[1], 'resource', 'chromedriver.exe')
    driver = webdriver.Chrome(Chorme_file, chrome_options=option)
    driver.implicitly_wait(30)
    return driver

def IE():
   # Chorme_file=operation().read_file('resource', 'IEDriverServer.exe')
    IE_file = ''
    driver=webdriver.Chrome(IE_file)
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver


