import mysql.connector as mysql
from initConnection import connectDB
from crud import *
from a import query as query1
from b import query as query2
from c import query as query3
from d import query as query4
from e import query as query5
from f import query as query6
from g import query as query7


if __name__ == '__main__':

	(mydb, mycursor) = connectDB("airport")

	print("\nA. Flight number, number of passengers, and flight date for all flights that took place in May 2020:\n")
	selectQuery(mydb, mycursor, query1)

	print("\nB. Flight info for all flights between our airport and London:\n")
	selectQuery(mydb, mycursor, query2)

	print("\nC. Total number of passengers who used the airport during 2020:\n")
	selectQuery(mydb, mycursor, query3)

	print("\nD. Aircraft name, number of passengers for all aircrafts in the system, ordered descending by number of passengers:\n")
	selectQuery(mydb, mycursor, query4)

	print("\nE. Names of all Palestinian passengers who arrived at the airport:\n")
	selectQuery(mydb, mycursor, query5)

	print("\nF. Country of residence, number of flights, and average number of passengers per flight for all countries:\n")
	selectQuery(mydb, mycursor, query6)

	print("\nG. Full information of the top 5 travelling passengers:\n")
	selectQuery(mydb, mycursor, query7)


	mycursor.close()
	mydb.close()
