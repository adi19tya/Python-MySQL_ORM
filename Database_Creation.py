import mysql.connector

# MYSQL Commands
# show databases
# show tables
# select * from <table name>
# drop database <database name>
# INNER JOIN:
#	SELECT EMPLOYEE_ID, NAME, DEPARTMENT.DEPARTMENT_ID, DEPARTMENT_NAME FROM EMPLOYEE JOIN DEPARTMENT ON EMPLOYEE.DEPARTMENT_ID = DEPARTMENT.DEPARTMENT_ID;
#   SELECT EMPLOYEE_ID, NAME, EMPLOYEE.DEPARTMENT_ID, DEPARTMENT_NAME FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.DEPARTMENT_ID = DEPARTMENT.DEPARTMENT_ID;

#--------------------------------------------------------------#

# Create connection
def connectToMysql(database):
	conn = mysql.connector.connect(
		host ="localhost",
	  	user ="root",
	  	passwd ="1123581321",
	  	database = database
		) 
	return conn
conn = connectToMysql("")
cursor = conn.cursor()

#--------------------------------------------------------------#

# Reset
deleteDataBase = "drop database company1"
cursor.execute(deleteDataBase)
print(" -> Deleted company1 Database\n")

#--------------------------------------------------------------#

# Create Database:
createDatabase = "CREATE DATABASE company1"
cursor.execute(createDatabase)
print(" -> Created company1 Database\n")
# Connect and point cursor to the company1 database
conn = connectToMysql("company1")
cursor = conn.cursor()
print(" -> Connected cursor to the company1 Database\n")

#--------------------------------------------------------------#

# Create DEPARTMENT table:
tableRecord = """CREATE TABLE DEPARTMENT(
	DEPARTMENT_ID INT,
	DEPARTMENT_NAME VARCHAR(255) NOT NULL,
	PRIMARY KEY (DEPARTMENT_ID)
	)"""
cursor.execute(tableRecord)
print(" -> Created the DEPARTMENT table\n")

# Create EMPLOYEE table:
tableRecord = """CREATE TABLE EMPLOYEE(
	EMPLOYEE_ID INT,
	NAME VARCHAR(255),
	EMAIL VARCHAR(255),
	DEPARTMENT_ID INT,
	PRIMARY KEY (EMPLOYEE_ID),
	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENT(DEPARTMENT_ID)
	)"""
cursor.execute(tableRecord)
print(" -> Created the EMPLOYEE table\n")

# Create SALARY table:
tableRecord = """CREATE TABLE SALARY(
	EMPLOYEE_ID INT,
	CTC INT,
	BASIC INT,
	VARIABLE INT,
	PRIMARY KEY (EMPLOYEE_ID),
	FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID),
	INDEX(CTC, BASIC)
	)"""
cursor.execute(tableRecord)
print(" -> Created the SALARY table\n")

#--------------------------------------------------------------#

# Insert multiple Rows in the DEPARTMENT Table
sql = "INSERT INTO DEPARTMENT (DEPARTMENT_ID, DEPARTMENT_NAME) VALUES (%s, %s)"
val = [("1", "Admin"), 
	   ("2", "HR"), 
	   ("3", "IT")]
cursor.executemany(sql, val)
conn.commit()
print(" -> Inserted into the DEPARTMENT Table\n")

# Insert multiple Rows in the EMPLOYEE Table
sql = "INSERT INTO EMPLOYEE (EMPLOYEE_ID, NAME, EMAIL, DEPARTMENT_ID) VALUES (%s, %s, %s, %s)"
val = [(str(1001), "Nikhil", "Nikhil@gmail.com", str(1)), 
	   (str(1002), "Lakshmi", "Lakshmi@gmail.com", str(1)), 
	   (str(1004), "Nisha", "Nisha@gmail.com", None), 
	   (str(1008), "Rohan", "Rohan@gmail.com", str(3)), 
	   (str(1009), "Amit", "Amit@gmail.com", str(1)), 
	   (str(1012), "Anil", "Anil@gmail.com", str(3)), 
	   (str(1016), "Megha", "Megha@gmail.com", str(2)), 
	   (str(1023), "Sita", "Sita@gmail.com", None), 
	   (str(1024), "Ram", "Ram@gmail.com", str(2))]
#val = (str(1001), "Nikhil", "Nikhil@gmail.com", "1")
cursor.executemany(sql, val)
conn.commit()
print(" -> Inserted into the EMPLOYEE Table\n")

# Insert multiple Rows in the SALARY Table
sql = "INSERT INTO SALARY (EMPLOYEE_ID, CTC, BASIC, VARIABLE) VALUES (%s, %s, %s, %s)"
val = [("1001", "12", "9", "3"),
	   ("1002", "8", "7", "1"),
	   ("1004", "15", "10", "5"),
	   ("1008", "13", "12", "1"),
	   ("1009", "8", "6", "2"),
	   ("1012", "19", "8", "11"),
	   ("1016", "4", "3", "1"),
	   ("1023", "37", "30", "7"),
	   ("1024", "17", "15", "2")]
cursor.executemany(sql, val)
conn.commit()
print(" -> Inserted into the SALARY Table\n")

#--------------------------------------------------------------#

# INNER JOIN

innerJoinQuery = "SELECT EMPLOYEE_ID, NAME, EMPLOYEE.DEPARTMENT_ID, DEPARTMENT_NAME FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.DEPARTMENT_ID = DEPARTMENT.DEPARTMENT_ID;"
cursor.execute(innerJoinQuery)
myResult = cursor.fetchall()

print("The INNER JOIN: ")
for elem in myResult:
	print(elem)

print(" -> Completed an INNER Join operation")

#--------------------------------------------------------------#
