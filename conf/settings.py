#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 23:37
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : settings.py
# @Software: PyCharm

import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 项目路径
LOG_DIR = os.path.join(BASE_PATH,'log') # 日志目录
CASE_DIR = os.path.join(BASE_PATH,'script') # Case目录
REPORT_DIR = os.path.join(BASE_PATH,'report') # 测试报告路径
LOG_FILE = os.path.join(LOG_DIR,'test_log.log') # 日志文件
SCREENSHOTDIR = os.path.join(BASE_PATH,'screenshot') # 异常截图目录

# 项目环境
CONSOLE_HOST_INFO = {
    "staging":"http://console.portal.staging.com/login",
    "testing":"http://console.qingcloud-portal.com/login",
    "product":"https://console.qingcloud.com/login",
    "preview":"https://pek2console3.qingcloud.com/login"
}

TESTER = "唐移维"  # 定义执行测试的tester

CONSOLE_PAGE_ELE = os.path.join(BASE_PATH,'conf','page_ele','page_ele.ini') # Console页面元素配置

PATTERN = '\$\{(.*?)\}'  # 参数替换规则，获取key

VERSION = 'xxx'  # 测试的版本

HUB_ADDRES = "http://192.168.12.88:4444/wd/hub" # 配置selenium_hub地址

# WebDriver驱动路径
chromeDriverFilePath = os.path.join(BASE_PATH,'drivers','chrome','chromedriver.exe')
ieDriverFilePath = os.path.join(BASE_PATH,'drivers','ie','IEDriverServer.exe')
firefoxDriverFilePath = os.path.join(BASE_PATH,'drivers','firefox','geckodriver.exe')
edgeDriverFilePath = os.path.join(BASE_PATH,'drivers','edge','msedgedriver.exe')
operaDriverFilePath = os.path.join(BASE_PATH,'drivers','opera','operadriver.exe')

if __name__ == "__main__":
    print(BASE_PATH)
    print(REPORT_DIR)
    print(chromeDriverFilePath)
    print(ieDriverFilePath)
    print(firefoxDriverFilePath)
    print(CONSOLE_HOST_INFO)


