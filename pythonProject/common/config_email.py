import smtplib
import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class ConfigEmail:
    """
        配置发送邮件
    """
    def __init__(self, username, password, receivers, title, content,
                 file=None, ssl=False, email_host="smtp.163.com", port=25, ssl_port=465):
        self.username = username  # 发送者用户名
        self.password = password  # 发送者密码
        self.receivers = receivers  # 收件者邮箱
        self.title = title  # 邮件标题
        self.content = content  # 邮件正文内容
        self.file = file  # 邮件附件
        self.ssl = ssl  # 使用与否ssl协议
        self.email_host = email_host  # smtp服务主机
        self.port = port  # smtp服务端口号
        self.ssl_port = ssl_port  # ssl端口号

    def send_email(self):
        message = MIMEMultipart()
        try:
            with open(self.file, "rb") as f:
                content = f.read()
        except FileNotFoundError:
            print("File not found!")
        else:
            file_name = os.path.split(self.file)[-1]
            att = MIMEText(content, "base64", "utf-8")
            att['Content-Type'] = 'application/octet-stream'
            new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
            att["Content-Disposition"] = 'attachment; filename="%s"' % new_file_name
            message.attach(att)
        message.attach(MIMEText(self.content))
        message['Subject'] = self.title
        message['From'] = self.username
        message['To'] = ','.join(self.receivers)
        if self.ssl:
            smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            smtp = smtplib.SMTP(self.email_host, port=self.port)
        smtp.login(user=self.username, password=self.password)
        try:
            smtp.sendmail(self.username, self.receivers, message.as_string())
        except smtplib.SMTPException:
            print('发送邮件出错！')
        else:
            print('发送成功！')
        smtp.quit()
