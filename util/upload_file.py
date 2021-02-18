#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 21:38
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : upload_file.py
# @Software: PyCharm


"""
win32gui.FindWindow(ipClassName,ipWindowsName)
自顶层窗口开始寻找匹配条件的窗口,并返回这个窗口的句柄
ipClassName:类名，在Spy++里能够看到；ipWindowsName:窗口名，标题栏能够看到

win32gui.FindWindowEx(hwndParent=0,hwndChildAfter=0,ipszClass=None,ipsxWindow=None)
搜索类名和窗体名匹配的窗体，并返回这个窗体的句柄，找不到就返回0
hwndParent:若不为0，则搜索句柄为hwndParent的子窗体
hwndChildAfter:若不为0，则按照z-index的顺序从hwndChildAfter后开始搜索子窗体，否则从第一个子窗体开始搜索
ipszClass:字符型，是窗体的类名，可以在Spy++里能够看到
ipsxWindow:字符型，是窗口名，标题栏能看到

win32gui.SendMessage(hWnd,Msg,wParam,IParam)
hWnd:整形，接收消息的窗体句柄
Msg:整形，要发送的消息，这些消息都是windows预先设置好的
wParam:整形，消息的wParam参数
IParam:整形，消息的IParam参数
"""


import win32gui
import win32con


def upload_file_by_chrome(filepath,syslanguage="en"):
    """
    谷歌浏览器上传文件控件
    :param filepath:上传文件的路径
    :param syslanguage:操作系统当前的语言环境,默认为en
    :return:None
    """
    if syslanguage == "ch":
        dialog = win32gui.FindWindow ("#32770", "打开")
    elif syslanguage == "en":
        dialog = win32gui.FindWindow("#32770", "open")
    else:
        print("不支持的语言!")
    print(dialog)
    # 找到窗口
    comboxex32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    print(comboxex32)
    combox = win32gui.FindWindowEx(comboxex32,0,"ComboBox",None)
    print(combox)
    edit = win32gui.FindWindowEx(combox,0,"Edit",None)
    print(edit)
    if syslanguage == "ch":
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
    elif syslanguage == "en":
        button = win32gui.FindWindowEx(dialog, 0, "Button", "&Open")
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath)
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button) # 点击打开按钮

def upload_file_by_firefox(filepath,syslanguage="ch"):
    """
    火狐浏览器上传文件控件
    :param filepath:上传文件的路径
    :param syslanguage:操作系统当前的语言环境,默认为en
    :return:None
    """
    if syslanguage == "ch":
        dialog = win32gui.FindWindow ("#32770", "文件上传")
    elif syslanguage == "en":
        dialog = win32gui.FindWindow("#32770", "open")
    else:
        print("不支持的语言!")
    print(dialog)
    # 找到窗口
    comboxex32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    print(comboxex32)
    combox = win32gui.FindWindowEx(comboxex32,0,"ComboBox",None)
    print(combox)
    edit = win32gui.FindWindowEx(combox,0,"Edit",None)
    print(edit)
    if syslanguage == "ch":
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
    elif syslanguage == "en":
        button = win32gui.FindWindowEx(dialog, 0, "Button", "&Open")
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath)
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button) # 点击打开按钮

if __name__ == '__main__':
    # upload_file_by_chrome(r"C:\Users\Administrator\Desktop\clips\A.mov")
    upload_file_by_firefox(r"C:\Users\Administrator\Desktop\clips\A.mov")