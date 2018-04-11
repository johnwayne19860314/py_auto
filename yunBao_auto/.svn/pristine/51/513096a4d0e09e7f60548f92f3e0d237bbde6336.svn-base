
# -*- coding: utf8 -*-
import MySQLdb

dbConnector = {
    'yb':['riskeys_yb','Ja5pe+hYjBc=','116.62.28.180','3306','riskeys_yb'],
    'cbs':['cbs','jBS+FSt7pvvKv6Y=','116.62.28.180','3306','cbs_db']
}

class DbUnit():
    connector = dbConnector['cbs']
    print connector
    self.conn = MySQLdb.connect(user=connector[0], password=connector[1], host=connector[2], port=connector[3],
                                database=connector[4])
    # self.conn = MySQLdb.connect(user="riskeys_yb", password="Ja5pe+hYjBc=", host="116.62.28.180",port='3306', database="riskeys_yb")
    self.cursor = self.conn.cursor()
    def __init__(self):
        connector = dbConnector['cbs']
        print connector
        self.conn=MySQLdb.connect(user=connector[0],password=connector[1],host=connector[2],port=connector[3],database=connector[4])
     # self.conn = MySQLdb.connect(user="riskeys_yb", password="Ja5pe+hYjBc=", host="116.62.28.180",port='3306', database="riskeys_yb")
        self.cursor = self.conn.cursor()
    def sqlExec(self,sql):
        self.cursor.execute (sql)
        row = self.cursor.fetchone ()
        #print "server version:", row[0]
        self.cursor.close()
        self.conn.close()
        return row


if __name__ == '__main__':
    sql = "select *  from core_order where id = '4F00010078334A7A92590000' and appid = 'anyi'"
    res = DbUnit().sqlExec(sql)
    print res