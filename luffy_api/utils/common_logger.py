# -*- coding: utf-8 -*-
# author : heart
# blog_url : https://www.cnblogs.com/ssrheart/
# time : 2024/5/9
from loguru import logger
import os

LOG_PATH = os.path.join("logs", "luffy.log")


def configure_logger():
    # logger.remove()  # 清除默认的日志处理器
    # logger.level("CRITICAL")
    logger.add(f"{LOG_PATH}", rotation="300 MB", level="ERROR")
