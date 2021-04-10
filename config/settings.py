import sys
import os


if (len(sys.argv))-1 < 1 or (len(sys.argv))-1 >1:
    exit("参数错误,请传入一个环境变量!比如: python xx.py dev|test")
else:
    if sys.argv[1] == "dev":
        from config.settings_dev import *
    elif sys.argv[1] == "test":
        from config.settings_test import *
    else:
        exit("参数错误,请传入dev或test")

# 邮箱配置
MAIL_CNF = {
    "smtp": {
        "smtp_host": "smtp.126.com",
        "port": 25,
        "user": "wyu1210@126.com",
        "password": "SCCPTFNPCCMQAFFM"
    },

    "to_list": ["1170816341@qq.com"],
    "cc_list": ["519738668@qq.com"]

}


# 路径配置
# 当前文件的绝对路径
file_path = os.path.abspath(__file__)
# print(file_path)

# 获取当前文件的目录路经
dir_path = os.path.dirname(__file__)
# print(dir_path)

# 获取项目路径
project_path = os.path.dirname(dir_path)
# print(project_path)

# 测试数据data文件路径
data_path = os.path.join(project_path, "data")

# test_log目录路经
test_log_path = os.path.join(project_path, "test_log")

# 测试报告路经
report_path = os.path.join(project_path,"reports")
# print(report_path)

# 测试用例路经
testcase_path = os.path.join(project_path, "testcase")
# print(testcase_path)



