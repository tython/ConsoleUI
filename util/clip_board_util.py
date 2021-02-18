#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 23:37
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : clip_board_util.py
# @Software: PyCharm

import win32con
import win32clipboard as w

class Clipboard():
    """模拟Windows设置剪切板"""

    # 读取剪切板
    @staticmethod
    def getText():
        # 打开剪切板
        w.OpenClipboard()
        # 获取剪切板中的数据
        d = w.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪切板
        w.CloseClipboard()
        return d.decode('utf-8')

    # 设置剪切板内容
    @staticmethod
    def setText(aString):
        # 打开剪切板
        w.OpenClipboard()
        # 清空剪切板
        w.EmptyClipboard()
        # 将数据aString写入到剪切板
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        # 关闭剪切板
        w.CloseClipboard()

if __name__ == '__main__':
    Clipboard.setText("tyw")
    d = Clipboard.getText()