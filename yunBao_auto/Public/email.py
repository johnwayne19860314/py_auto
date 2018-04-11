# -*- coding:utf-8 -*-
from __future__ import absolute_import
import os,time,sys
import HTMLTestRunner
import smtplib
import email
print str(email)
#from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase



def write(filenames,names):
    #读取报告
    with open(filenames,'wb') as fp:
        #定义runner
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'测试报告',
            description=u'用例执行情况：'
            )
        #执行用例
        print(u'开始执行测试用例;')
        runner.run(names)
        print(u'执行测试用例完成;')

#定义发送邮件
def sent_mail(file_new,files):
    u"""定义发送邮件"""
    print(u'开始定义邮件;')
    #设置发送服务器、账号、用户名
    From = 'xiaoqing.han@anyi-tech.com'
    To =['zhijun.jiang@anyi-tech.com']
    server = smtplib.SMTP('smtp.exmail.qq.com', 25)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(From,'Anyi1234')

    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()

    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    f =open(file_new,'rb')
    mail_body = f.read()
    f.close()
    text_msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    main_msg.attach(text_msg)


    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)
    ## 读入文件内容并格式化
    data = open(file_new, 'rb')
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    email.encoders.encode_base64(file_msg)

    ## 设置附件头
    basename = os.path.basename(file_new)
    file_msg.add_header('Content-Disposition','attachment', filename = basename)
    main_msg.attach(file_msg)

    #图片
    pngdir=[]
    listaa=os.listdir(os.path.join(files,"screenshot"))
    for png in listaa:
        if '_png' in png:
            pngdir.append(png)
    for eachpng in pngdir:
        fp=open(os.path.join(files,"screenshot",eachpng),'rb')
        msgImage=MIMEImage.MIMEImage(fp.read(),'x-png None')
        msgImage.add_header('Content-Disposition','attachment',filename=eachpng)
        main_msg.attach(msgImage)
        fp.close()
    # 设置根容器属性
    main_msg['From'] = From
    main_msg['To'] = ",".join(To)
    main_msg['Subject'] = u'云保测试报告'
    main_msg['Date'] = email.utils.formatdate()

    # 得到格式化后的完整文本
    fullText = main_msg.as_string()

    # 用smtp发送邮件
    try:
        server.sendmail(From, To, fullText)
    finally:
        server.quit()
        print('Mail has sended out！')

#发送测试报告
def sendreport(files):
    u"""发送测试报告"""

    print(u'开始发送邮件;')
    #查找最新生成的测试报告文件
    result_dir=os.path.join(files,'report')
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(result_dir,fn)))
    print(u'最新测试生成报告' +lists[-1])
    file_new=os.path.join(result_dir,lists[-1])
    print(file_new)

    #调用发邮件模块
    sent_mail(file_new,files)
    print(u'邮件发送完成;')

#清除测试产生的screenshot和repot
def clean(files):
    u"""清除测试产生的screenshot和repot"""
    #清除screenshot
    print(u'开始清理screenshot；')
    listscreenshot=os.listdir(os.path.join(files,"screenshot"))
    print(listscreenshot)
    if len(listscreenshot)> 0:
        for eachscreenshot in listscreenshot:
            print('remove '+os.path.join(files,"screenshot",eachscreenshot))
            os.remove(os.path.join(files,"screenshot",eachscreenshot))
    else:
        print('no file;')
    print(u'清理完成;')

    #清除repot

    print(u'开始清理report；')
    listreport = os.listdir(os.path.join(files,"report"))
    print(listreport)
    if len(listreport)> 0:
        for eachreport in listreport:
            print('remove '+os.path.join(files,"report",eachreport))
            os.remove(os.path.join(files,"report",eachreport))
    else:
        print('no file;')
    print(u'清理完成;')