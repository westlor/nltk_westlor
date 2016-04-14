#!/usr/bin/python3
'''
Created on 2016年 4月14日
@author: Westlor
'''
import jieba.posseg as pseg

while 1:
    print("...>>>");
    raw = input();
    words = pseg.cut(raw)
    for w in words:
        print("%s -> %s" % (w.word, w.flag))
    if w.word == "quit":
        print("Over...")
        quit() 