#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年4月21日

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
    while prop==NULL or prop=='':
        prop = input(words[0] + "的什么" + words[1] + words[2] + "?:~$ ")
    sql = dbs.Sql("rs_ns.db")
    sql.addelem("rs_ns", "name", words[0], prop, words[2])

switch={
    0: proc_w0,
    1: proc_w1,
    2: proc_w2,
    3: proc_w3,
};
def proc(words, flags):
    switch.get(len(words))(words, flags)
    pass

if __name__ == '__main__':
    
    table = "rs_ns"
    sql = dbs.Sql(table + ".db")
    
    print(sql.probetable(table))
    print(sql.colinfo(table))
    print(sql.tabledata(table))  
    pass