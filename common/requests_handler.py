import requests


class Request(object):
    def __init__(self):
        self.request = requests

    def set_session(self):
        s = self.request.Session()
        self.request = s

    def requests_handler(self, url, method, headers=None, data=None, params=None, **kwargs):
        """
        请求接口
        :param url: 接口地址
        :param method: 访问方法
        :return:
        """
        r = self.request.request(method=method, url=url, headers=headers, data=data, params=params, **kwargs)

        res = r.json()
        ret = r.headers
        # ret2 = r.cookies

        try:
            return ret
        except Exception as error:
            return "返回的数据不是json{}".format(error)


if __name__ == '__main__':
    # import sys
    # print(sys.argv[0])
    # print(sys.argv[1].split("="))
    # print(sys.argv[2].split("="))
    ret = Request()
    ret.set_session()
    res = ret.requests_handler(
        url="http://v.juhe.cn/toutiao/index",
        method="post",
        params={"key": "37e47a2441ceb88ab3086574dc68f1e3", "type": "top"})
    print(res)


    # "type":"top","key":"37e47a2441ceb88ab3086574dc68f1e3"
