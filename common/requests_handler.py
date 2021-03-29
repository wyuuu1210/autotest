import requests

def requests_handler(url, method, headers=None, data=None,params=None,**kwargs):
    """
    请求接口
    :param url: 接口地址
    :param method: 访问方法
    :return:
    """
    r = requests.request(method=method, url=url, headers=headers, data=data, params=params,**kwargs)

    res = r.json()

    try:
        return res
    except Exception as error:
        return "返回的数据不是json{}".format(error)



if __name__ == '__main__':
    ret = requests_handler(
        url="http://v.juhe.cn/toutiao/index",
        method="post",
        params={"key":"37e47a2441ceb88ab3086574dc68f1e3","type":"top"})
    print(ret)

    # "type":"top","key":"37e47a2441ceb88ab3086574dc68f1e3"