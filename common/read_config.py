import yaml
from config import config_path

def read_config(config_path):
    """
    读取配置文件
    :param config_path: 配置文件路径
    :return: 以key:value的形式返回
    """

    with open(config_path, "r", encoding="utf-8") as f:
        config_info = yaml.load(stream=f, Loader=yaml.SafeLoader)
    return config_info


if __name__ == '__main__':
    test = read_config(config_path.conf_path)
    print(test)