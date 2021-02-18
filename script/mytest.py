#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 16:17
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : mytest.py
# @Software: PyCharm

CONSOLE_HOST_INFO = {
    "staging":"http://console.portal.staging.com/login",
    "testing":"http://console.qingcloud-portal.com/login",
    "production":"https://console.qingcloud.com/login",
    "pek2":"https://pek2console3.qingcloud.com/login"
}
print(list(CONSOLE_HOST_INFO.keys())[2])

if __name__ == '__main__':
    pass