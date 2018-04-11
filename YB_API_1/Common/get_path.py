# -*- coding:utf-8 -*-
import os

#获取文件路径
def Read_path(filer,filename):
    pro_dict=os.path.dirname(os.getcwd())
    filePath=os.path.join(pro_dict,filer,filename)
    if os.path.exists(filePath)==False:
        raise Exception("文件不存在")
    else:
        return filePath