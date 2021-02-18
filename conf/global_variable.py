#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 0:57
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : global_variable.py
# @Software: PyCharm

import os


def init():
    global global_dict
    global_dict = {}
    # 代码根目录
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 存放程序所在目录
    global_dict['root_path'] = root_dir
    # 存放正常截图文件夹
    global_dict['screenshot_path'] = "{}\\screenshot\\".format(root_dir)
    # 下载文件夹
    global_dict['download_path'] = "{}\\file\\download\\".format(root_dir)
    # 上传文件夹
    global_dict['upload_path'] = "{}\\file\\upload\\".format(root_dir)
    # 存放报告路径
    global_dict['report_path'] = "{}\\report\\".format(root_dir)
    # 存放用户数据的路径
    global_dict['user_data'] = "{}\\file\\user_data\\".format(root_dir)
    # 保存driver
    global_dict['driver'] = "{}\\drivers\\chrome\\chromedriver.exe".format(root_dir)
    # 设置运行环境网址主页
    global_dict['site'] = 'https://console.qingcloud.com/'
    # 运行环境，默认preview，可设为product
    global_dict['environment'] = 'product'
    # 测试的浏览器
    global_dict['driver_name'] = 'chrome'
    # 指定在本地或者远程进行测试
    global_dict['run_addres'] = 'local'

def set_value(name, value):
    """
    修改全局变量的值
    :param name: 变量名
    :param value: 变量值
    """
    global_dict[name] = value

def get_value(name, def_val='no_value'):
    """
    获取全局变量的值
    :param name: 变量名
    :param def_val: 默认变量值
    :return: 变量存在时返回其值，否则返回'no_value'
    """
    try:
        return global_dict[name]
    except KeyError:
        return def_val


if __name__ == '__main__':
    init()
    print(global_dict)