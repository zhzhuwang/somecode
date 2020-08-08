import logging
from scripts.config import TEST_LOGS_PATH


class HandleLog:

    def __init__(self):
        # 日志收集器及收集等级
        self.case_logger = logging.getLogger("case")
        self.case_logger.setLevel("DEBUG")
        # 输出渠道
        console_handle = logging.StreamHandler()
        file_handle = logging.FileHandler(TEST_LOGS_PATH, encoding="utf-8")
        # 输出渠道的日志等级
        console_handle.setLevel("ERROR")
        file_handle.setLevel("DEBUG")
        # 日志显示格式
        simple_formatter = logging.Formatter("%(asctime)s  [%(levelname)s]  [msg]%(message)s")
        verbose_formatter = logging.Formatter(
            "%(asctime)s  [%(levelname)s]  [msg]%(message)s - %(filename)s - %(lineno)d")
        # 绑定输出渠道
        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter(verbose_formatter)
        # 将日志收集器与输出渠道进行对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        return self.case_logger


do_logger = HandleLog().get_logger()

if __name__ == '__main__':
    case_logger = HandleLog().get_logger()
    case_logger.info("这是一条info级别的日志。")
    case_logger.error("这是一条error级别的日志。")
