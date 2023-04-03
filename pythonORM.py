import mysql.connector

class Employee():

	def __init__(self, empID, empName, empEmail, empDept, empSalary):
		self.empID = empID
		self.empName = empName
		self.empEmail = empEmail
		self.empDept = empDept
		self.empSalary = empSalary

	def showEmployeeDetails(self):
		print("Employee Details: \nEmployee ID: ", self.empID, "\nEmployee Name: ", self.empName, "\nEmployee Email: ", self.empEmail, "\nDepartment Name: ", self.empDept, "\nEmployee Salary: ", self.empSalary, "Lakhs\n")

class Department():

	def __init__(self, deptID, deptName):
		self.deptID = deptID
		self.deptName = deptName

	def showDepartmentDetails(self):
		print("\nDepartment Details: \nDepartment ID: ", self.deptID, "\nDepartment Name: ", self.deptName)

class Salary():

	def __init__(self, empID, ctc, basic, variable):
		self.empID = empID
		self.ctc = ctc
		self.basic = basic
		self.variable = variable

def connectToMysql():
	conn = mysql.connector.connect(
		host ="localhost",
	  	user ="root",
	  	passwd ="1123581321",
	  	database = "company1"
		)
	return conn
conn = connectToMysql()
cursor = conn.cursor()

#--------------------------------------------------------------#

# employeeDetails_Query = "SELECT EMPLOYEE_ID, NAME FROM EMPLOYEE"

# cursor.execute(employeeDetails_Query)

# myResult = cursor.fetchall()

# employeeList = []
# for x in  :
# 	employeeList.append(x)

# print("Employee List: ", employeeList)

#--------------------------------------------------------------#

# Salary Datails

salaryDetails_Query = "SELECT * FROM SALARY"

cursor.execute(salaryDetails_Query)
salaryResult = cursor.fetchall()

salaryList = []
salaryDict = dict()
for x in  range(len(salaryResult)):
	salaryList.append(Salary(salaryResult[x][0], salaryResult[x][1],salaryResult[x][2], salaryResult[x][3]))
	salaryDict[salaryResult[x][0]] = salaryResult[x][1]

print("Salary Dict: ", salaryDict)

# for salaryObject in range(len(salaryList)):
# 	salaryList[salaryObject].showSalaryDetails()

#--------------------------------------------------------------#

# Departmment Datails

departmentDetails_Query = "SELECT * FROM DEPARTMENT"

cursor.execute(departmentDetails_Query)
departmentResult = cursor.fetchall()

departmentList = []
departmentDict = dict()
for x in  range(len(departmentResult)):
 	departmentList.append(Department(departmentResult[x][0], departmentResult[x][1]))
 	departmentDict[departmentResult[x][0]] = departmentResult[x][1]

for departmentObject in range(len(departmentList)):
	departmentList[departmentObject].showDepartmentDetails()

print("Department Dict: ", departmentDict)
print("\n")

#--------------------------------------------------------------#

# Employee Datails

employeeDetails_Query = "SELECT * FROM EMPLOYEE"

cursor.execute(employeeDetails_Query)
employeeResult = cursor.fetchall()

employeeList = []
for x in  range(len(employeeResult)):

	if employeeResult[x][3] != None:
		departmentName = departmentDict[employeeResult[x][3]]
	else:
		departmentName = None
	employeeSal = salaryDict[employeeResult[x][0]]

	employeeList.append(Employee(employeeResult[x][0], employeeResult[x][1],employeeResult[x][2], departmentName, employeeSal))

for employeeObject in range(len(employeeList)):
	employeeList[employeeObject].showEmployeeDetails()

#--------------------------------------------------------------#
