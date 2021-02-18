#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 18:19
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : file_util.py
# @Software: PyCharm


import os

def create_forder(path):
    """创建文件夹"""
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    UI_LOG = os.path.join(parentDirPath, 'log', 'ui')
    create_forder(UI_LOG)