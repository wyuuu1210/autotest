import os
from common import read_test_data
from config import settings
from common import test_log


class MiddleHandler(object):

    # def get_conf_data(self):
    #     """读取conf.yaml文件"""
    #     return read_config.read_config(config_path.conf_path)

    def get_test_data(self, sheet):
        """读取data.xlsx的结果"""
        path = os.path.join(settings.data_path, settings.DATA["file_name"])
        test_data = read_test_data.ReadExcel().read_sheet(path, sheet)
        return test_data

    def log_init(self):
        """log初始化"""
        log_path = os.path.join(settings.test_log_path, settings.LOG["log_file"])
        logger = test_log.get_log(name=settings.LOG["name"], level=settings.LOG["level"], log_file=log_path)
        return logger


if __name__ == '__main__':
    a = MiddleHandler()
    b = a.get_test_data("news")
    print(b)