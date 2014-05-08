# -*- coding: utf-8 -*-
'''
Created on 2014-5-5

@author: zqtang
'''
import pymongo


__conndb = None

def __init__(self):
    __conndb = self.application.db.mytestdb

def getAllData():
    return __conndb.find();