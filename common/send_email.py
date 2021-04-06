#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
发送邮件...
"""
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class Mail:
    """
    邮件操作类
    """
    def __init__(self, smtp, port, user, pwd, timeout=15):
        """
        初始化
        :param smtp: SMTP服务器
        :param port: 端口
        :param user: 用户名
        :param pwd: 密码
        :return: None
        """
        self.smtp = smtp
        self.port = port
        self.user = user
        self.pwd = pwd
        self.isauth = True
        self.timeout = timeout

    def send(self, subject, content, tolist, cclist=None, plugins=None):
        """
        发送邮件
        :param subject: 标题
        :param content: 内容
        :param tolist: 收件人列表
        :param cclist: 抄送人列表
        :param plugins: 附件列表
        :return: 是否发送成功
        """
        # 构造邮件消息
        msg = MIMEMultipart()
        msg.set_charset("utf-8")
        msg["from"] = self.user
        msg["to"] = ",".join(tolist)
        addr_list = tolist
        if cclist:
            msg["cc"] = ",".join(cclist)
            addr_list.extend(cclist)
        msg["subject"] = subject
        msg.attach(MIMEText(content, "html", "utf-8"))
        if plugins:
            for i in plugins:
                if isinstance(i["filename"], bytes):
                    filename = i["filename"].decode("utf-8")
                else:
                    filename = i["filename"]
                mimeapp = MIMEApplication(i["body"])
                mimeapp.add_header("content-disposition", "attachment",
                                   filename=filename)
                msg.attach(mimeapp)

        # 连接SMTP服务器
        conn = smtplib.SMTP(self.smtp, port=self.port, timeout=self.timeout)
        conn.set_debuglevel(smtplib.SMTP.debuglevel)
        if self.isauth:
            conn.docmd("EHLO %s" % self.smtp)
        try:
            conn.starttls()
        except smtplib.SMTPException as exp:
            logging.warn("fail to starttls: %s", exp)
        conn.login(self.user, self.pwd)
        result = conn.sendmail(self.user, addr_list, msg.as_string())
        conn.close()
        return result


if __name__ == "__main__":
    MAIL = Mail("smtp.xxx.com", "xxxx@xxx.com", "password")
    MAIL.send("发送邮件测试", '<font color="#0000FF">热门</color>',
              ["xxxxx@xxx.com"], None,
              [{"filename": "附件1.txt", "body": "内容1"}])
    print("mail send ...")