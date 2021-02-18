#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 17:52
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : feature_action.py
# @Software: PyCharm

import allure
from page_locators.global_module.feature_page import Feature_Page


class Feature_Action(Feature_Page):

    def close_workbench_window(self):
        """导航到主机页面"""
        with allure.step("关闭新功能介绍窗口"):
            self.click_close()
        with allure.step("跳过新功能介绍步骤"):
            self.guide_step_skip()

    def skip(self):
        """跳过引导弹框"""
        with allure.step("跳过引导弹框"):
            self.guide_step_skip()