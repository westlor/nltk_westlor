#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年4月21日
@intent: 解析含有名词或者代词的句子
@author: Westlor
'''
import database.sql as dbs
from _overlapped import NULL

def proc_w0(words, flags):
    
    pass

def proc_w1(words, flags):
    
    pass

def proc_w2(words, flags):
    
    pass

def proc_w3(words, flags):
    prop = NULL
    if flags[1] == 'p':     # 介词  n1-p-n2 的结构，n2是n1的属性
        while prop==NULL or prop=='':
            prop = input(words[0] + "的什么" + words[1] + words[2] + "?:~$ ")
        sql = dbs.Sql("n_property.db")
        sql.addelem("../data/"+"n_property", "name", words[0], prop, words[2])
    elif flags[1] == 'v':   # 动词 n1-v-n2 的结构，v是n1的方法，n2是？
        sql = dbs.Sql("n_method.db")
        sql.addelem("../data/"+"n_method", "name", words[0], words[1], words[2])
        
process={
    0: proc_w0,
    1: proc_w1,
    2: proc_w2,
    3: proc_w3,
    4: proc_w0,
    5: proc_w0,
    6: proc_w0,
    7: proc_w0,
};
def proc(words, flags):
    process.get(len(words))(words, flags)
    pass

if __name__ == '__main__':
    
    table = "n_method"
    sql = dbs.Sql("../data/" + table + ".db")
    
    print(sql.probetable(table))
    print(sql.colinfo(table))
    print(sql.tabledata(table))
    pass