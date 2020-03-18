import configparser
import os

#获取相对路径下的配置文件#
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)
path=parent_path+'\config.ini'

cf=configparser.ConfigParser()
cf.read(path)
# 获取所有section，返回值为list
secs = cf.sections()
print(parent_path)


class readConfig:
    # 获取全部#
    def getItem(name):
        value=cf.items(name)
        return value

    #输入模块名和选项名获取对应的值#
    def getValue(modelName,itemName):
        value=cf.get(modelName,itemName)
        return value








