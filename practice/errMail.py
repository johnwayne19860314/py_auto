import os
import smtplib
import time
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    mail_host = "smtp.exmail.qq.com"  # 设置服务器
    #mail_user = 'zhijun.jiang@anyi-tech.com'  # 用户名
    mail_user = 'xiaoqing.han@anyi-tech.com'  # 用户名
    mail_pass = "Anyi1234"  # 口令
    #mail_postfix = ""  # 发件箱的后缀

    #me = "错误日志" + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEMultipart()
    msg['Subject'] = sub  # 设置主题
    msg['From'] = mail_user
    msg['To'] = ";".join(to_list)
    # ---邮件正文---
    part = MIMEText(open(objectdir, 'r').read(), _charset='gb2312')  # 将错误文件内容做为邮件正文内容
    msg.attach(part)

    # txt类型附件
    part = MIMEApplication(open(objectdir, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="error_log.txt")
    msg.attach(part)
    try:
        s = smtplib.SMTP(mail_host)
        #s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(mail_user, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False


# 获取错误日志内容
def getContent(resouce, final):
    f = open(resouce, 'r')
    finalfile = open(final, 'w')
    try:
        for line in f:
            #if yes_date in line:
                if "ERROR" in line:  # 按行读取，如果该行包含“ERORR”字符串，则将该行写入目标文件
                    finalfile.write(line)

    finally:
        f.close()
        finalfile.close()


# 获取昨天的时间，这块可以任意改成自己需要的时间
def get_yesterday_date():
    today = datetime.datetime.now()
    oneday = today - datetime.timedelta(days=1)
    yes_date = oneday.strftime("%Y-%m-%d")
    return yes_date


if __name__ == '__main__':
    sourcedir = "D:/catalina.out"  # 需要读取的源文件路径
    objectdir = "D:/error_log.txt"  # 存放的目标文件
    mailto_list = ["dong.li@anyi-tech.com",'zhijun.jiang@anyi-tech.com']  # 收件人邮箱，可以发送存放多个
    yes_date = get_yesterday_date()

    getContent(sourcedir, objectdir)
    if os.path.getsize(objectdir):
        if send_mail(mailto_list, "错误日志_" + yes_date, objectdir):
            print("发送成功")
        else:
            print("发送失败")
    else:
        print("无错误日志，未发送邮件")