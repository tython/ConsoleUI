#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 23:20
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : account_service.py
# @Software: PyCharm

import allure
import pytest
from page_action.login_action import Login_Action
from data.login_module_data.login_data import userlist

@pytest.mark.skip(reason="跳过执行这条case")
@allure.testcase("https://pek2console3.qingcloud.com/login")
@allure.feature("登录模块")
@pytest.mark.usefixtures("init_log")
class Test_Login():

    @allure.title("正确的用户名和错误的密码登录测试")
    @pytest.mark.skip(reason="跳过执行这条case")
    @pytest.mark.parametrize("item", userlist)
    @pytest.mark.passwd_error
    @pytest.mark.usefixtures("init_driver")
    def test_console_login_fail(self,item,init_driver):
        """正确的用户名和错误的密码登录"""
        print("测试数据：",item)
        obj = Login_Action(init_driver)
        obj.console_login(item['username'],item['password'])
        assert obj.assert_success_text() == True, "测试失败"

    @allure.feature('正确的用户名和正确的密码登录测试')
    @allure.title("正确的用户名和正确的密码登录测试")
    @pytest.mark.skip(reason="跳过执行这条case")
    @pytest.mark.parametrize("item", userlist)
    @pytest.mark.login_success
    @pytest.mark.usefixtures("init_driver")
    def test_console_login_success(self,item,init_driver):
        """正确的用户名和密码登录成功"""
        print("测试数据：",item)
        obj = Login_Action(init_driver)
        obj.console_login(item['username'], item['password'])
        assert obj.assert_success_text() == True, "测试失败"


if __name__ == '__main__':
    pytest.main(['-rs','test_login.py'])