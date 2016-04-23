#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年4月21日

@author: Westlor
'''
import sqlite3
from _overlapped import NULL

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
        sql = "CREATE TABLE " + table + "(ID INTEGER PRIMARY KEY AUTOINCREMENT"
        i = 0;
        while i<n:
                sql += (',' + name[i] + ' ' + types[i])
                i += 1
        sql += ");"
        print("SQL: " + sql);
        try:
            self.conn.execute(sql);
            #print("Table created successfully");
        except sqlite3.OperationalError as e:
            print('except:', e)
        finally:
            pass
        self.close()
        
    # 探测数据库中某个表格是否存在
    def probetable(self, table):
        self.open()
        sql = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='" \
                + table + "'"
        print("SQL: " + sql + " # 探测表格是否存在");
        cursor = self.conn.execute(sql);
        info = cursor.fetchall()
        self.close()
        if info[0][0]:
            return True
        return False
        
    # 向表格中添加一列
    def addcol(self, table, name, tp):
        self.open()
        sql = "ALTER TABLE " + table + " ADD COLUMN " + name + ' ' + tp
        print("SQL: " + sql);
        self.conn.execute(sql);
        self.conn.commit();
        #print("Table add column successfully");
        self.close()
        
    # 获取表格中存在的列名称
    def colinfo(self, table):
        self.open()
        sql = "PRAGMA table_info(" + table + ")"
        print("SQL: " + sql + " # 打印表格列信息")
        cursor = self.conn.execute(sql);
        info = cursor.fetchall()
        self.close()
        #print("select column info successfully")
        return info
    
    # 获取表格中所有数据
    def tabledata(self, table):
        self.open()
        sql = "select * from " + table + ';'
        print("SQL: " + sql + " # 打印表格数据")
        cursor = self.conn.execute(sql);
        info = cursor.fetchall()
        self.close()
        #print("select column info successfully")
        return info
        
    
    # 查询表格中有没有对应的列
    def findcol(self, table, col):
        cinfo = self.colinfo(table)
        for row in cinfo:
            if col in row:
                if col == row[1]:
                    return True
        return False
    
    # 查询表格中有没有对应的行
    def findrow(self, table, name, value):
        data = self.select(table, name, value)
        if len(data) > 0:
            return True
        else:
            return False
        
    # 查询表格中有没有对应的元素
    def findelem(self, table, src_name, src_value, des_name):
        self.open()
        src_value = "'"+src_value+"'"
        
        sql = "select " + des_name + " from " + table + " where " + src_name + "=" + src_value
        
        print("SQL: " + sql + " # 查找对应列是否存在");
        try:
            cursor = self.conn.execute(sql);
            data = cursor.fetchall()
        except sqlite3.OperationalError as e:
            print('except:', e)
            data = NULL
        finally:
            pass
        
        self.close()
        if data == NULL:
            return NULL
        elif len(data) == 0:
            return NULL
        else:
            return data[0][0]
        
    def addelem(self, table,  src_name, src_value, des_name, des_value):
        # 1.判断表格是否存在
        if self.probetable(table):          # 表格存在
            # 判断列是否存在
            if self.findcol(table, des_name):  # des_name列存在
                data = self.findelem(table, src_name, src_value, des_name)
                if data is NULL:            # 这个元素为空
                    if self.findrow(table, src_name, src_value):    #存在对应的行
                        self.update(table, src_name, src_value, des_name, des_value)
                    else:   #不存在对应的行
                        self.insert(table, (src_name, des_name), (src_value, des_value))
                elif des_value in data:     # 这个元素包含需要插入的元素
                    return 
                else:                       # 这个元素不包含需要插入的元素
                    data = data + " " + des_value
                    self.update(table, src_name, src_value, des_name, data)
            else:                           # des_name列不存在，需要先添加该列
                if type(des_value) is int:
                    self.addcol(table, des_name, "INTEGER")
                else:
                    self.addcol(table, des_name, "TEXT")
                self.update(table, src_name, src_value, des_name, des_value)
            pass
        else:   #表格不存在，先创建该表格
            rtype = "NCHAR(20)"     # src_type 一般为name列
            dtype = NULL
            if type(des_value) is int:
                dtype = "INTEGER"
            else:
                dtype = "TEXT"
            
            self.creat(table, (src_name, des_name), (rtype, dtype))
            self.insert(table, (src_name, des_name), (src_value, des_value))
            pass
        
    # 向表格中插入一条数据，不用写PRIMARY KEY
    def insert(self, table, names, values):
        self.open()
        n = len(names);
        sql = "insert into " + table + "("
        i=0
        while i<n:
            sql += names[i]
            if(i < n-1):
                sql += ','
            i += 1
        sql += ") values("
        i = 0
        while i<n:
            sql += ("'" + values[i] + "'")
            if(i < n-1):
                sql += ','
            i += 1
        sql +=');'
        print("SQL: " + sql);
        self.conn.execute(sql);
        self.conn.commit();
        #print("insert values successfully");
        self.close();

    # 查询表格中name列中一条值为value的记录
    def select(self, table, name, value):
        self.open()
        sql = "select * from " + table + " where " + name + "='" + value + "'"
        print("SQL: " + sql);
        cursor = self.conn.execute(sql);
        data = cursor.fetchall()
        #print("select successfully");
        self.close()
        return data
    
    # 更新表格中src_name列中值为src_value的一条记录中uname列的值为uvalue
    def update(self, table, src_name, src_value, uname, uvalue):
        self.open()
        sql = "UPDATE " + table + " set " + uname + "='" + uvalue + "'" \
                      + " where " + src_name + "='" + src_value + "'"
        
        print("SQL: " + sql);
        self.conn.execute(sql);
        self.conn.commit();
        #print("update successfully");
        self.close()

    # 删除表格中dname列中值为dvalue的一条记录
    def delete(self, table, dname, dvalue):
        self.open()
        sql = "DELETE from " + table + " where " + dname + "='" + dvalue + "'"
        print("SQL: " + sql);
        self.conn.execute(sql);
        self.conn.commit();
        #print("Total number of rows deleted :" + self.conn.total_changes());
        self.close()

