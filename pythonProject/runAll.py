import os
import unittest
from common import read_config, config_email, HTMLTestRunner, log, get_project_path

log = log.logger
mail_info = read_config.ReadConfig().get_email_info()
username = mail_info['sender']
password = mail_info['password']
title = mail_info['subject']
receiver = mail_info['receiver'].split(",")
on_off = mail_info['on_off']

path = get_project_path.get_path()
report_path = os.path.join(path, "reports")

send_mail = config_email.ConfigEmail(
    username=username,
    password=password,
    receivers=receiver,
    title=title,
    content='test',
    file=os.path.join(report_path, "test_report.html")
)


class AllTest:
    def __init__(self):
        self.result_path = os.path.join(report_path, "test_report.html")
        self.case_list_file = os.path.join(path, "case_list.txt")
        self.case_file = os.path.join(path, "testCases")
        self.case_list = []
        log.info('result_path-{}'.format(self.result_path))

    def set_case_list(self):
        with open(self.case_list_file) as fb:
            for value in fb.readlines():
                data = str(value)
                if data != "" and not data.startswith("#"):
                    self.case_list.append(data.replace("\n", ""))

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.case_list:
            case_name = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(start_dir=self.case_file, pattern=case_name+'.py', top_level_dir=None)
            suite_module.append(discover)
        if suite_module:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        suite = self.set_case_suite()
        if suite:
            with open(self.result_path, 'wb') as fp:
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test report', description='test results')
                runner.run(suite)
        else:
            print("no case!")
        if on_off == "on":
            send_mail.send_email()
        else:
            print("do not send email!")


if __name__ == "__main__":
    AllTest().run()
