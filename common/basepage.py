#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 10:00
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : common.py
# @Software: PyCharm

import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.tools import p
from util.logger import logger
from conf.settings import SCREENSHOTDIR
from util.clip_board_util import Clipboard
from util.key_board_util import KeyboardKeys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from util.date_util import create_dir,getCurrentTime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def split_locator(self,locator):
        """
        分解定位表达式
        :param locator:example=>'css=>.username'
        :return:('css selector', '.username')
        """
        by = locator.split('=>', 1)[0]
        value = locator.split('=>', 1)[1]
        locator_dict = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            error_message = "wrong locator! 'id','name','class','tag','link','plink','xpath','css',exp:'id=>username'"
            logger.logger.error(error_message)
            raise NameError(error_message)
        return locator_dict[by], value

    def wait_element(self, locator, sec=30):
        """
        等待元素出现
        :param localtor:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param sec:默认等待30秒
        :return: 元素出现返回True，元素未出现返回False
        """
        by,value = self.split_locator(locator)
        start_time = time.time()
        try:
            WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value),
                                                     message='element not found!!!')
            end_time = time.time()
            logger.logger.debug ("查找:{0}元素,耗时:{1}s".format (locator,round((end_time - start_time),4)))
            return True
        except TimeoutException as e:
            end_time = time.time()
            logger.logger.debug("查找:{0}元素失败,耗时:{1}s,原因:{2}".format(locator,round((end_time - start_time),4),str(e)))
            return False
        except Exception as e:
            end_time = time.time()
            logger.logger.debug("查找:{0}元素失败,耗时:{1}s,原因:{2}".format(locator,round((end_time - start_time),4),str(e)))
            raise e

    def wait_ele_visible(self,locator,sec=30,poll_frequency=1):
        """
        显示等待页面元素的出现在DOM中,并且可见,存在则返回该页面元素对象，定位器传入元祖类型
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param sec:等待秒数，默认30s
        :param poll_frequency:轮询频率，默认1s
        :return:
        """
        by, value = self.split_locator(locator)
        start_time = time.time ()
        try:
            if by.lower() == "id":
                element = WebDriverWait (self.driver, sec, poll_frequency).until(EC.visibility_of_element_located((By.ID,value)))
            elif by.lower() == "name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until(EC.visibility_of_element_located ((By.NAME, value)))
            elif by.lower() == "class name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.visibility_of_element_located ((By.CLASS_NAME, value)))
            elif by.lower() =="link text":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.visibility_of_element_located ((By.LINK_TEXT, value)))
            elif by.lower() =="partial link text":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.visibility_of_element_located ((By.PARTIAL_LINK_TEXT, value)))
            elif by.lower() =="tag name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.visibility_of_element_located ((By.TAG_NAME, value)))
            elif by.lower() =="xpath":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.visibility_of_element_located ((By.XPATH, value)))
            elif by.lower() =="css selector":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.visibility_of_element_located ((By.CSS_SELECTOR, value)))
            end_time = time.time()
            logger.logger.debug ("查找:{0}元素,耗时:{1}s".format (locator,round((end_time - start_time),4)))
        except Exception as e:
            end_time = time.time()
            logger.logger.debug("查找:{0}元素失败,耗时:{1}s,原因:{2}".format(locator, round((end_time - start_time), 4), str(e)))
            self.screen_shot()
            return False
        else:
            return element

    def wait_iframe_available(self,locator,sec=30,poll_frequency=1):
        """
        检查Frame是否存在,存在则切换进frame控件中，定位器传入元祖类型
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param sec:等待秒数，默认30s
        :param poll_frequency:轮询频率，默认1s
        :return:
        """
        by, value = self.split_locator(locator)
        start_time = time.time ()
        try:
            if by.lower() == "id":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.frame_to_be_available_and_switch_to_it ((By.ID, value)))
            elif by.lower() == "name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.frame_to_be_available_and_switch_to_it ((By.NAME, value)))
            elif by.lower() == "class name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.frame_to_be_available_and_switch_to_it ((By.CLASS_NAME, value)))
            elif by.lower() == "link text":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.frame_to_be_available_and_switch_to_it ((By.LINK_TEXT, value)))
            elif by.lower() == "partial link text":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.frame_to_be_available_and_switch_to_it ((By.PARTIAL_LINK_TEXT, value)))
            elif by.lower() == "tag name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.frame_to_be_available_and_switch_to_it ((By.TAG_NAME, value)))
            elif by.lower() == "xpath":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.frame_to_be_available_and_switch_to_it ((By.XPATH, value)))
            elif by.lower() == "css selector":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.frame_to_be_available_and_switch_to_it ((By.CSS_SELECTOR, value)))
            end_time = time.time ()
            logger.logger.debug ("查找:{0}元素,耗时:{1}s".format (locator,round((end_time - start_time),4)))
        except Exception as e:
            end_time = time.time()
            logger.logger.debug("查找:{0}元素失败,耗时:{1}s,原因:{2}".format(locator,round((end_time - start_time),4),str(e)))
            self.screen_shot ()
            return False
        else:
            return element

    def wait_ele_selection_state(self,locator,sec=30,poll_frequency=1):
        """
        判断一个元素的状态是否是给定的选择状态
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param sec:等待秒数，默认30s
        :param poll_frequency:轮询频率，默认1s
        :return:
        """
        by, value = self.split_locator(locator)
        start_time = time.time ()
        try:
            if by.lower() == "id":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.element_located_selection_state_to_be ((By.ID, value)))
            elif by.lower() == "name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.element_located_selection_state_to_be ((By.NAME, value)))
            elif by.lower() == "class name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.element_located_selection_state_to_be ((By.CLASS_NAME, value)))
            elif by.lower() == "link text":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.element_located_selection_state_to_be ((By.LINK_TEXT, value)))
            elif by.lower() == "partial link text":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.element_located_selection_state_to_be ((By.PARTIAL_LINK_TEXT, value)))
            elif by.lower() == "tag name":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.element_located_selection_state_to_be ((By.TAG_NAME, value)))
            elif by.lower() == "xpath":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.element_located_selection_state_to_be ((By.XPATH, value)))
            elif by.lower() == "css selector":
                element = WebDriverWait (self.driver, sec, poll_frequency).until (EC.element_located_selection_state_to_be ((By.CSS_SELECTOR, value)))
            end_time = time.time ()
            logger.logger.debug ("查找:{0}元素,耗时:{1}s".format (locator,round((end_time - start_time),4)))
        except Exception as e:
            end_time = time.time ()
            logger.logger.debug("查找:{0}元素失败,耗时:{1}s,原因:{2}".format(locator,round((end_time - start_time),4),str(e)))
            self.screen_shot ()
            return False
        else:
            return element

    def get_element(self, locator, sec=30):
        """
        获取一个元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param sec:等待秒数，默认30s
        :return: 元素可找到返回element对象，否则返回False
        """
        if self.wait_element(locator, sec):
            by, value = self.split_locator(locator)
            try:
                element = self.driver.find_element(by=by, value=value)
                logger.logger.debug(u'获取元素：%s' % locator)
                return element
            except Exception as e:
                raise e
        else:
            return False

    def get_elements(self, locator, sec=30, poll_frequency=1):
        """
        获取一组元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param sec:等待秒数，默认30s
        :param poll_frequency:轮询频率，默认1s
        :return: elements
        """
        by, value = self.split_locator(locator)
        try:
            elements = WebDriverWait(self.driver, sec, poll_frequency).until(lambda x: x.find_elements(by=by, value=value))
            logger.logger.debug(u'获取元素列表：%s' % locator)
            return elements
        except Exception as e:
            raise e

    def get_url(self):
        """
        获取当前网址
        :return: 返回网站地址
        """
        current_site_link = self.driver.current_url
        logger.logger.debug("当前网站地址：%s"%(current_site_link))
        return current_site_link

    def open(self,url):
        """
        打开网址
        :return:
        """
        self.driver.get(url)
        logger.logger.debug(u"打开网址：%s"%(url))

    def quit(self):
        """
        关闭相关驱动和所有窗口
        :return:
        """
        try:
            self.driver.quit()
            logger.logger.debug(u"关闭驱动和窗口成功")
        except Exception as e:
            logger.logger.error(e)
            raise e

    def close(self):
        """
        关闭窗口
        :return:
        """
        try:
            self.driver.close()
            logger.logger.debug(u"关闭窗口成功")
        except Exception as e:
            logger.logger.error(e)
            raise e

    def sleep(self,second):
        """固定等待"""
        time.sleep(int(second))
        logger.logger.debug(u"固定等待{0}s".format(second))

    def clear(self,locator):
        """
        清空文本框
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        try:
            self.get_element(locator).clear()
            logger.logger.debug(u"清空元素输入框成功")
        except Exception as e:
            logger.logger.error(u"清空输入框失败")
            self.screen_shot()
            raise e

    def input(self,locator,text):
        """
        输入框中输入内容
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param text: 预期要输入的文本
        :return:
        """
        try:
            self.get_element(locator).send_keys(text)
            logger.logger.debug(u"输入文本:{0}".format(text))
        except Exception as e:
            logger.logger.error(u"输入文本:{0},原因{1}".format(text,str(e)))
            self.screen_shot()
            raise e

    def input_all(self,locator,text):
        """
        在符合条件的所有元素中输入内容，依次循环输入text1,text2……
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param text: 输入的内容
        """
        allt = self.get_elements(locator)
        i = 1
        logger.logger.debug(u'开始执行type_all，共%s个元素' % (len(allt)))
        for ele in allt:
            newtext = text + str(i)
            ele.send_keys(newtext)
            logger.logger.debug(u'向第 %s 个元素输入文字：%s' % (i, newtext))
            i += 1

    def click(self,locator,repeat=0):
        """
        点击元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param repeat:重复次数标记，不要填写
        :return:
        """
        try:
            repeat += 1
            self.get_element(locator).click()
            logger.logger.debug(u"点击{0}元素".format(locator))
        except Exception as e:
            logger.logger.debug(u'点击元素：%s 第%s次执行失败' % (locator, repeat))
            if repeat > 2:
                raise e
            self.click(locator, repeat)

    def click_all(self, locator):
        """
        点击所有符合条件的元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        """
        allc = self.get_elements(locator)
        i = 0
        logger.logger.debug(u'开始执行click_all，共%s个元素' % (len(allc)))
        for ele in allc:
            self.sleep(0.3)
            ele.click()
            i += 1
            logger.logger.debug(u'点击第 %s 个元素' % i)

    def double_click(self, locator):
        """
        双击元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        """
        element = self.get_element(locator)
        ActionChains(self.driver).double_click(element).perform()
        logger.logger.debug(u'在元素上双击：%s' % locator)

    def double_click_all(self, locator):
        """
        双击所有符合条件的元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        """
        allc = self.get_elements(locator)
        i = 0
        logger.logger.debug(u'开始执行double_click_all，共%s个元素' % (len(allc)))
        for ele in allc:
            ActionChains(self.driver).double_click(ele).perform()
            i += 1
            logger.logger.debug(u'点击第 %s 个元素' % i)

    def right_click(self, locator):
        """
        鼠标右击元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        """
        element = self.get_element(locator)
        ActionChains(self.driver).context_click(element).perform()
        logger.logger.debug(u'在元素上右击：%s' % locator)

    def click_and_hold(self,locator):
        """
        对元素做按下鼠标左键的操作
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        try:
            ActionChains(self.driver).click_and_hold(self.get_element(self.driver,locator)).perform()
            ActionChains(self.driver).release(self.get_element(locator)).perform() # 释放按下的左键
            logger.logger.debug(u"在{0}元素上执行按下鼠标左键并保持".format(locator))
        except Exception as e:
            logger.logger.error(u"在{0}元素上执行按下鼠标左键并保持失败".format(locator))
            self.screen_shot()
            raise e

    def move_to_element(self,locator):
        """
        鼠标指向元素
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        try:
            ActionChains(self.driver).move_to_element(self.get_element(locator)).perform()
            logger.logger.debug(u"鼠标指向元素{0}".format(locator))
        except Exception as e:
            logger.logger.error(u"鼠标指向元素{0}失败，原因:{1}".format(locator,str(e)))
            self.screen_shot()
            raise e

    def drag_and_dorp(self,source_locator,target_locator):
        """
        拖动一个元素到另一个元素上
        :param source_locator:需要拖动的元素,定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param target_locator: 拖动到的目标元素,定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        try:
            source = self.get_element(source_locator)
            target = self.get_element(target_locator)
            ActionChains(self.driver).drag_and_drop(source,target).perform()
            logger.logger.debug(u"{0}元素拖动到{1}元素上".format(source,target))
        except Exception as e:
            logger.logger.error(u"{0}元素拖动到{1}元素上失败".format(source,target))
            self.screen_shot()
            raise e

    def drag_and_drop_by_offset(self,locator,offset_x,offset_y):
        """
        拖动一个元素移动x,y个偏移量
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param offset_x: X offset to move to
        :param offset_y: Y offset to move to
        :return:
        """
        try:
            ActionChains(self.driver).drag_and_drop_by_offset(self.get_element(locator),offset_x,offset_y).perform()
            logger.logger.debug(u"{0}元素从{1}滑动到{2}处".format(locator,offset_x,offset_y))
        except Exception as e:
            logger.logger.error(u"{0}元素从{1}滑动到{2}处失败".format(locator,offset_x,offset_y))
            self.screen_shot()
            raise e

    def maximize(self):
        """
        最大化浏览器窗口
        :return: 
        """
        try:
            self.driver.maximize_window()
            logger.logger.debug(u"最大化窗口")
        except Exception as e:
            logger.logger.error(u"执行最大化窗口失败")
            self.screen_shot()
            raise e

    def get_element_offset(self, locator):
        """
        获取元素坐标
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return: x,y
        """
        element = self.get_element(locator)
        loc = element.location
        x = loc['x']
        y = loc['y']
        logger.logger.debug(u'获取元素坐标：%s,%s' % (x, y))
        return x, y

    def get_element_offset_click(self, locator):
        """
        获取元素坐标并点击中间位置，适用于：元素A中套着元素B，元素B无法定位但元素A可以定位
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        """
        element = self.get_element(locator)
        loc = element.location
        x = loc['x']
        y = loc['y']
        size = element.size
        width = size['width']
        height = size['height']
        x += width
        y += height
        self.click_offset(x, y)

    def click_offset(self, x, y):
        """
        点击坐标
        :param x: x坐标'
        :param y: y坐标'
        """
        ActionChains(self.driver).move_by_offset(x, y).click().perform()
        logger.logger.debug(u'点击坐标%s,%s' % (x, y))

    def click_partial_text_link(self, text):
        """
        按部分链接文字查找并点击链接
        :param text: 链接的部分文字
        """
        self.get_element('plink,' + text).click()
        logger.logger.debug(u'点击连接：%s' % text)

    def get_window_position(self):
        """
        获取浏览器窗口尺寸大小
        :return:
        """
        try:
            position = self.driver.get_window_position()
            logger.logger.debug("窗口位置为：{0}".format(position))
            # print("Browser x => ",position['x'])
            # print("Browser y => ",position['y'])
            return position
        except Exception as e:
            logger.logger.error("获取浏览器窗口位置失败")
            self.screen_shot()
            raise e

    def set_window_position(self,x,y):
        """设置窗口的位置"""
        try:
            self.driver.set_window_position(x=x,y=y)
            logger.logger.debug(u"窗口位置设置为{0},{1}".format(x,y))
        except Exception as e:
            logger.logger.error(u"设置浏览器窗口位置失败")
            self.screen_shot()
            raise e

    def set_window_size(self,width,height):
        """设置浏览器窗口显示大小"""
        try:
            self.driver.set_window_size(width=width,height=height,windowHandle='current')
            logger.logger.debug(u"窗口大小设置为,width:{0},height:{1}".format(width,height))
        except Exception as e:
            logger.logger.error(u"浏览器窗口大小设置失败")
            self.screen_shot()
            raise e

    def get_window_size(self):
        """获取浏览器窗口的位置"""
        try:
            size = self.driver.get_window_size()
            logger.logger.debug("窗口位置为:{0}".format(size))
            # print("Browser width => ",size['width'])
            # print("Browser height => ",size['height'])
            return size
        except Exception as e:
            logger.logger.error("获取浏览器窗口位置失败")
            self.screen_shot()
            raise e

    def get_attribute(self,locator,attribute):
        """
        获取元素属性
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param attribute:属性名称
        :return:属性值
        """
        try:
            value = self.get_element(locator).get_attribute(attribute)
            logger.logger.debug(u"{0}元素的{1}属性值为:{2}".format(locator,attribute,value))
            return value
        except Exception as e:
            logger.logger.error(u"获取{0}元素的{1}属性值失败".format(locator,attribute))
            self.screen_shot()
            raise e

    def get_css_value(self,locator,key):
        """
        获取元素CSS属性
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :param key:css属性名称
        :return:属性值
        """
        try:
            css_value = self.get_element(locator).value_of_css_property(key)
            logger.logger.debug(u"获取{0}元素的{1}CSS属性值为:{2}".format(locator,key,css_value))
            return css_value
        except Exception as e:
            logger.logger.error(u"获取{0}元素的{1}CSS属性值失败".format(locator,key))
            self.screen_shot()
            raise e

    def get_title(self):
        """
        获取页面的title
        :return: title文本
        """
        try:
            title = self.driver.title
            logger.logger.debug("获取的Title为{0}".format(title))
            return title
        except Exception as e:
            logger.logger.error("获取页面Title失败")
            self.screen_shot()
            raise e

    def getPageSource(self):
        """
        获取页面源码
        :return: 源码文本
        """
        try:
            page_source = self.driver.page_source
            logger.logger.debug("获取页面源码")
            return page_source
        except Exception as e:
            logger.logger.error("获取页面源码失败")
            self.screen_shot()
            raise e

    def back(self):
        """
        浏览器后退操作
        :return:
        """
        self.driver.back()
        logger.logger.debug(u'页面后退')

    def forward(self):
        """
        浏览器前进操作
        :return:
        """
        self.driver.forward()
        logger.logger.debug(u'页面向前')

    def refresh(self):
        """刷新操作"""
        self.driver.refresh()
        logger.logger.debug(u"刷新页面")

    def get_capabilities(self):
        """
        获取浏览器详细信息
        :return: 浏览器详情
        """
        try:
            capabilities = self.driver.capabilities
            logger.logger.debug("浏览器详细信息为{0}".format(str(capabilities)))
            return capabilities
        except Exception as e:
            logger.logger.error("获取浏览器详细信息失败")
            self.screen_shot()
            raise e

    def get_driver_name(self):
        """
        获取Driver的名称
        :return: browser driver name property
        """
        driver_name = self.driver.name
        logger.logger.debug(u"当前使用的浏览器为:{0}".format(driver_name))
        return driver_name

    def set_page_load_timeout(self,second=10):
        """设置页面访问超时的最大值"""
        try:
            self.driver.set_page_load_timeout(second)
            logger.logger.debug("设置页面加载最大值为{}s".format(second))
        except Exception as e:
            logger.logger.error(e)
            raise e

    def switch_to_frame(self,locator):
        """
        进入frame
        :param locator:定位方法+定位表达式组合字符串，如'css,.username'
        :return:
        """
        try:
            e = self.get_element(locator)
            self.driver.switch_to.frame(e)
            logger.logger.debug("切换到{0}所在的iframe里".format(locator))
        except Exception as e:
            logger.logger.error("切换到iframe失败")
            self.screen_shot()
            raise e

    def switch_to_default_content(self):
        """
        退出frame返回默认文档
        :return:
        """
        try:
            self.driver.switch_to_default_content()
            logger.logger.debug(u"退出frame返回默认文档")
        except Exception as e:
            logger.logger.error(u"退出frame返回默认文档失败")
            self.screen_shot()
            raise e

    def switch_to_parent_frame(self):
        """
        切换到父frame
        :return:
        """
        try:
            self.driver.switch_to.parent_frame()
            logger.logger.debug(u"切换到父frame")
        except Exception as e:
            logger.logger.error(u"切换到父frame失败")
            self.screen_shot()
            raise e

    def get_current_window_handle(self):
        """
        获取当前页面的handle
        :return: handle object
        """
        try:
            current_window_handle = self.driver.current_window_handle
            logger.logger.debug(u"当前窗口的handle为{}".format(current_window_handle))
        except Exception as e:
            logger.logger.error(u"获取当前页面的handle失败")
            self.screen_shot()
            raise e

    def switch_to_window(self,locator=None):
        """
        点击元素打开新窗口，并将句柄切换到新窗口，如果传递定位表达式则点击并切换到新窗口，如果不传递定位表达式则切换到第一个窗口
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        try:
            if locator:
                element = self.get_element(locator)
                element.click()
                self.sleep(2)
                print(self.driver.window_handles)
                if self.driver.name == "chrome":
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                elif self.driver.name == "firefox":
                    self.driver.switch_to.window(self.driver.window_handles[1])
                else:
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                logger.logger.debug(u'点击元素打开新窗口')
            else:
                self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as e:
            logger.logger.error(u"切换窗口失败")
            self.screen_shot()
            raise e

    def get_ele_text(self,locator):
        """
        返回元素的文本
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:元素的文本
        """
        try:
            text = self.get_element(locator).text
            logger.logger.debug(u"{0}元素的text值为：{1}".format(locator,text))
            return text
        except Exception as e:
            logger.logger.error(u"获取{0}元素的text值失败".format(locator))
            self.screen_shot()
            raise e

    def get_element_info(self,locator):
        """
        获取元素的tag_name和size信息
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        try:
            element = self.get_element(locator)
            logger.logger.debug(u"{0}元素具体信息为:{1}".format(locator,element))
            return element.tag_name,element.size
        except Exception as e:
            self.screen_shot()
            logger.logger.error(u"获取元素信息失败")
            raise e

    def is_displayed(self,locator):
        """
        检查元素是否可见
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return: True or False
        """
        ele = self.get_element(locator)
        try:
            is_displayed = ele.is_displayed()
            logger.logger.debug(u"元素{0}可见状态是:{1}".format(locator,is_displayed))
            return is_displayed
        except Exception as e:
            logger.logger.error(u"获取元素可见状态失败")
            self.screen_shot()
            raise e

    def is_enabled(self,locator):
        """
        检查元素是否不可见
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        ele = self.get_element(locator)
        try:
            is_enabled = ele.is_enabled()
            logger.logger.debug(u"元素{0}不可见状态是:{1}".format(locator,is_enabled))
            return is_enabled
        except Exception as e:
            logger.logger.error(u"获取元素不可见状态失败")
            self.screen_shot()
            raise e

    def is_selected(self,locator):
        """
        检查元素是否已被选择
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        ele = self.get_element(locator)
        try:
            is_selected = ele.is_selected()
            logger.logger.debug(u"元素{0}选中状态为:{1}".format(locator,is_selected))
            return is_selected
        except Exception as e:
            logger.logger.error(u"检查元素是否已被选择失败,原因:{0}".format(str(e)))
            self.screen_shot()
            raise e

    def assert_string_in_pagesource(self,assert_str):
        """断言关键字是否在页面源码中"""
        try:
            assert assert_str in self.driver.page_source,f"not found {assert_str} in page source!"
        except AssertionError as e:
            logger.logger.error(e)
            raise AssertionError(e)
        except Exception as e:
            logger.logger.error(e)
            raise e

    def assert_title(self,title_str):
        """断言关键字是否在title中"""
        try:
            assert title_str in self.driver.title(),"not found {0} in title!".format(title_str)
        except AssertionError as e:
            logger.logger.error(e)
            raise AssertionError(e)
        except Exception as e:
            logger.logger.error(e)
            raise e

    def enter(self,locator):
        """
        enter快捷键
        :param locator:
        :return:
        """
        self.get_element(locator).send_keys(Keys.ENTER)
        try:
            logger.logger.debug(u"点击快捷键enter")
        except Exception as e:
            logger.logger.error(u"点击快捷键enter失败")
            self.screen_shot()
            raise e

    def paste(self,pasteString):
        """
        ctrl + v 快捷键
        :param pasteString:
        :return:
        """
        Clipboard.setText(pasteString)
        time.sleep(2)# 强行等待2s,防止代码执行太快，而未成功粘贴
        try:
            KeyboardKeys.twoKeys('ctrl','v')
            logger.logger.debug(u"ctrl + v字符串:{0}".format(pasteString))
        except Exception as e:
            logger.logger.error(u"粘贴:{0}字符串失败".format(pasteString))
            self.screen_shot()
            raise e

    def press_tab_key(self):
        """
        tab快捷键
        :return:
        """
        try:
            KeyboardKeys.oneKey('tab')
            logger.logger.debug(u"执行Tab快捷键")
        except Exception as e:
            logger.logger.error(u"执行tab快捷键失败")
            self.screen_shot()
            raise e

    def press_enter_key(self):
        """
        enter
        :return:
        """
        try:
            KeyboardKeys.oneKey('enter')
            logger.logger.debug("执行enter快捷键")
        except Exception as e:
            logger.logger.error("执行enter快捷键失败")
            self.screen_shot()
            raise e

    def get_cookies(self):
        """
        获取coolies
        :return:
        """
        try:
            cookies = self.driver.get_cookies()
            logger.logger.debug(u"cookies值为：{0}".format(cookies))
            return cookies
        except Exception as e:
            logger.logger.error(u"获取cookies失败")
            self.screen_shot()
            raise e

    def add_cookie(self,cookie_dict):
        """
        添加cookie
        Usage:
            driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
        :param cookie_dict:
        :return:
        """
        try:
            self.driver.add_cookie(cookie_dict)
            logger.logger.debug(u"添加cookie:{0}成功".format(cookie_dict))
        except Exception as e:
            logger.logger.error(u"添加cookies失败")
            self.screen_shot()
            raise e

    def delete_all_cookies(self):
        """
        删除所有的cookies
        :return:
        """
        try:
            self.driver.delete_all_cookies()
            logger.logger.debug(u"清空cookies")
        except Exception as e:
            logger.logger.error(u"清空cookies失败")
            self.screen_shot()
            raise e

    def screen_shot(self):
        """
        屏幕截图,名称:模块名_函数名_年月日时分秒
        :return: 图片名称:example:PageAction_screen_shot_13-19-03-410409.png
        """
        capture_dir = create_dir(SCREENSHOTDIR)
        module_name = os.path.basename(__file__).split('.')[0]
        fun_name = p.get_current_function_name()
        currTime = getCurrentTime()
        picNameAndPath = os.path.join(capture_dir,(module_name+"_"+fun_name+"_"+currTime+'.png'))
        try:
            self.driver.get_screenshot_as_file(picNameAndPath)
            logger.logger.debug(u"截图成功，文件路径为:{0}".format(picNameAndPath))
        except Exception as e:
            logger.logger.error(u"截图失败,原因{0}".format(e))
            raise e
        else:
            return picNameAndPath

    def js(self,script):
        """
        执行JavaScript
        :param param:js语句
        :return:
        """
        try:
            self.driver.execute_script(script)
            logger.logger.debug(u"执行js代码为{0}".format(script))
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_get_title(self):
        """
        js获取站点title方法
        :return:
        """
        try:
            title = self.js("document.title")
            logger.logger.debug(u"js获取title为{0}".format(title))
            return title
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_get_url(self):
        """
        js获取网址的方法
        :return:
        """
        try:
            js = "var a = document.URL;return a"
            return self.js(js)
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def window_stop(self):
        """
        js停止加载页面的方法
        """
        self.js('windos.stop()')

    def js_get_cookies(self):
        """
        js获取cookie的方法
        :return:
        """
        try:
            js = "var a = document.cookie;return a"
            return self.js(js)
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_open(self,url):
        """js打开站点的方法"""
        try:
            js = "var a = window.open('url');return a".format(url)
            return self.js(js)
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_location(self):
        """返回Location 对象属性"""
        dict = {}
        try:
            js1 = "var a = window.location;return a"
            # js2 = "var a = window.location.host;return a"
            # js3 = "var a = window.location.hostname;return a"
            # js4 = "var a = window.location.pathname;return a"
            # js5 = "var a = window.location.port;return a"
            # js6 = "var a = window.location.protocol;return a"
            # js7 = "var a = window.location.search;return a"
            # js8 = "var a = window.location.href;return a"
            dict['location'] = self.js(js1)
            # dict['host'] = self.js(js2)
            # dict['hostname'] = self.js(js3)
            # dict['pathname'] = self.js(js4)
            # dict['port'] = self.js(js5)
            # dict['protocol'] = self.js(js6)
            # dict['search'] = self.js(js7)
            # dict['href'] = self.js(js8)
            return dict
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_history_go(self,num=None):
        """js返回操作，同back"""
        try:
            if num is None:
                js = "var a = window.history.go(-1);return a"
            else:
                js = f"var a = window.history.go(-{int(num)});return a"
            self.js(js)
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_display_alert(self,showText=None):
        """弹出提示窗口"""
        try:
            js = f"alert('{showText}');"
            self.js(js)
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_get_screen_width_and_height(self):
        """
        获取屏幕的宽、高值
        :return:
        """
        dict = {}
        try:
            js1 = "var element = window.screen.width;return (element)"
            js2 = "var element = window.screen.height;return (element)"
            dict['width'] = self.js(js1)
            dict['height'] = self.js(js2)
            return dict
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_get_browser_visual_area_width_and_height(self):
        """
        获取屏幕可视区的宽、高值
        :return:
        """
        dict = {}
        try:
            js1 = "var element = document.body.clientWidth;return(element)"
            js2 = "var element = document.body.clientHeight;return(element)"
            dict['visual width'] = self.js(js1)
            dict['visual height'] = self.js(js2)
            return dict
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_send_keys(self,key,value):
        """
        js发送文本的方法，通过元素id
        :param key:
        :param value:
        :return:
        """
        try:
            self.js(f"document.getElementById('{key}').value='{value}'")
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_click_button(self,id):
        """
        js点击元素的方法
        :param id:
        :return:
        """
        try:
            self.js(f"document.getElementById('{id}').click()")
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_set_element_border(self,element):
        """
        高亮显示页面元素--设置边框为2px
        :param element:
        :return:
        """
        try:
            self.js(f'document.getElementById({element}).style.border="2px solid red";')
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_set_element_highlight(self,element):
        """
        高亮显示页面元素--设置文字颜色,颜色参照 http://www.w3school.com.cn/cssref/css_colors.asp
        :param element:
        :return:
        """
        try:
            self.js(f'document.getElementById({element}).style.color="#ff0000";')
        except Exception as e:
            logger.logger.error(e)
            self.screen_shot()
            raise e

    def js_scroll_top(self):
        """拖动浏览器右侧滑动条到页面顶部(非内嵌滚动条)"""
        if self.driver.name == 'chrome':
            js = 'var q=document.body.scrollTop=0'
        else:
            js = 'var q=document.documentElement.scrollTop=0'
        self.js(js) #self.js("window.scrollTo(document.body.scrollHeight,0)")

    def js_scroll_foot(self):
        """拖动浏览器右侧的滑动条到页面底部(非内嵌滚动条)"""
        if self.driver.name == "chrome":
            js = "var q=document.body.scrollTop=10000"
            return self.js(js)
        else:
            js = 'var q=document.documentElement.scrollTop=10000'
        self.js(js) #self.js("window.scrollTo(0,document.body.scrollHeight)")

    def js_scroll_in_to_view(self, param,view_position='true'):
        # WebDriverException，Cannot read property 'scrollIntoView' of null,发现了一个WebDriver的Bug，这里无法执行成功
        """
        将被遮挡的元素滚动到屏幕可见的地方
        param为元素的ID，view_position默认为true,表示将元素滚动到屏幕中间；当设置为false时，元素将滚动到屏幕的底部
        """
        self.js(f"document.getElementById('{param}').scrollIntoView({view_position});")

    def scroll_element_false(self,locator):
        """
        移动元素element对象底端与当前窗口的底部对齐
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        :return:
        """
        script = "arguments[0].scrollintoView(false);"
        element = self.get_element(locator)
        self.driver.execute_script(script, element)
        logger.logger.debug(u'滚动至元素：%s' % locator)

    def scroll_element(self, locator):
        """
        拖动滚动条至目标元素
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        script = "return arguments[0].scrollIntoView();"
        element = self.get_element(locator)
        self.driver.execute_script(script, element)
        logger.logger.debug(u'滚动至元素：%s' % locator)

    def js_scroll_to_foot(self):
        """将滚动条滑动到页面的最下方"""
        self.js("window.scrollTo(0,document.body.scrollHeight);")  # scrollTo是跳转到指定位置，括号里是位置的坐标

    def js_scroll_to_top(self):
        """将滚动条滑动到页面的最上方"""
        self.js("window.scrollTo(0,0);")  # scrollTo是跳转到指定位置，括号里是位置的坐标
        # self.js("window.scrollTo(document.body.scrollHeight,0);") # 方法二

    def js_scroll_by_offset(self, pixel_x=0, pixel_y=0):
        """
        将页面纵向上下滑动N个像素，pixel_y为负数表示向上滚动，pixel_y为正表示向下滚动
        将页面纵向左右滑动N个像素，pixel_x为负数表示向左滚动，pixel_x为正表示向右滚动
        """
        self.js(f"window.scrollBy({pixel_x},{pixel_y})")

    def switch_readonly(self,id):
        """去掉html只读属性"""
        self.js(f"document.getElementById('{id}').readOnly = false;")
        # 或者移除readonly属性
        # self.js(f"document.getElementById('{id}').removeAttribute("readonly");")

    def set_value(self,value):
        """设置html的value值"""
        self.js(f"document.getElementById('{id}').value = '{value}';")

    def js_get_src(self,locator):
        """
        返回文件的播放地址
        :param locator:定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        element = self.get_element(locator)
        return self.driver.execute_script("return arguments[0].currentSrc;",element)

    def js_play_video(self,locator):
        """
        播放视频
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css=>.username'
        :return:
        """
        element = self.get_element(locator)
        self.driver.execute_script("return arguments[0].play()",element)

    def js_pause_video(self,locator):
        """
        暂停播放
        :param locator:
        :return:
        """
        element = self.get_element(locator)
        self.driver.execute_script("return arguments[0].pause()",element)

    def alert_text(self,input_text=None,flag='accept'):
        """
        处理alert弹窗 => accept  or dismiss 并返回文本
        处理prompt弹框 => 输入文本，并accept  or dismiss
        :param flag: 模拟鼠标单击alert弹窗上的"确定"按钮；alert对象的dismiss()方法模拟"取消"按钮
        :return: text
        """
        try:
            alert = self.driver.switch_to.alert #获取alert对象
            self.sleep(2)
            if input_text:
                alert.send_keys(input_text)
            else:
                if flag == 'accept':
                    alert.accept()
                if flag == 'dismiss':
                    alert.dismiss()
                return alert.text
        except NoAlertPresentException as e:
            logger.logger.error(u"获取alert弹框中的text失败")
            self.screen_shot()
            raise e

    def select(self,locator,index=None,visible_text=None,value=None):
        """
        选择下拉框中的文本，通过is_enabled()和is_selected()方法
        获取选择项的3个方法
        select_by_index(param):通过下标
        select_by_visible_text(param)：通过文本值
        select_by_value(param)：通过value值
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.
        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against
        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>
            driver.select("#nr", '20')
            driver.select("xpath=>//[@name='NR']", '20')
        """
        select_ele = Select(self.get_element(locator))
        try:
            if index:
                select_ele.select_by_index(index)
            if visible_text:
                select_ele.select_by_visible_text(visible_text)
            if value:
                select_ele.select_by_value(value)
        except Exception as e:
            logger.logger.error(u"在{0}元素中选择下拉框中的{1}元素失败".format(locator,(index,visible_text,value)))
            self.screen_shot()
            raise e
        # #print default text
        # print(selectElement.first_selected_option.text)
        # allOptions = selectElement.options
        # print("total Options is: ",len(allOptions))
        # if allOptions[1].is_enabled() and not allOptions[1].is_selected():
        #     selectElement.select_by_index(1)   #另外还有select_by_visible_text() 和 select_by_value()来获取选项
        #     #打印已选项的文本
        #     print(selectElement.all_selected_options[0].text)

    def selectText(self,locator,expect_OptionsList=None):
        """断言选择框中的实际文本和预期列表中的文本是否一致，传一个预期列表参数和实际列表参数做断言"""
        if expect_OptionsList is None:
            expect_OptionsList = []
            selectElement = Select(self.get_element(self.driver,locator))
            actual_Options = selectElement.options
            actual_OptionsList = map(lambda option : option.text,actual_Options)


if __name__ == '__main__':
    from common.driver import browser
    bp = BasePage(browser())
    bp.open('http://www.baidu.com')
    bp.quit()