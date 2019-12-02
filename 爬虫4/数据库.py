#1、导包
import pymysql

#2、创建连接
host = 'localhost'#本地主机
user = 'root'#用户名
password = ''#数据库密码
database = 'maoyan'#数据库名称
port =3306 #端口号
# cursorclass=pymysql.cursors.DictCursor   #修改数据的输出格式，加上之后输出为列表嵌套字典的格式

#创建连接
# db = pymysql.connect(host=host,user=user,password=password,database=database,)
db = pymysql.connect(host,user,password,database)

#3、创建游标对象  监测sql语句执行位置
cursor = db.cursor()

#4、编写sql语句
sql1 = 'create database python0805 charset=utf8;'
#5、执行sql语句
cursor.execute(sql1)
sql = 'show databases'
cursor.execute(sql)

#6、输出结果
print(cursor.fetchone())    #查询单条数据
print('_'*100)
print(cursor.fetchmany(3))  #查询多条数据
print('_'*100)
print(cursor.fetchall())    #查询所有数据

# sql2  ='create table students(id int auto_increment primary key,name varchar(32) not null default "",address char(32) default "")'
# cursor.execute(sql2)

#插入数据
# sql3 = 'insert into students(name,address) values("{}","{}")'.format('lisi','北京')
# cursor.execute(sql3)

#修改数据
# sql4 = 'update students set name="王五" where id=2;'
# cursor.execute(sql4)

# sql5 = 'delete from students where id=2'
# cursor.execute(sql5)
# db.commit()

# sql6 = 'drop table students;'
# cursor.execute(sql6)
# db.commit()

sql7 = 'drop database python0805;'
cursor.execute(sql7)
db.commit()

#7、关闭连接
cursor.close()
db.close()
