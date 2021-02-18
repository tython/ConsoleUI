#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 0:50
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : conftest_bak.py
# @Software: PyCharm

import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)))))
import pytest
import allure
from util.logger import logger
from common.driver import browser
from conf.settings import CONSOLE_HOST_INFO
from page_action.login_action import Login_Action
from data.login_module_data.login_data import normal_user
from conf import global_variable as gd


driver = None

def pytest_addoption(parser):
    """添加命令行参数-B"""
    parser.addoption(
        "-B", action="store", default="Chrome", help="browser option:Firefox or Chrome"
    )

@pytest.fixture(scope="session")
def init_log():
    print("\n开始初始化日志组件...")
    log = logger
    yield log
    print("关闭日志组件...")

@pytest.fixture(scope='session')
def driver():
    global driver
    print("开始初始化浏览器...")
    if hasattr(gd,"global_dict"):
        driver = gd.global_dict['driver']
        url = gd.global_dict['site']
    else:
        driver = browser()
        url = CONSOLE_HOST_INFO['product']
    driver.maximize_window()
    driver.get(url)
    print("打开测试站点:{0}".format(url))
    yield driver
    print("断开浏览器驱动...")
    driver.close()
    driver.quit()

@pytest.fixture(scope='session')
def init_db():
    print("开始初始化数据库连接操作...")
    yield
    print("释放数据库连接...")

@allure.title("前置操作：登录")
@pytest.mark.parametrize(normal_user,indirect=True)
@pytest.fixture(scope="module",autouse="true")
def login_console():
    global driver
    username = normal_user["username"]
    password = normal_user['password']
    print(f"登录账户:{username},登录的密码是:{password}")
    obj = Login_Action(driver)
    obj.console_login(username,password)
    return driver




skipif_win = pytest.mark.skipif(sys.platform == "win32",reason="windows上不能执行此用例...")
skipif_linux = pytest.mark.skipif(sys.platform == "linux",reason="linux上不能执行此用例...")