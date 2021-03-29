from common import read_config
from common import read_test_data
from config import config_path
from common import test_log
import os

class MiddleHandler(object):

    def get_conf_data(self):
        """读取conf.yaml文件"""
        return read_config.read_config(config_path.conf_path)

    def get_test_data(self, sheet):
        """读取data.xlsx的结果"""
        conf_data = self.get_conf_data()
        path = os.path.join(config_path.data_path, conf_data["test_data"]["file_name"])
        test_data = read_test_data.ReadExcel().read_sheet(path, sheet)
        return test_data

    def log_init(self):
        """log初始化"""
        conf_data = self.get_conf_data()
        log_conf = conf_data["log"]
        log_path = os.path.join(config_path.test_log_path, log_conf["log_file"])
        logger = test_log.get_log(name=log_conf["name"],level=log_conf["level"],log_file=log_path)
        return logger


# if __name__ == '__main__':
#     a = Middle_Handler()
#
#     b = a.get_test_data("news")
#     print(b)