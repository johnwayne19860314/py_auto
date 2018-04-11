# -*-coding:utf-8 -*-
import configparser
import codecs
from Common import get_path

class Read_config():
    '''
    读取ini格式配置文件
    '''
    def __init__(self):
        configpath=get_path.Read_path('Config','config.ini')
        fd=open(configpath,'rb')
        data=fd.read()
        #remove BOM： 配置文件前3个空格
        if data[:3]==codecs.BOM_UTF8:
            data=data[:3] #去掉前3个空格
            file=codecs.open(configpath,'w')
            file.write()
            file.close()
        fd.close()
        self.config=configparser.ConfigParser()
        self.config.read(configpath,encoding='utf-8')

    def get_database(self,name):
        value=self.config.get("database",name)
        return value

    def get_http(self,name):
        value=self.config.get("HTTP",name)
        return value

    def get_log(self,name):
        value=self.config.get("log",name)
        return value
