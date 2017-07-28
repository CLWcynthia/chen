#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  @Time          : 2017/7/26 17:07
  @Author       : Chen
  @Introduction: ${ Describes the function of this script}
"""

from pymongo import MongoClient as mc


def connect():
    """
    :return: 
    """
    client = mc('192.168.10.5', 27017)
    db = client['test']  # test代表数据库名称
    collection = db['col']  # col代表集合名称

    for data in db.col.find():
        # 从集合中取数据
        print(data)
    client.close()  # 关闭连接

connect()
