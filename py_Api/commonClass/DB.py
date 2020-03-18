from py_Api.commonClass.readConfig import readConfig
from py_Api.commonClass.readExcel import doExcel
import pymysql
import re

class sqlClass:
    #执行sql#
 def dosql(sql):
  DB = doExcel.getDB(sql)
 # 打开数据库连接
  DBName = DB
  host = readConfig.getValue(DBName, 'db_host')
  port = readConfig.getValue(DBName, 'db_port')
  userName = readConfig.getValue(DBName, 'db_user')
  passWord = readConfig.getValue(DBName, 'db_pass')
  conn = psycopg2.connect(
         host=host,
         port=int(port),
         user=userName,
         password=passWord,
         database=DBName,
         charset='utf8')

 # 得到一个可以执行SQL语句的光标对象
  cursor = conn.cursor()
  str1=str(sql)
  Sql=str1.split(';\n')
  num=len(Sql)
  if num==0:
      return
  else:
    i=1
    while i<=num:
     try:
         T_sql=doExcel.getSQL(Sql[i-1])
         cursor.execute(T_sql)
         print('正在执行sql：' + T_sql)
         i = i + 1
         conn.commit()
         print("执行成功")
         #return cursor.fetchone()
     except:
         print("嘤嘤嘤,执行出错了，请检查sql："+T_sql)
         conn.rollback();
         i=i+1
    conn.close()
    return cursor.fetchone()

 def ExcuteSql(db,sql):
        # 打开数据库连接
    if(db==""or sql==""):
            return
    else:
        DBName = db
        host = readConfig.getValue(DBName, 'db_host')
        port = readConfig.getValue(DBName, 'db_port')
        userName = readConfig.getValue(DBName, 'db_user')
        passWord = readConfig.getValue(DBName, 'db_pass')
        conn = pymysql.connect(
            host=host,
            port=int(port),
            user=userName,
            password=passWord,
            database=DBName,
            charset='utf8')

        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()
        try:
         cursor.execute(sql)
         print("正在执行sql："+sql)
         conn.commit()
         print("执行成功！")
        except:
         print("嘤嘤嘤,执行出错了，请检查sql：" + sql)
         conn.rollback();
        conn.close()
        return cursor.fetchone()



  #获取一个字段string#
 def getOneStr(sql):
    result=sqlClass.dosql(sql)
    result1=str(result)
    result1=re.findall(r'[^(,]+', result)[0]
    return str(result1)












