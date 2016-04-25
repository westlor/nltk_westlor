#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年 4月20日
@author: Westlor
'''
import jieba.posseg as pseg
import re

# 句子预处理，更改分词的词性
def pro_start(words, flags):
    for i,a in enumerate(flags):
        if i > 0:
            if words[i] == 'n':         # n-名词    a-形容词
                flags[i-1] = 'n'
            elif words[i] == 'a':
                flags[i-1] = 'a'
    for w,f in zip(words,flags):
        if w == 'n' or w == 'a':
            words.remove(w)
            flags.remove(f)

# 查找句子的
def find_key(words, flags):
    
    pro_start(words, flags)
    print(words)
    print(flags)
    
    sign = None
    for arg in flags:
        if re.match(r'n+', arg) or re.match(r'r+', arg):
            sign = 'nr'
    return sign

def read(raw):
    raw_words = []
    raw_flags = []
    
    print("raw:"+raw)
    words = pseg.cut(raw)

    for w in words:
        raw_words.append(w.word)
        raw_flags.append(w.flag)
        
    print(raw_words)
    print(raw_flags)
    
    s = find_key(raw_words, raw_flags)

if __name__ == '__main__':

    while 1:
        raw = input("ws@nltk:~$ ");
        
        if raw == "quit":
            print("Over...")
            quit() 
        elif raw == '':
            pass
        else:
            read(raw)
            pass