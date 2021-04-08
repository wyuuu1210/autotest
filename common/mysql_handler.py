import pymysql
import sys
import os
# sys.path.insert(0, os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
from config.settings import MYSQL


def test():
    print(MYSQL["host"])
    print(MYSQL["port"])

# print(sys.path)
# if sys.argv[1] == "settings":
#     from config.settings import *

# print(settings.MAIL_CNF)
