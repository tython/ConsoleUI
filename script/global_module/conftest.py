#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 16:07
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : conftest_bak.py
# @Software: PyCharm

import pytest
from page_locators.global_module.global_page import Global_Page
from page_action.feature_action import Feature_Action

@pytest.fixture(autouse="true")
@pytest.mark.usefixtures('driver')
def workbench(driver):
    obj = Global_Page(driver)
    obj.click_workbench()
    return driver

@pytest.fixture(scope="class",autouse="true")
@pytest.mark.usefixtures('driver')
def operation_feature(driver):
    obj = Feature_Action(driver)
    obj.close_workbench_window()

