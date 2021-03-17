import smtplib
import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class ConfigEmail:
    def __init__(self, username, password, receivers, title, content,
                 file=None, ssl=False, email_host="smtp.163.com", port=25, ssl_port=465):
        self.username = username
        self.password = password
        self.receivers = receivers
        self.title = title
        self.content = content
        self.file = file
        self.ssl = ssl
        self.email_host = email_host
        self.port = port
        self.ssl_port = ssl_port

    def send_email(self):
        message = MIMEMultipart()
        if self.file:
            file_name = os.path.split(self.file)[-1]
            try:
                f = open(self.file, "rb").read()
            except Exception:
                raise Exception("附件不存在")
            else:
                att = MIMEText(f, "base64", "utf-8")
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
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        smtp.quit()
