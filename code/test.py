import sqlite3
import csv, codecs
from io import StringIO
from distutils.msvc9compiler import query_vcvarsall
class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        self.writer.writerow(row)
        data = self.queue.getvalue()
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
    def writerows(self, rows):
        for row in rows:
            print(row)
            self.writerow(row)
conn = sqlite3.connect("D:/mysqlite.db")
writer = UnicodeWriter(open("D:/export_data.csv", "w", newline=''))
result = conn.execute('select * from kftestcase')
writer.writerows(result)