# -*- coding: utf-8 -*-
import sqlite3
import json
import datetime
import time
from datetime import timedelta
import chardet


import csv, codecs
from io import StringIO
from distutils.msvc9compiler import query_vcvarsall

Params_carDasProductRelease=""

dbsFile = "D:/mysqlite.db"
csvFile = "D:/Jexport_data.csv"

def carDasProductReleaseBizParams():
    global Params_carDasProductRelease
    currDate = datetime.datetime.now()
    carriageDate = currDate + timedelta(days=1)
    underdate = carriageDate
    valueDate = carriageDate + timedelta(days=1)
    dueDate = valueDate + timedelta(days=365)
    minPreDueDate = dueDate - timedelta(days=29)
    #获取当前时间戳的后四位作为产品号码
    data = int(time.time())
    data1 = data // 1000
    data2 = str(data - data1 * 1000)

    bizParams = {}

    bizParams["financingNo"] = "DSC-" + carriageDate.strftime("%Y%m%d")+"-"+data2
    bizParams["productName"] = "弹个车资产权益转让产品" + carriageDate.strftime("%Y%m%d") + data2 +"号"
    bizParams["requestAmount"] = "73132"
    bizParams["carriageDate"] = carriageDate.strftime("%Y%m%d")
    bizParams["underDate"] = underdate.strftime("%Y%m%d")
    bizParams["valueDate"] = valueDate.strftime("%Y%m%d")
    bizParams["term"] = "365"
    bizParams["minPreDueDate"] = minPreDueDate.strftime("%Y%m%d")
    bizParams["dueDate"] = dueDate.strftime("%Y%m%d")
    bizParams["profitYearRate"] = "0.09"
    bizParams["bizType"] = "TGC"  # TGC-弹个车   TGC_SECOND_HAND-弹个车二手车
    bizParams["assetNum"] = "1"  # 非必填  大搜车不推默认为0
    # bizParams["issuePeriods"] = "36"#大搜车默认赋值

    # print ("Params-carDasProductRelease: \n"  + json.dumps(bizParams) +  "\n")
    Params_carDasProductRelease = json.dumps(bizParams)
    #print(bizParams)
    print(Params_carDasProductRelease)


carDasProductReleaseBizParams()

#创建一个连接对象，连接到本地数据库
conn=sqlite3.connect(dbsFile)
#创建一个游标对象，调用其execute（）方法来执行SQL语句
c=conn.cursor()

#print(Params_carDasProductRelease)
s = Params_carDasProductRelease.replace('"term": "365"','"term": "364"')

#print (s)
#向表中插入一条数据
sql_one="update kftestcase set bizParamsJson = '"+Params_carDasProductRelease+"' where service = 'carDasProductRelease' and caseNo='1.1'"
'''
#向表中插入多条数据
sql_many="INSERT INTO COMPANY VALUES(?,?,?,?,?)"
#声明要插入的数据
datas=[(1,'灭霸1号',999,'阿斯加德',88888),
        (2,'灭霸2号',888,'哈瓦洛',66666),
        (3,'灭霸3号',666,'瓦斯诺',77777),
        (4,'灭霸4号',555,'贾满德',66666),
        (5,'灭霸5号',777,'地球',999999),
    ]
#插入多条数据
c.executemany(sql_many,datas)
'''
#执行插入SQL指令
try:
    c.execute(sql_one)
    conn.commit()
except Exception as e:
    print (e)
    conn.rollback()

sql_two = "update kftestcase set bizParamsJson = '"+s+"' where service = 'carDasProductRelease' and caseNo='1.3'"
try:
    c.execute(sql_two)
    conn.commit()
except Exception as e:
    print (e)
    conn.rollback()

#查询
# sql_id="SELECT * FROM kftestcase"
#
# for row in c.execute(sql_id):
#     print(row)

conn.close()

def procBOM(strPath, bAdd):
    newcontent = '';
    f = open(strPath, "rb");
    fcontent = f.read();
    f.close();
    codeType = chardet.detect(fcontent)
    print(codeType)
    codeType = codeType["encoding"]  #检测编码方式  
    printBuffer = "procBOM:" + "  "+str(codeType) 
    
    print(codeType)
    if codeType.lower().find('utf-8') == -1 and codeType.lower().find('ascii') == -1 :
        #非utf8文件保险起见先退出,并输出错误提示,todo后续再添加其它转码到utf8
        print(printBuffer + " error OK")
        return
    #不需要转换，已经添加bom头    
    if bAdd and fcontent[:3] != codecs.BOM_UTF8:
        print(  printBuffer+" add bom")
        newcontent = codecs.BOM_UTF8;
        newcontent += fcontent;
    elif not bAdd and fcontent[:3] == codecs.BOM_UTF8:
        newcontent = fcontent[3:];
        print(printBuffer+" del bom")
    else:
        return;
    fnew = open(strPath, "wb+")
    fnew.write(newcontent);
    fnew.close();
    print("done")
    return

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        # Redirect output to a queue
        self.queue = StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow(row)
        data = self.queue.getvalue()
        self.stream.write(data)
        #empty queue
        self.queue.truncate(0)
    def writerows(self, rows):
        for row in rows:
            print(row)
            self.writerow(row)
    def close(self):
        self.stream.close()
        
        
conn = sqlite3.connect(dbsFile)
f=open(csvFile, "w", encoding='utf_8', newline='')
writer = UnicodeWriter(f)
result = conn.execute('select * from kftestcase')
writer.writerows(result)
writer.close()

procBOM(csvFile, True)



