#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年4月21日
@intent: 解析含有名词或者代词的句子
@author: Westlor
'''
import database.sql as dbs
import re
from _overlapped import NULL

def proc_w0(words, flags):
    
    pass

def proc_w1(words, flags):
    
    pass

def proc_w2(words, flags):
    prop = NULL
    if re.match(r'n+', flags[0]):           # 第一个词是名词
        while prop==NULL or prop=='':
                prop = input(words[1] + "是指什么?:~$ ")
        status = prop
        prop = NULL
        while prop==NULL or prop=='':
                prop = input(words[0] + "的什么" + "是" + status + "?:~$ ")
        sql = dbs.Sql("../data/"+"n_property.db")
        sql.addelem("n_property", "name", words[0], prop, status)
    elif re.match(r'n+', flags[1]):         # 第二个词是名词
        while prop==NULL or prop=='':
                prop = input(words[1] + "的什么" + "在" + words[0] + "?:~$ ")
        sql = dbs.Sql("../data/"+"n_property.db")
        sql.addelem("n_property", "name", words[1], prop, words[0])
    pass

def proc_w3(words, flags):
    prop = NULL
    if re.match(r'n+', flags[0]):           # 第一个词是名词
        if flags[1] == 'p':     # 介词  n1-p-n2 的结构，n2是n1的属性
            while prop==NULL or prop=='':
                prop = input(words[0] + "的什么" + words[1] + words[2] + "?:~$ ")
            sql = dbs.Sql("../data/"+"n_property.db")
            sql.addelem("n_property", "name", words[0], prop, words[2])
        elif flags[1] == 'v':   # 动词 n1-v-n2 的结构，v是n1的方法，n2是？
            sql = dbs.Sql("../data/"+"n_method.db")
            sql.addelem("n_method", "name", words[0], words[1], words[2])
    elif re.match(r'n+', flags[1]):         # 第二个词是名词
        proc_w2(words[0:2], flags[0:2])
        proc_w2(words[1:3], flags[1:3])
    elif re.match(r'n+', flags[2]):         # 第三个词是名词
        pass

def proc_wn(words, flags):
    pass
       
process={
    '0': proc_w0,
    '1': proc_w1,
    '2': proc_w2,
    '3': proc_w3,
    'n': proc_wn,
};
def proc(words, flags):
    length = len(words)
    if length <= 3:
        process.get(str(length))(words, flags)
    else:
        process.get('n')(words, flags)
    pass

if __name__ == '__main__':
    
    #if re.match("*hehe*", "hehfdsfsdhehelkjkfjdslkj hehe "):
    #    print("I get")
    
    if False:
        table = "n_property"
        sql = dbs.Sql("../data/" + table + ".db")  
        print(sql.probetable(table))
        print(sql.colinfo(table))
        print(sql.tabledata(table))
        
        table = "n_method"
        sql = dbs.Sql("../data/" + table + ".db")  
        print(sql.probetable(table))
        print(sql.colinfo(table))
        print(sql.tabledata(table))
        pass