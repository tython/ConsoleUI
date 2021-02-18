#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 17:38
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : date_util.py
# @Software: PyCharm

import time,os
import calendar
import datetime


def calculate_function_run_time(func):
    """
    Calculate the running time of the function
    :param func: the function need to been calculated
    :return:s
    """
    def call_fun(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        end_time = time.time()
        print('%s() run time：%s s' % (func.__name__, int(end_time - start_time)))
        return f
    return call_fun

def calculate_function_run_time_ms(func):
    """
    Calculate the running time of the function
    :param func: the function need to been calculated
    :return:ms
    """
    def call_fun(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        end_time = time.time()
        print('%s() run time：%s ms' % (func.__name__, int(1000 * (end_time - start_time))))
        return f
    return call_fun

# def logger(flag = True):
#     """
#     打印函数耗时和记录函数耗时日志功能
#     :param flag: True运行时同时打印耗时和记录到日志中，False表示运行是只打印耗时且不记录耗时到日志中
#     :return:
#     """
#     def calculate_function_run_time(func):
#         def call_fun(*args,**kwargs):
#             start_time = time.time ()
#             func (*args, **kwargs)
#             end_time = time.time ()
#             print ('%s() run time：%s s' % (func.__name__, int (end_time - start_time)))
#             if flag:
#                 filePath = parentDirPath + r"\log" + time.strftime("\%Y-%m-%d",time.localtime(time.time()))
#                 if not os.path.exists(filePath):
#                     os.makedirs(filePath)
#                 with open((filePath + "\\" + func.__name__  + "_func_run_time" +".log"),"a+") as f:
#                     f.write('%s() run time：%s s' % (func.__name__, int (end_time - start_time)))
#         return call_fun
#     return calculate_function_run_time

def getTimeStamp():
    # 获取时间戳
    return time.time()

def mktime():
    # 转化为时间戳
    return time.mktime(time.localtime())

def getCurrentDate():
    # 获取当前日期eg:2019-1-27
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) + '-' + str(timeTup.tm_mon) + '-' + str(timeTup.tm_mday)
    return currentDate

def getCurrentTime():
    # 获取当前时间,eg:20_17_52_529533
    timeStr = datetime.datetime.now()
    # nowTime = timeStr.strftime('%H_%M_%S_%f')
    nowTime = timeStr.strftime('%H_%M_%S')
    return nowTime

def getHour_minute_second():
    """获取时分秒"""
    timeStr = datetime.datetime.now()
    nowHMS = timeStr.strftime ("%H-%M-%S")
    return nowHMS

def createCurrentDateDir():
    """在log目录下按照时间创建文件夹方法"""
    today = getCurrentDate()
    dateDir = os.path.join(os.path.dirname(LOG_PATH),today)
    if not os.path.exists(dateDir):
        os.makedirs(dateDir)
    return dateDir

def getCurrentDateAndTime():
    # 获取当前的日期和时间，例如:2019-10-13 03:54:54
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def getstrptime(param):
    # 转化为结构化时间.param接收例如：2019-11-24 19:50:20
    return time.strptime(param,"%Y-%m-%d %H:%M:%S")

def getLocaltime():
    # 获取本地时间
    return time.localtime(time.time())

def getFormatTime():
    # 获取格式化的时间
    return time.asctime(time.localtime(time.time()))

def getCalendarbyMonth(Years,Month):
    return calendar.month(Years, Month)

def create_dir(dir):
    # 创建目录
    dirName = os.path.join(dir,getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName