#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 19:31
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : login_page.py
# @Software: PyCharm

from common.basepage import BasePage
from conf.settings import CONSOLE_PAGE_ELE
from util.parse_configuration_file import ParseConfigFile


class Login_Page(BasePage):

    parseCF = ParseConfigFile(CONSOLE_PAGE_ELE)
    section = parseCF.getItemSection('console_login_page')
    print("开始读取Console Login页面配置文件...\n", section)

    def select_login_server(self,value="qingcloud"):
        """选择登录服务器,testing环境会有这个选项"""
        ele = self.section['login.login_server']
        self.select(ele,value=value)

    def username(self,username):
        """输入用户名"""
        ele = self.section['login.form_input_username'.lower()]
        self.wait_ele_visible(ele)
        self.input(ele,username)

    def passwd(self,passwd):
        """输入密码"""
        ele = self.section['login.form_input_password'.lower()]
        self.wait_ele_visible(ele)
        self.input(ele,passwd)

    def submit(self):
        """点击登录按钮"""
        ele = self.section['login.submit_button'.lower()]
        self.wait_ele_visible(ele)
        self.click(ele)

    def get_alert_error_text(self):
        """获取登录失败的文本信息"""
        ele = self.section['login.alert_error'.lower()]
        self.wait_ele_visible(ele)
        value = self.get_ele_text(ele)
        return value

    def get_login_success_text(self):
        """获取登录成功后的文本信息"""
        ele = self.section['login.success_user_name'.lower()]
        self.wait_ele_visible(ele)
        value = self.get_ele_text(ele)
        if value:
            return True
        else:
            return False

