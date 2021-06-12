import mysql.connector as mysql

def selectQuery(mydb, cursor, query):
	cursor = mydb.cursor()
	cursor.execute(query)
	records = cursor.fetchall()

	for record in records:
		print(record)

	if len(records) == 0:
		print("No matches")


def insertQuery(db, cursor, query): #values
    try:
        # Execute the SQL command
        cursor.execute(query)
        # Commit your changes in the database
        db.commit()
    except Error as e:
        # Rollback in case there is any error
        db.rollback()
        print('Error:', e)
    finally:
        if (db.is_connected()):
            cursor.close()
            db.close()


