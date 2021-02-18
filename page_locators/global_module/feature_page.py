#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 11:51
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : feature_page.py
# @Software: PyCharm

from common.basepage import BasePage
from conf.settings import CONSOLE_PAGE_ELE
from util.parse_configuration_file import ParseConfigFile

class Feature_Page(BasePage):

    parseCF = ParseConfigFile(CONSOLE_PAGE_ELE)
    section_feature = parseCF.getItemSection('guide_feature_modal')

    def click_close(self):
        """关闭新功能介绍弹窗"""
        alert_ele = self.section_feature['feature.alert'.lower()]
        if self.wait_ele_visible(alert_ele):
            ele = self.section_feature['feature.close'.lower()]
            if self.wait_ele_visible(ele):
                self.click(ele)

    def guide_step_skip(self):
        """跳过引导"""
        ele = self.section_feature['feature.skip'.lower()]
        if self.wait_ele_visible(ele):
            self.sleep(1.5)
            self.click(ele)

    def guide_step_text(self):
        """获取步骤文本"""
        ele = self.section_feature['feature.text'.lower()]
        if self.wait_ele_visible(ele):
            return self.get_ele_text(ele)

    def guide_step_last(self):
        """点击上一步"""
        ele = self.section_feature['feature.last'.lower()]
        if self.wait_ele_visible(ele):
            self.click(ele)

    def guide_step_next(self):
        """点击下一步"""
        ele = self.section_feature['feature.next'.lower()]
        if self.wait_ele_visible(ele):
            self.click(ele)

    def guide_step_iknow(self):
        """点击下一步"""
        ele = self.section_feature['feature.iknow'.lower()]
        if self.wait_ele_visible(ele):
            self.click(ele)

if __name__ == '__main__':
    from common.driver import browser
    from conf.settings import CONSOLE_HOST_INFO
    from page_action.login_action import Login_Action
    driver = browser()
    driver.get(CONSOLE_HOST_INFO['production'])
    obj = Login_Action(driver)
    obj.console_login("yiweitang@yunify.com","HYz.510824")

    obj2 = Feature_Page(driver)
    obj2.click_close()
    obj2.guide_step_next()
    obj2.guide_step_next()
    obj2.guide_step_next()
    obj2.guide_step_iknow()







