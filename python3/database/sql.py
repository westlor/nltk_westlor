#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Created on 2016年4月21日

@author: Westlor
'''
import sqlite3

class Sql(object):
    
    def __init__(self, db):
        self.db = db
        self.conn = None
        
    # 打开数据库文件，文件名在类构造方法中指定
    def open(self):
        self.conn = sqlite3.connect(self.db);
        #print("Opened database successfully");
    # 关闭数据库文件
    def close(self):
        self.conn.close();
        #print("Closed database successfully");
    
    # 创建一个表格table，列名name[], 列类型types[]
    def creat(self, table, name, types):
        self.open()
        n = len(name);
        sql = "CREATE TABLE " + table + "(ID INT PRIMARY KEY NOT NULL"
        i = 0;
        while i<n:
                sql += (',' + name[i] + ' ' + types[i])
                i += 1
        sql += ");"
        print(sql);
        try:
            self.conn.execute(sql);
            print("Table created successfully");
        except sqlite3.OperationalError as e:
            print('except:', e)
        finally:
            pass
        self.close()
        
    # 向表格中添加一列
    def addcol(self, table, name, type):
        self.open()
        sql = "ALTER TABLE " + table + " ADD COLUMN " + name + ' ' + type
        print(sql);
        self.conn.execute(sql);
        self.conn.commit();
        print("Table add column successfully");
        self.close()
        
    # 获取表格中存在的列名称
    def colinfo(self, table):
        self.open()
        sql = "PRAGMA table_info(" + table + ")"
        print(sql)
        cursor = self.conn.execute(sql);
        self.close()
        print("select column info successfully")
        return cursor
        
    # 向表格中插入一条数据，不用写PRIMARY KEY
    def insert(self, table, values):
        self.open()
        n = len(values);
        sql = "insert into " + table + " values(null"
        i = 0
        while i<n:
                i += 1
                sql += (',' + values)
        print(sql);
        self.conn.execute(sql);
        self.conn.commit();
        print("insert values successfully");
        self.close();

    # 查询表格中name列中一条值为value的记录
    def select(self, table, name, value):
        self.open()
        sql = "select * from " + table + " where " + name + "=" + value
        print(sql);
        cursor = self.conn.execute(sql);
        print("select successfully");
        self.close()
        return cursor
    
    # 更新表格中rname列中值为rvalue的一条记录中uname列的值为uvalue
    def update(self, table, rname, rvalue, uname, uvalue):
        self.open()
        sql = "UPDATE " + table + " set " + uname + " = " + uvalue \
                          + " where " + rname + "=" + rvalue
        print(sql);
        self.conn.execute(sql);
        self.conn.commit();
        print("update successfully");
        self.close()

    # 删除表格中dname列中值为dvalue的一条记录
    def delete(self, table, dname, dvalue):
        self.open()
        sql = "DELETE from " + table + " where " + dname + "=" + dvalue
        print(sql);
        self.conn.execute(sql);
        self.conn.commit();
        print("Total number of rows deleted :" + self.conn.total_changes());
        self.close()

