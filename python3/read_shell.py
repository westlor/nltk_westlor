#!/usr/bin/python3
'''
Created on 2016��4��20��

@author: Westlor
'''
def read():
    words = pseg.cut(raw)
    for w in words:
        print("%s -> %s" % (w.word, w.flag))
    pass