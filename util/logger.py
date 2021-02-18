#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 18:41
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : logger_bak.py
# @Software: PyCharm

import os
import logging
from logging import handlers
from util.date_util import create_dir
from conf.settings import LOG_DIR


class Logger(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls,*args)
        return cls.__instance

    def __init__(self,logger='root'):
        dir = create_dir(LOG_DIR)
        LOG_FILE = os.path.join(dir,'test_log.log')
        self.formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(pathname)s] : %(funcName)s:%(lineno)d , %(message)s')
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.filelogger = handlers.RotatingFileHandler(filename=LOG_FILE,
                                                       mode='a',
                                                       maxBytes=10485760,#10M
                                                       backupCount=10,#最多备份10个
                                                       encoding='utf-8')
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)
        self.filelogger.setFormatter(self.formatter)
        self.console.setFormatter(self.formatter)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

logger = Logger()


if __name__ == '__main__':
    logger.logger.debug ('this is a debug')
    logger.logger.info ('this is a info')
    logger.logger.warning ('this is a warning')
    logger.logger.warn ('this is a warn')
    logger.logger.error ('this is a error')
    logger.logger.critical ('this is a critical')