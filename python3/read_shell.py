#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Created on 2016年 4月20日
@author: Westlor
'''
import read_shell_ns as rsns
import jieba.posseg as pseg
import re

def read(raw):
    raw_words = []
    raw_flags = []
    
    print("raw:"+raw)
    words = pseg.cut(raw)
    #print(words.__next__().encode('utf-8').decode('utf-8'))
    #print(words.__next__().encode('utf-8').decode('utf-8'))
    #print(words.__next__().encode('utf-8').decode('utf-8'))
    
    #if re.match(r'n*', words.__next__().encode('utf-8'), 0):
    #    print(words.__next__().encode('utf-8'))

    for w in words:
        #print("%s -> %s" % (w.word, w.flag))
        raw_words.append(w.word)
        raw_flags.append(w.flag)
        
    print(raw_words)
    print(raw_flags)
    
    if re.match(r'n+', raw_flags[0]):
        print('n is master..'+raw_flags[0])
        rsns.proc(raw_words, raw_flags)
        pass