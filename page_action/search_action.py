#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 15:26
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : search_action.py
# @Software: PyCharm

import allure
from page_locators.global_module.global_page import Global_Page

class Search_Action(Global_Page):

    def search(self,content):
        """输入框中输入检索内容"""
        with allure.step("点击搜索框"):
            self.click_search_box()
        with allure.step("输入检索条件并点击enter"):
            self.input_search_content_and_enter(content)


if __name__ == '__main__':
    from common.driver import browser
    from conf.settings import CONSOLE_HOST_INFO
    driver = browser()
    driver.get(CONSOLE_HOST_INFO['pek2'])
    obj = Search_Action(driver)
    obj.search("主机")


