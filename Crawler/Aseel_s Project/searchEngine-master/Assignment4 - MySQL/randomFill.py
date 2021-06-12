import mysql.connector as mysql
from initConnection import connectDB
from crud import *
from random import choice

# import pydbgen as pd
# from pydbgen import pydbgen
# myDB=pydbgen.pydb()

# myDB.city_real(myDB)


if __name__ == '__main__':

	(mydb, mycursor) = connectDB("airport")
	sql = "INSERT INTO flight(countryID, arrivalTime, departureTime, direction, aircraftID) VALUES (6, '2019-07-05 00:04:00', '2019-07-02 23:59:59' , 0, 1);"	
	insertQuery(mydb, mycursor, sql)
	mycursor.close()
	mydb.close()
