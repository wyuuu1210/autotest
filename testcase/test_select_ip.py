import ddt
from middle_handler.middlehandler import MiddleHandler
from common import requests_handler
import unittest
import json
from config import settings

test_data = MiddleHandler().get_test_data("select_ip")
logger = MiddleHandler().log_init()


@ddt.ddt()
class TestSelectIP(unittest.TestCase):
    """查询IP地址接口测试"""

    @ddt.data(*test_data)
    def test_select_ip(self, case_info):
        # print(case_info)
        url = settings.HOST["host2"] + case_info["url"]
        print(url)
        params = json.loads(case_info["params"])
        print(params)
        ret = requests_handler.Request().requests_handler(
            url=url,
            params=params,
            method="post"
        )
        print(ret)
        try:
            except_result = json.loads(case_info["expect_result"])
            self.assertEqual(except_result["error_code"], ret["error_code"])
            logger.info("断言成功")
        except Exception as e:
            logger.error("断言失败{}".format(e))
            raise e


if __name__ == '__main__':
    t = TestSelectIP()
    t.test_select_ip()
