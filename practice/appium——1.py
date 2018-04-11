#! /usr/bin/env python
# import os
# import time
#
# from lib2to3.pgen2.driver import Driver
# from lib2to3.tests.support import driver
#

#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'　　#设备系统
# desired_caps['platformVersion'] = '5.1.2'　　#设备系统版本
# desired_caps['deviceName'] = 'Lenovo P1c72'　　#设备名称
#
# desired_caps['app'] = PATH('C:\\Users\\LENOVO\\Desktop\\StarZone_V2.0.0.apk')　
# #desired_caps['appPackage'] = 'com.xiangchao.starspace'　　
# #desired_caps['appActivity'] = 'com.xiangchao.starspace.activity.SplashActivity'
#
# #如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)　　#启动app
#
# time.sleep(5)　　#启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
# driver.find_element_by_id('com.xiangchao.starspace:id/skip').click()
#
# driver.quit()
from appium import webdriver
#from selenium import webdriver
#from appium import webdriver
#import appium.webdriver
#import appium
import unittest
import os

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['noReset']=True
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0.1'#备版本号
desired_caps['deviceName']='4e299031' #设备名
desired_caps['browserName']='Chrome'
#desired_caps['app']=PATH(r"D:/Tools/com.android.chrome.apk")    #com.android.chrome-62.0.3202.84-320208401
#print desired_caps['app']
desired_caps['appPackage'] ='com.android.chrome' #谷歌包名
desired_caps['appActivity'] = 'org.chromium.chrome.browser.document.ChromeLauncherActivity' #谷歌起始页面

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)