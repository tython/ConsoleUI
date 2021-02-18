#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 23:37
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : key_board_util.py
# @Software: PyCharm

import win32api
import win32con
import win32clipboard as w

class KeyboardKeys():
    """Analog keyboard keys class"""
    VK_CODE = {
        'backspace': 0x08,
        'tab': 0x09,
        'clear': 0x0c,
        'enter': 0x0D,
        'shift': 0x10,
        'ctrl': 0x11,
        'alt': 0x12,
        'pause': 0x13,
        'caps_lock': 0x14,
        'esc': 0x1B,
        'spacebar': 0x20,
        'page_up': 0x21,
        'page_down': 0x22,
        'end': 0x23,
        'home': 0x24,
        'left_arrow': 0x25,
        'up_arrow': 0x26,
        'right_arrow': 0x27,
        'down_arrow': 0x28,
        'select': 0x29,
        'print': 0x2A,
        'execute': 0x2B,
        'print_screen': 0x2C,
        'ins': 0x2D,
        'del': 0x2E,
        'help': 0x2F,
        '0': 0x30,
        '1': 0x31,
        '2': 0x32,
        '3': 0x33,
        '4': 0x34,
        '5': 0x35,
        '6': 0x36,
        '7': 0x37,
        '8': 0x38,
        '9': 0x39,
        'a': 0x41,
        'b': 0x42,
        'c': 0x43,
        'd': 0x44,
        'e': 0x45,
        'f': 0x46,
        'g': 0x47,
        'h': 0x48,
        'i': 0x49,
        'j': 0x4A,
        'k': 0x4B,
        'l': 0x4C,
        'm': 0x4D,
        'n': 0x4E,
        'o': 0x4F,
        'p': 0x50,
        'q': 0x51,
        'r': 0x52,
        's': 0x53,
        't': 0x54,
        'u': 0x55,
        'v': 0x56,
        'w': 0x57,
        'x': 0x58,
        'y': 0x59,
        'z': 0x5A,
        'numpad_0': 0x60,
        'numpad_1': 0x61,
        'numpad_2': 0x62,
        'numpad_3': 0x63,
        'numpad_4': 0x64,
        'numpad_5': 0x65,
        'numpad_6': 0x66,
        'numpad_7': 0x67,
        'numpad_8': 0x68,
        'numpad_9': 0x69,
        'multiply_key': 0x6A,
        'add_key': 0x6B,
        'separator_key': 0x6C,
        'subtract_key': 0x6D,
        'decimal_key': 0x6E,
        'divide_key': 0x6F,
        'F1': 0X70,
        'F2': 0X71,
        'F3': 0X72,
        'F4': 0X73,
        'F5': 0X74,
        'F6': 0X75,
        'F7': 0X76,
        'F8': 0X77,
        'F9': 0X78,
        'F10': 0X79,
        'F11': 0X7A,
        'F12': 0X7B,
        'F13': 0X7C,
        'F14': 0X7D,
        'F15': 0X7E,
        'F16': 0X7F,
        'F17': 0X80,
        'F18': 0X81,
        'F19': 0X82,
        'F20': 0X83,
        'F21': 0X84,
        'F22': 0X85,
        'F23': 0X86,
        'F24': 0X87,
        'num_lock': 0x90,
        'scroll_lock': 0x91,
        'left_shift': 0xA0,
        'right_shift': 0xA1,
        'left_control': 0xA2,
        'right_control':0xA3,
        'left_menu': 0xA4,
        'right_menu': 0xA5,
        'browser_back':0xA6,
        'browser_forward': 0xA7,
        'browser_refresh': 0xA8,
        'browser_stop': 0xA9,
        'browser_search': 0xAA,
        'browser_favorites': 0xAB,
        'browser_start_and_home': 0xAC,
        'voleme_mute': 0xAD,
        'voleme_down': 0xAE,
        'voleme_up': 0xAF,
        'next_track': 0xB1,
        'stop_media': 0xB2,
        'play/pause_media': 0xB3,
        'start_mail': 0xB4,
        'select_media': 0xB5,
        'start_application_1': 0xB6,
        'start_application_2': 0xB7,
        'attn_key': 0xF6,
        'crsel_key': 0xF7,
        'exsel_key': 0xF8,
        'play_key': 0xFA,
        'zoom_key': 0xFB,
        'ckear_key': 0xFE,
        '+': 0xBB,
        ',': 0xBC,
        '-': 0xBD,
        '.': 0xBE,
        '/': 0xBF,
        '`': 0xC0,
        ';': 0xBA,
        '[': 0xDB,
        '\\': 0xDC,
        ']': 0xDD,
        "'": 0xDE
    }

    @staticmethod
    def keyDown(keyName):
        """按下按键"""
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0, 0, 0)

    @staticmethod
    def keyUp(keyName):
        """释放按键"""
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0,win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def oneKey(key):
        """模拟单个按键,按下并释放"""
        KeyboardKeys.keyDown(key)
        KeyboardKeys.keyUp(key)

    @staticmethod
    def twoKeys(key1,key2):
        """模拟两个按键"""
        KeyboardKeys.keyDown(key1)
        KeyboardKeys.keyDown(key2)
        KeyboardKeys.keyUp(key2)
        KeyboardKeys.keyUp(key1)




if __name__ == "__main__":
    test = KeyboardKeys()
    KeyboardKeys.oneKey('backspace')
    test.setText(u'my name is tyw')
    print(test.getText().decode('gbk').encode('utf-8'))