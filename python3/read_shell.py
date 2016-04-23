#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年 4月20日
@author: Westlor
'''
import read_shell_ns as rs_ns
import jieba.posseg as pseg
import re

def nothing(w, f):
    pass

process={
    'ns': rs_ns.proc,
    'rs': rs_ns.proc,
    None: nothing,
};

def find_start(words, flags):
    if re.match(r'n+', flags[0]):           # 名词开头
        return 'ns'
    elif flags[1]=='eng' and words[1]=='n': # 标记为名词
        words.remove(words[1])
        flags.remove(flags[1])
        return 'ns'
    else:
        return None

def read(raw):
    raw_words = []
    raw_flags = []
    
    print("raw:"+raw)
    words = pseg.cut(raw)

    for w in words:
        #print("%s -> %s" % (w.word, w.flag))
        raw_words.append(w.word)
        raw_flags.append(w.flag)
        
    print(raw_words)
    print(raw_flags)
    
    s = find_start(raw_words, raw_flags)
    process.get(s)(raw_words, raw_flags)

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