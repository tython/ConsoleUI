#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 23:37
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : xml_util.py
# @Software: PyCharm

from xml.etree import ElementTree
from xml.dom import minidom
from conf.settings import BASE_PATH

class ParseXMLByElementTree(object):
    """采用ElementTree方式解析XML"""
    def __init__(self,xmlPath):
        self.xmlPath = xmlPath

    def getRoot(self):
        # 打开要解析的xml
        tree = ElementTree.parse(self.xmlPath)
        print("根节点：",tree.getroot())
        return tree.getroot()

    def findNodeByName(self,parentNode,nodeName):
        # 通过节点的名字获取对象
        nodes = parentNode.findall(nodeName)
        print("node:",nodes)
        return nodes

    def getNodeOfChildText(self,node):
        # 获取节点node下所有子节点的节点名作为Key,本节点名作为Value组成的字典对象
        childrenTextDict = {i.tag: i.text for i in list(node.iter())[1:]}
        return childrenTextDict

    def getDataFromXml(self):
        # 获取xml文档树的根节点对象
        root = self.getRoot()
        # 获取根节点下所有名叫book的节点对象
        books = self.findNodeByName(root,"book")
        dataList = []
        # 遍历获取到的所有book节点对象，取得需要的测试数据
        for book in books:
            childrenText = self.getNodeOfChildText(book)
            dataList.append(childrenText)
        return dataList


class ParseXMLByDom(object):
    """采用DOM方式解析XML"""
    def __init__(self, xmlPath):
        self.xmlPath = xmlPath

    def getdom(self):
        # 打开要解析的xml
        dom = minidom.parse(self.xmlPath)
        return dom

    def getXmlObj(self):
        # 得到文档元素对象
        root = self.getdom().documentElement
        return root

    def getLabelName(self,TagName):
        # 获取标签名
        tagname =  self.getXmlObj().getElementsByTagName(TagName) # 通过下标取tagName的值
        print(f"标签{TagName}共计",len(tagname),'个')
        # for i in tagname:
        #     print(i.tagName)
        return tagname

    def getAttribute(self,labelName,attribute,N = 1):
        # 获取标签的属性值
        # 1.先获取要取值的标签，再获取标签里要查询的属性值名称
        label = self.getXmlObj().getElementsByTagName(labelName)
        print(f"标签{labelName}共计",len(label),'个')
        att = label[N-1].getAttribute(attribute) # 默认取下标为0的标签值
        print(att)
        return att

    def getDataBetweenTags(self,LabelName,N = 1):
        # 获取标签之间的数据
        label = self.getXmlObj().getElementsByTagName(LabelName)
        value = label[N-1].firstChild.data
        print(value)
        return value




if __name__ == "__main__":
    pass

