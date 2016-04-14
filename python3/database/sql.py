#!/usr/bin/python3
'''
Created on 2016Äê4ÔÂ14ÈÕ

@author: Westlor
'''
import sqlite3

CONN = None

def open(db):
        global CONN
        CONN = sqlite3.connect(db);
        print("Opened database successfully");

def execSql(sql):
        return CONN.execute(sql);

def creat(table, name, types):
        n = len(name);
        sql = "CREATE TABLE " + table + "(ID INT PRIMARY KEY NOT NULL,"
        i = 0;
        while i<n:
                i += 1
                sql += (name[i] + ' ' + types[i] + ',')
        sql += ");"
        print(sql);
        execSql(sql);
        print("Table created successfully");

def insert(table, values):
        n = len(values);
        sql = "insert into " + table + " values(null,"
        i = 0
        while i<n:
                i += 1
                sql += (values + ',')
        print(sql);
        execSql(sql);
        CONN.commit();
        print("insert values successfully");

def select(table, name, value):
        sql = "select * from " + table + " where " + name + "=" + value
        print(sql);
        cursor = execSql(sql);
        print("select successfully");
        return cursor

def update(table, rname, rvalue, uname, uvalue):
        sql = "UPDATE " + table + " set " + uname + " = " + uvalue \
                          + " where " + rname + "=" + rvalue
        print(sql);
        execSql(sql);
        CONN.commit();
        print("update successfully");

def delete(table, dname, dvalue):
        sql = "DELETE from " + table + " where " + dname + "=" + dvalue
        print(sql);
        execSql(sql);
        CONN.commit();
        print("Total number of rows deleted :" + CONN.total_changes());

def close(db):
        CONN.close();
        print("Closed database successfully");
