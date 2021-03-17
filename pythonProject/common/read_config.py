import os
from common import get_project_path
import configparser

project_path = get_project_path.get_path()
config_path = os.path.join(project_path, "config.ini")


class ReadConfig:
    def __init__(self):
        self.configparser = configparser.ConfigParser()
        self.configparser.read(config_path, encoding='utf-8')

    def get_base_url(self):
        base_url = self.configparser.get("HTTPS", "DEV_URL")
        return base_url

    def get_email_info(self):
        email_dict = {}
        username = self.configparser.get("EMAIL", "USER_NAME")
        password = self.configparser.get("EMAIL", "PASSWORD")
        on_off = self.configparser.get("EMAIL", "ON_OFF")
        subject = self.configparser.get("EMAIL", "SUBJECT")
        receiver = self.configparser.get("EMAIL", "RECEIVER")
        email_dict['sender'] = username
        email_dict['password'] = password
        email_dict['on_off'] = on_off
        email_dict['subject'] = subject
        email_dict['receiver'] = receiver
        return email_dict
