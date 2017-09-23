import MySQLdb

db1 = MySQLdb.connect(host="localhost",user="root",passwd="pass")
cursor = db1.cursor()


''' part a '''

sql = 'CREATE DATABASE mario'
cursor.execute(sql)




''' part b '''

sql= "CREATE USER 'astrophysics1'@'localhost' IDENTIFIED BY 'pass';"
cursor.execute(sql)

sql= "GRANT ALL PRIVILEGES ON * . * TO 'astrophysics1'@'localhost';"
cursor.execute(sql)





''' part c '''

db = MySQLdb.connect(host="localhost", user="root", passwd="pass", db="mario")
db.autocommit(True)

cur = db.cursor()

sql= '''CREATE TABLE IF NOT EXISTS astrophysics_users (
		id int(11) NOT NULL AUTO_INCREMENT,  		
		Name varchar(45) NOT NULL,
		Designation varchar(45),
  		Email varchar(45),
		PRIMARY KEY (id)
		);'''
cur.execute(sql)


values=[
        ['Albert', 'Professor', 'albert@icts.res.in'],
        ['Einstein', 'Asst. Professor' ,'einstein@icts.res.in'],
        ['Michael', 'Student','michael@icts.res.in'],
        ['John' , 'Student' , 'john@icts.res.in']
       ]

for line in values:
	sql= "INSERT INTO astrophysics_users(Name, Designation, Email) VALUES ('"+line[0]+"','"+line[1]+"','"+line[2]+"');"
	cur.execute(sql)
	print 'inserted'





''' part d '''

sql= '''CREATE TABLE IF NOT EXISTS astrophysics_students (		
		Name varchar(45) NOT NULL,
  		Email varchar(45)
		);'''
cur.execute(sql)


sql= '''INSERT INTO astrophysics_students(Name, Email)
	SELECT Name, Email
	FROM astrophysics_users
	WHERE Designation='Student';'''
cur.execute(sql)










