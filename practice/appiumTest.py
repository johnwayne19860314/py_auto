
#coding=utf-8

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
desired_caps['app']=PATH(r"D:/Tools/com.android.chrome.apk")    #com.android.chrome-62.0.3202.84-320208401
print desired_caps['app']
desired_caps['appPackage'] ='com.android.chrome' #谷歌包名
desired_caps['appActivity'] = 'org.chromium.chrome.browser.document.ChromeLauncherActivity' #谷歌起始页面

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)