import ddt
from middle_handler.middlehandler import MiddleHandler
from common import requests_handler
import unittest
import json

test_data = MiddleHandler().get_test_data("news")

log = MiddleHandler().log_init()


@ddt.ddt
class TestNewsApi(unittest.TestCase):
    """新闻查询接口测试"""

    @ddt.data(*test_data)
    def test_news_api(self, case_info):
        print(case_info)
        url = MiddleHandler().get_conf_data()["host"] + case_info["url"]
        params = json.loads(case_info["params"])
        print(params)
        ret = requests_handler.requests_handler(url=url, method="post", params=params)
        print(ret)
        try:
            expect_result = json.loads(case_info["expect_result"])
            self.assertEqual(expect_result["error_code"], ret["error_code"])
            log.info("断言成功")
        except Exception as f:
            log.error("断言失败{}".format(f))
            # print("断言失败{}".format(f))


if __name__ == '__main__':
    a = TestNewsApi()
    a.test_news_api()
