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

class ProcWord(object):
    
    def __init__(self):
        pass
    
    def proc_w0(self, words, flags):
    
        pass

    def proc_w1(self, words, flags):
        
        pass
    
    def proc_w2(self, words, flags):
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
    
    def proc_w3(self, words, flags):
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
            elif re.match(r'n+', flags[1]):     # n-n-* 的结构，i:关系
                if flags[2] == 'i':
                    sql = dbs.Sql("../data/"+"n_relation.db")
                    sql.addelem("n_relation", "name", words[0], 'name_s', words[1])
                    sql.addelem("n_relation", "name", words[0], 'relation', words[2])
                    sql.addelem("n_relation_s", "name", words[1], 'name_s', words[0])
                    sql.addelem("n_relation_s", "name", words[1], 'relation', words[2])
                    
        elif re.match(r'n+', flags[1]):         # 第二个词是名词
            self.proc_w2(words[0:2], flags[0:2])
            self.proc_w2(words[1:3], flags[1:3])
        elif re.match(r'n+', flags[2]):         # 第三个词是名词
            pass
        
    def proc_w4(self, words, flags):
        if re.match(r'n+', flags[0]):           # 第一个词是名词
            if flags[1] == 'd':                 # 第二个词是副词 n-d-* 单句分析，去掉副词
                words.remove(words[1])
                flags.remove(flags[1])
                self.proc_w3(words, flags)
            elif re.match(r'n+', flags[1]):     # 第二个词也是名词
                if flags[2] == 'd':             # 第三个词是副词
                    if flags[3] == 'a':         # n-n-d-a（副词+形容词） 表示状态a
                        tmpw = [words[0], words[2]+words[3]]
                        tmpf = [flags[0], 'a']
                        self.proc_w2(tmpw, tmpf)
                        tmpw = [words[1], words[2]+words[3]]
                        tmpf = [flags[1], 'a']
                        self.proc_w2(tmpw, tmpf)
                    elif flags[3] == 'v':       # n-n-d-v (副词+动词) 表示关系i
                        tmpw = [words[0], words[1], words[2]+words[3]]
                        tmpf = [flags[0], flags[2], 'i']
                        self.proc_w3(tmpw, tmpf)
                   
    def proc_wn(self, words, flags):
        length = len(words)
        if length <= 4:
            if length == 0:
                self.proc_w0(words, flags)
            elif length == 1:
                self.proc_w1(words, flags)
            elif length == 2:
                self.proc_w2(words, flags)
            elif length == 3:
                self.proc_w3(words, flags)
            elif length == 4:
                self.proc_w4(words, flags)
        else:
            # dosomething here...
            pass
    
    def proc_words(self, words, flags):
        
        self.proc_wn(words, flags)
    
    # 去除句子中的副词
    def rm_adverb(self, words, flags):
        for w,f in zip(words,flags):
            if f == 'd':
                words.remove(w)
                flags.remove(f)

def proc(words, flags):
    
    pw = ProcWord()
    pw.proc_words(words, flags)
    

if __name__ == '__main__':
    
    if True:
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
    
        table = "n_relation"
        sql = dbs.Sql("../data/" + table + ".db")  
        print(sql.probetable(table))
        print(sql.colinfo(table))
        print(sql.tabledata(table))
        table = "n_relation_s"
        print(sql.probetable(table))
        print(sql.colinfo(table))
        print(sql.tabledata(table))
        pass