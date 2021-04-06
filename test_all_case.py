from config import config_path,settings
import unittest
from HTMLTestRunner import HTMLTestRunnerNew
import time
import os
from common import send_email
from middle_handler import middlehandler

# print(config_path.testcase_path)
mail = send_email.Mail(
    settings.MAIL_CNF["smtp"]["smtp_host"],
    settings.MAIL_CNF["smtp"]["port"],
    settings.MAIL_CNF["smtp"]["user"],
    settings.MAIL_CNF["smtp"]["password"]
)

to_list = settings.MAIL_CNF["to_list"]
cc_list = settings.MAIL_CNF["cc_list"]
# 生成测试套件
test_loader = unittest.TestLoader()
testsuit = test_loader.discover(config_path.testcase_path)

# 使用HTMLTestRunner生成测试报告
report_name = "测试报告{}.html".format(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(report_name)
report_path = os.path.join(config_path.report_path, report_name)
# print(report_path)

with open(report_path, "wb") as f:
    HTMLTestRunnerNew.HTMLTestRunner(
        stream=f, title="自动化测试报告", description="api测试", tester="王钰").run(testsuit)

with open(report_path, "r") as e:
    HTMLReport = e.read()

mail.send("测试报告", HTMLReport, to_list, cc_list)