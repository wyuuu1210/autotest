import logging


def get_log(name=None,
            level="DEBUG",
            fmt="%(asctime)s--%(filename)s--line:%(lineno)d--%(levelname)s:%(message)s",
            log_file=None):
    """输出test_case运行的日志"""

    # 通过logging.getLogger(name)来获取对象，可以直接向logger写入日志信息
    test_logger = logging.getLogger(name=name)
    test_logger.setLevel(level)

    # 设置日志输出格式
    log_fmt = logging.Formatter(fmt)

    # 日志输出到控制台
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(log_fmt)
    test_logger.addHandler(stream_handler)

    # 日志输出到文件
    if log_file:
        # 如果logging_file文件存在，将格式化的日志记录追加到文件logging_file中
        file_handler = logging.FileHandler(filename=log_file, mode="a", encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(log_fmt)
        test_logger.addHandler(file_handler)

    return test_logger


