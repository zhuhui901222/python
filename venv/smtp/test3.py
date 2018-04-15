#!/usr/bin/python
# -*- coding: UTF-8 -*-

#测试成功！
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = "smtp.139.com"
mail_user = "15812902593@139.com"   #发送邮件的邮箱账号名（不加@xxx什么鬼的）
mail_pass = "wolf901222"   #发送邮件的邮箱密码

sender = '15812902593@139.com'  #发送邮件的邮箱全名（包括@xxx什么鬼的）
receivers = '478040236@qq.com'   #接收邮件的邮箱地址全称（xxx@xxx.xxx）

message = MIMEText('Py mail test!!!','plain','utf-8')
message['From'] = mail_user
message['To'] = receivers

subject = 'Py SMTP Test'
message['Subject'] = Header(subject,'utf-8')


try:
    s = smtplib.SMTP_SSL("smtp.139.com", 465)
    s.login(mail_user, mail_pass)
    s.sendmail(sender, receivers,message.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException, e:
    print str(e)
    print "Error: 无法发送邮件"
