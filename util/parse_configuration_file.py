#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 23:37
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : parse_configuration_file.py
# @Software: PyCharm

# 对.ini配置文件的查询，添加，修改，删除，保存

from configparser import ConfigParser

class ParseConfigFile():

    def __init__(self,configFilePath=None):
        self.cf = ConfigParser()
        try:
            if configFilePath is None:
                raise FileNotFoundError("Can't found config file!")
            else:
                self.configFilePath = configFilePath
                self.cf.read(self.configFilePath,encoding="utf-8")
        except Exception as e:
            raise e

    def getItemSection(self,sectionName):
        """
        获取配置文件中指定section下所有的option键值对,并以字典类型返回给调用者
        注意：
        使用self.cf.items(sectionNmae)此种方法获取到的配置文件中的option内容均被转换成小写
        如loginPage.username被转换成loginpage.username
        :param sectionName:
        :return:
        """
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionsBySection(self,sectionName):
        """
        获取指定sectionName下的所有option
        :param sectionName:
        :return: List Type
        """
        value = self.cf.options(sectionName)
        return value

    def getOptionValue(self,sectionName,optionName):
        """
        获取指定section下指定的option值
        :param sectionName:
        :param optionName:
        :return:string 类型
        """
        value = self.cf.get(sectionName,optionName)
        return value

    def getOptionValueInt(self,sectionName,optionName):
        """
        获取指定section下指定的option的值
        :param sectionName:
        :param optionName:
        :return:Int 类型
        """
        value = self.cf.getint(sectionName,optionName)
        return value

    def getSection(self):
        """
        获取所有的section
        :return: List
        """
        return self.cf.sections()

    def dump(self):
        """
        打印配置文件中的所有内容
        :return:
        """
        sectionsList = self.cf.sections()
        print("="*50)
        for i in sectionsList:
            print(i)
            print(self.cf.items(i))
        print("="*50)

    def remove_section(self,section):
        """
        删除section
        :param section:
        :param key:
        :return:
        """
        self.cf.remove_section(section)


    def remove_option(self,section,key):
        """
        删除option
        :param section:
        :param key:
        :return:
        """
        self.cf.remove_option(section,key)

    def add_section(self,section):
        """
        添加section
        :param section:
        :return:
        """
        self.cf.add_section(section)

    def set_item(self,section,key,value):
        """
        给指定的Section设置key,value
        :param section:
        :param key:
        :param value:
        :return:
        """
        self.cf.set(section,key,value)

    def save(self):
        """
        保存配置文件
        :return:
        """
        fp = open(self.configFilePath,'w') # with open(self.configFilePath,"w+") as f:self.cf.write(f)
        self.cf.write(fp)
        fp.close()

