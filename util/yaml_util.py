#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 22:59
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : yaml_util.py
# @Software: PyCharm

import yaml


class GetYaml:
    """
    读取yaml
    若yaml文件中存在重复的key, 读取时则会读取最新写入的
    """
    def __init__(self,path,key=None,dict_info=None):
        self.path = path
        self.key = key
        self.dict_info = dict_info

    def get_data(self):
        """获取yaml中的数据,且只获取最外层的key"""
        with open(self.path,'rb') as y:
            cont = y.read()    # 获取yaml文件中的所有信息
        yaml.warnings({'YAMLLoadWarning':False})
        cf = yaml.load(cont)        # 将bytes转为dict
        y.close()              # 关闭文件
        if self.key == None:
            return cf       # 返回所有数据
        else:
            return cf.get(self.key) #获取键为param的值

    def echo_data(self):
        """python对象转化yaml文档"""
        with open(self.path, "a+", encoding="utf-8") as f:# 注：此模式为追加模式,若想直接重写则将open函数中的模式'a+'改为'w'
            yaml.dump(self.dict_info, f)
        f.close()

if __name__ == '__main__':
    y = GetYaml('./test.yaml')
    print(y.get_data())

