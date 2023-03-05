import pymysql
import psutil
 
client_ip = psutil.net_if_addrs()
 
# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    # 插入纪录
    with connection.cursor() as cursor:
        sql = "INSERT INTO ip_record (ip_addr) VALUES (%s)"
        try:
            cursor.execute(sql, str(client_ip))
            connection.commit()
            print("Insert success!")
        except:
            connection.rollback()
            print("Insert fail!")
    
    # 读取纪录
    with connection.cursor() as cursor:
        sql = "SELECT id, ip_addr FROM ip_record"
        cursor.execute(sql)
        # result = cursor.fetchone()
        result = cursor.fetchall()
        print(result)
        
    # 删除记录
    with connection.cursor() as cursor:
        sql = "DELETE FROM ip_record WHERE ip_addr = %s"
        try:
            cursor.execute(sql, str(client_ip))
            connection.commit()
            print("Delete success!")
        except:
            connection.rollback()
            print("Delete fail!")
            
    # 读取纪录
    with connection.cursor() as cursor:
        sql = "SELECT id, ip_addr FROM ip_record"
        cursor.execute(sql)
        # result = cursor.fetchone()
        result = cursor.fetchall()
        print(result)
