#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 19:40
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : login_action.py
# @Software: PyCharm

import allure
from page_locators.account_service.login_page import Login_Page

class Login_Action:

    def __init__(self,driver):
        self.driver = driver
        self.login = Login_Page(self.driver)

    def console_login(self,username=None,passwd=None):
        """Login Action"""
        try:
            # self.login.select_login_server()
            with allure.step("输入用户名"):
                self.login.username(username)
            with allure.step("输入密码"):
                self.login.passwd(passwd)
            with allure.step("点击登录按钮"):
                self.login.submit()
        except Exception as e:
            print(e)
            raise e

    def assert_error_text(self):
        """断言错误提示框文本"""
        return self.login.get_alert_error_text()

    def assert_success_text(self):
        """断言登录成功后的文本"""
        return self.login.get_login_success_text()


if __name__ == '__main__':
    from common.driver import browser
    from conf.settings import CONSOLE_HOST_INFO
    driver = browser()
    driver.get(CONSOLE_HOST_INFO['production'])
    obj = Login_Action(driver)
    obj.console_login("yiweitang@yunify.com","HYz.510824")
    print(obj.assert_success_text())