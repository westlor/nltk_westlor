#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年 4月20日
@author: Westlor
'''
import read_shell_nr as rs_nr
import jieba.posseg as pseg
import re

def nothing(w, f):
    pass

process={
    'nr': rs_nr.proc,
    'rs': rs_nr.proc,
    None: nothing,
};

# 查找arr元组中item项的索引
def find_all_index(arr,item): 
    return [i for i,a in enumerate(arr) if a==item] 

# 句子预处理，更改分词的词性
def pro_start(words, flags):
    index = find_all_index(flags, 'eng')
    
    if len(index) > 0:
        if index[0] == 0:
            index.remove(0)
        for i in index:
            print(i)
            if words[i] == 'n':
                words.remove(words[i])
                flags.remove(flags[i])
                flags[i-1] = 'n'
            elif words[i] == 'a':
                words.remove(words[i])
                flags.remove(flags[i])
                flags[i-1] = 'a'

# 查找句子的
def find_key(words, flags):
    
    pro_start(words, flags)
    print(words)
    print(flags)
    
    for arg in flags:
        if re.match(r'n+', arg) or re.match(r'r+', arg):           # 名词开头
            return 'nr'
        else:
            return None

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
    #process.get(s)(raw_words, raw_flags)

if __name__ == '__main__':

    while 0:
        raw = input("ws@nltk:~$ ");
        
        if raw == "quit":
            print("Over...")
            quit() 
        elif raw == '':
            pass
        else:
            read(raw)
            pass