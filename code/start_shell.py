#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Created on 2016年 4月14日
@author: Westlor
'''
import part_of_speech
import content_functional
import phrase
# switch={
#     '0': read_shell.read,
#     '1': ask_shell.read,
# };
#mod = input("Please select mod: 0-read_shell, 1-ask_shell, 2-speak_shell...):~$ ");
#switch.get(mod)(raw)

# 程序起点
while 1:
    raw = input("ws@nltk:~$ ");
    
    if raw == "quit":
        print("Over...")
        quit() 
    elif raw == '':
        pass
    else:
        # 分词，词性提取
        sentence = part_of_speech.word_segmentation(raw)
        # 短语分析，分块
        phrase.divide(sentence)
        # 实词、虚词划分
        content_functional.classification(sentence)
        #part_of_speech.chunking(sentence)
        # 句子成分解析
        