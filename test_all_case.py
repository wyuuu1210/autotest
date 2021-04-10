import sys
from config import settings
import unittest
from HTMLTestRunner import HTMLTestRunnerNew
import time
import os
from common import email_handler
# from common.mysql_handler import test


def run_all_case(tester):
    """测试所有用例"""


    # 生成测试套件
    test_loader = unittest.TestLoader()
    testsuit = test_loader.discover(settings.testcase_path)

    # 生成报告
    # 使用HTMLTestRunner生成测试报告
    report_name = "测试报告{}.html".format(time.strftime("%Y-%m-%d %H:%M:%S"))
    # print(report_name)
    report_path = os.path.join(settings.report_path + settings.REPORT_DIR["dir"], report_name)
    with open(report_path, "wb") as f:
        HTMLTestRunnerNew.HTMLTestRunner(
            stream=f, title="自动化测试报告", description="api测试", tester=tester).run(testsuit)

    # 发邮件
    mail = email_handler.Mail(
        settings.MAIL_CNF["smtp"]["smtp_host"],
        settings.MAIL_CNF["smtp"]["port"],
        settings.MAIL_CNF["smtp"]["user"],
        settings.MAIL_CNF["smtp"]["password"]
    )

    to_list = settings.MAIL_CNF["to_list"]
    cc_list = settings.MAIL_CNF["cc_list"]

    with open(report_path, "r") as e:
        HTMLReport = e.read()

    mail.send("测试报告", HTMLReport, to_list, cc_list)


if __name__ == '__main__':
    run_all_case("wangyu")
    # print(settings.REPORT_DIR, settings.DATA, settings.MYSQL)

