import pandas as pd
from mysql.connector import MySQLConnection, Error
import mysql.connector 


def connect():
    db_config = {
        'host': 'localhost',
        'database': 'python_bai3',
        'user': 'root',
        'password': ''
    }
    
    conn = None
 
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
 
    except Error as error:
        print(error)
 
    return conn

df = pd.read_excel('input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
print(df)



# import ex

# data = []
# for row in df.iterrows():
#     row_data = []
#     for value in row[1]:
#         row_data.append(value)
#     sql = "insert into students(id, code, first_name, last_name, birthOfDate, Toan, Ly, Hoa) values (%s,%s,%s,%s,%s,%s,%s,%s)"
#     conn = connect()
#     val = (row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7])
#     cursor = conn.cursor()
#     cursor.execute(sql, val)
#     conn.commit()
#     data.append(row_data)

myconn = mysql.connector.connect(host = "localhost", user = "root",
password = "", database = "python_bai3")
cur = myconn.cursor()

# Thêm
def insert():
    sql = "insert into students(id, code, first_name, last_name, birthOfDate, Toan, Ly, Hoa)" + "values (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (53, "C2000","abc","def","12/02/2000",8,9,8)
    try:
        cursor = myconn.cursor()
        cursor.execute(sql, val)
        myconn.commit()
        print(cursor.rowcount, "record(s) was inserted.")
    except:
        myconn.rollback()
        myconn.close()



# Update
def update(): 
    try:
        cur.execute("update students set first_name = 'Tran Van', last_name = 'An' where id = 52")
        myconn.commit()
        print(cur.cursor.rowcount, "record(s) was updated.")
    except:
        myconn.rollback()
        myconn.close()

#XOA
def delete():
    try:
    # cập nhật name cho bảng students
        cur.execute("delete from students where id = 53")
        print('delete thanh cong id')
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()

insert()

