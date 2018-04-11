
# -*- coding: utf8 -*-
import MySQLdb

dbConnector = {
    'yb':['riskeys_yb','Ja5pe+hYjBc=','116.62.28.180',3306,'riskeys_yb'],
    'cbs':['cbs','jBS+FSt7pvvKv6Y=','116.62.28.180',3306,'cbs_db']
}

class DbUnit():

    
    def sqlExec(self,sql,db):
        connector = dbConnector[db]
        print connector
        conn = MySQLdb.connect(user=connector[0], passwd=connector[1], host=connector[2], port=connector[3],
                               db=connector[4])
        # conn = MySQLdb.connect(user="riskeys_yb", password="Ja5pe+hYjBc=", host="116.62.28.180",port='3306', database="riskeys_yb")
        cursor = conn.cursor()
        cursor.execute (sql)
        row = cursor.fetchone ()
        #print "server version:", row[0]
        cursor.close()
        conn.commit()
        conn.close()
        return row


if __name__ == '__main__':
    sql = "select *  from core_order where id = '4F00010078334A7A92590000' and appid = 'anyi'"
    res = DbUnit().sqlExec(sql,'cbs')
    print res