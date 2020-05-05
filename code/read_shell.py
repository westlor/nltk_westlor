#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年 4月20日
@author: Westlor
'''
import read_shell_nr as rs_nr
import jieba.posseg as pseg
import re
import constant
import constituent
from warnings import catch_warnings

def nothing(w, f):
    pass

process={
    'nr': rs_nr.proc,
    'rs': rs_nr.proc,
    None: nothing,
};

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
    raw_flags_zh = []
    
    print("raw:"+raw)
    words = pseg.cut(raw)

    for w in words:
        raw_words.append(w.word)
        raw_flags.append(w.flag)
        try:
            raw_flags_zh.append(constant.ParticipleName[w.flag])
        except KeyError:
            raw_flags_zh.append("未知词")
    
    # 语法分析
    constituent.analysis(raw_words, raw_flags, raw_flags_zh)
    
    #s = find_key(raw_words, raw_flags)
    #process.get(s)(raw_words, raw_flags)