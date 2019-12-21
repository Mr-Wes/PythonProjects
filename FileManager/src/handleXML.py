import os
import xml.etree.cElementTree as ET


"""
获取根结点
"""

def getRoot(xmlpath):
    tree = ET.parse(xmlpath)
    root = tree.getroot()

"""
将仓库名：文件夹路径写入到 my.xml中
"""

def writeRep(dirname, dirpath):
    pass

"""
获取仓库名列表
"""

def getRepsName():
    root = getRoot('../record/my.xml')

def createXML(filename, rootname):
    fd = open('../record/'+filename+'.xml', mode='w', encoding='utf-8')
    msg = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n<"+rootname+">\n</"+rootname+">\n"
    fd.write(msg)
    fd.close()
