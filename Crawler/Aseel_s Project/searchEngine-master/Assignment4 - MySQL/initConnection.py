import mysql.connector as mysql

def connectDB(databaseName):
	try:
		mydb = mysql.connect(
		host = "localhost",
		user = "root",
		password = "sool2020",
		database = databaseName
		)
		mycursor = mydb.cursor()
		return mydb, mycursor
	except Error as e:
		print('Error:', e)



