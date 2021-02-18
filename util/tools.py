#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 16:04
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : util.py
# @Software: PyCharm

import sys,inspect
import ctypes
import locale
import socket

class GetCurrentItems(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        pass

    @staticmethod
    def get_current_file_path():
        """获取当前文件路径"""
        return __file__

    def get_current_class_name(self):
        """获取当前类的类名"""
        return self.__class__.__name__

    @staticmethod
    def get_current_function_name():
        """获取函数名称"""
        return inspect.stack()[1][3]

    @staticmethod
    def get_current_lineno():
        """获取当前行数"""
        return sys._getframe().f_lineno

    @staticmethod
    def get_func_name():

        import sys
        try:
            raise Exception
        except:
            exc_info = sys.exc_info()  # 返回 异常类型，异常，traceback对象
            traceObj = exc_info[2]  # traceback对象
            frameObj = traceObj.tb_frame  # 获取frame对象，即本函数的frame信息
            # print frameObj.f_code.co_name,frameObj.f_lineno         #请在使用的时候将其注释
            Upframe = frameObj.f_back  # 获取该代码段的frame信息，即调用该函数的函数frame
            # print Upframe.f_code.co_name, Upframe.f_lineno          #请在使用的时候将其注释
            return (Upframe.f_code.co_name, Upframe.f_lineno)[0]  # 获取名称

    @staticmethod
    def getCurRunPosInfo():
        import sys
        try:
            raise Exception
        except:
            exc_info = sys.exc_info()
            traceObj = exc_info[2]
            frameObj = traceObj.tb_frame
            # print frameObj.f_code.co_name,frameObj.f_lineno
            Upframe = frameObj.f_back
            # print Upframe.f_code.co_name, Upframe.f_lineno
            return (Upframe.f_code.co_filename, Upframe.f_code.co_name, Upframe.f_lineno)

class GetLang:
    """获取语言"""
    @staticmethod
    def get_sys_lang():
        """
        获取系统语言
        :return:
        """
        dll_handle = ctypes.windll.kernel32
        sys_lang = hex(dll_handle.GetSystemDefaultUILanguage())
        return sys_lang

    @staticmethod
    def get_loc_lang():
        """
        获取区域语言
        :return:
        """
        loc_lang = locale.getdefaultlocale()
        return loc_lang

class GetIp:
    """获取本机ip"""
    @staticmethod
    def get_ip():
        """获取本机的ip地址"""
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip


# 单例模式，不用重复创建对象，可在其他模块直接调用p实例下的方法
p = GetCurrentItems()

if __name__ == '__main__':
    print(p.get_current_file_path())
    print(p.get_current_class_name())
    print(p.get_current_function_name())
    print(p.get_current_lineno())
    print(GetLang.get_sys_lang())
    print(GetLang.get_loc_lang())
    print(GetIp.get_ip())
    print(p.get_func_name())
    print(p.getCurRunPosInfo())