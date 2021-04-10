import pymysql
# import sys
# import os
# sys.path.insert(0, os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
from config.settings import MYSQL


class MysqlHandler(object):

    def __init__(self, MQ):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MQ["host"],
            port=MQ["port"],
            user=MQ["user"],
            password=MQ["password"],
            database=MQ["database"],
            cursorclass="DictCusor"
        )
        # 创建游标：相当于进入 mysql> 命令操作界面
        self.cursor = self.connect.cursor()

    def query_data(self, sql):
        # 查询数据
        # 执行sql
        self.cursor.execute(sql)
        # 获取结果
        res = self.cursor.fetchall()
        if res:
            return res
        else:
            return None

    def commit_data(self, sql):
        # 增加、删除、修改数据
        self.cursor.execute(sql)
        self.connect.commit()

    def close_connect(self):
        # 关闭连接
        self.cursor.close()
        self.connect.close()



if __name__ == '__main__':
    t = MysqlHandler(MYSQL)
