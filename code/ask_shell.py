#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Created on 2016年4月20日
@author: Westlor
'''
import jieba.posseg as pseg

def read(raw):
    words = pseg.cut(raw)
    for w in words:
        print("%s -> %s" % (w.word, w.flag))
    pass