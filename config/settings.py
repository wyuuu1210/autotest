import sys

if sys.argv[1] == "dev":
    from config.settings_dev import *
elif sys.argv[1] == "test":
    from config.settings_test import *

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


# 数据库配置
