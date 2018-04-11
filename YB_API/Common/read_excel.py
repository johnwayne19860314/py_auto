# -*- coding:utf-8 -*-

import xlrd
from Common import get_path

def read_Excel(sheetname):
    #获取文件路径
    excelpath=get_path.Read_path('data','yb_account.xlsx')
    #打开Excel
    workbook=xlrd.open_workbook(excelpath)
    table=workbook.sheet_by_name(sheetname)
    nrows=table.nrows
    dict={}
    list=[]
    for i in range(1,nrows):
        # dict['method']=table.cell(i,0).value.replace('\n','').replace('\r','')
        # dict['url']=table.cell(i,1).value.replace('\n','').replace('\r','')
        # dict['body']=table.cell(i,2).value.replace('\n','').replace('\r','')
        # dict['type']=table.cell(i,3).value.replace('\n','').replace('\r','')
        # print(dict['method'])
        # print(dict)
        raw_data=table.row_values(i)
        list.append(raw_data)
    return list

if __name__ == "__main__":
    read_Excel("Sheet1")