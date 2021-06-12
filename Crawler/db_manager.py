import config
import MySQLdb as mySqlConnector
from db_result_set import DbResultSet


class DbManager:

    def __init__(self, host=None, user=None, password=None, database=None):
        """
        Creates a DbManager object with the given credentials to connect to database. If no credentials are provided,
        the credentials in the database/config.py will be used.
        :param host: string
        :param user: string
        :param password: string
        :param database: string
        """
        self.host = host if host is not None else "localhost"
        self.user = user if user is not None else "root"
        self.password = password if password is not None else "1234"
        self.database = database if database is not None else "search_engine"
        
        DbManager.connection = self.connect()


    def connect(self):
        """
        Tries to connect to the database using the credentials provided in the constructor, or the config otherwise.
        :return: MySQLConnection or None
        """
        connection = None

        try:
            connection = mySqlConnector.connect(self.host, self.user, self.password, self.database, charset='utf8', use_unicode=True)
        except Exception as exception:
            print("DATABASE EXCEPTION: {0}".format(str(exception)))

        return connection


    def executeSelectQuery(self, query):
        """
        Executes the given SQL select query on the database, and returns the whole result set, or None.
        :param query: string
        :return: DbResultSet
        """
        resultSet = DbResultSet()
        connection = DbManager.connection
        cursor = connection.cursor()

        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            resultSet.fill(rows)

        except Exception as exception:
            print("QUERY EXCEPTION IN: {0} --> {1}".format(query, str(exception)))

        finally:
            cursor.close()
            del cursor

        return resultSet


    def execute(self, query):
        """
        Executes the given SQL statement(s) on the database, and returns ID of the last inserted row or the number of
        rows that were affected.
        :param query: string|list of string
        :return: bool
        """
        connection = DbManager.connection
        cursor = connection.cursor()
        result = False

        try:
            cursor.execute(query)
            connection.commit()
            # If we have inserted, we get the latest inserted ID, otherwise we get 1 to indicate that the query
            # has succeeded no matter how many rows were affected.
            result = cursor.lastrowid if cursor.lastrowid > 0 else 1

        except Exception as exception:
            print("D.B. EXCEPTION IN: {0} --> {1}".format(query, str(exception)))

            try:
                connection.rollback()
            except Exception as exception:
                print("ROLLBACK EXCEPTION IN: {0} --> {1}".format(query, str(exception)))

        finally:
            cursor.close()
            del cursor

        return result
    

    def executeScript(self, scriptFileUrl):
        """
        Executes all queries in the SQL script whose url is passed.
        :param scriptFileUrl: string
        :return: bool
        """
        result = True
        sqlScript = open(scriptFileUrl, "r").read()
        queries = sqlScript.split(";")

        for query in queries:
            query = query.strip()

            if len(query) > 0:
                queryResult = self.execute(query)
                result = result and queryResult
        
        return  result


    def initializeTables(self):
        """
        Inserts the initial values that should exist in the tables to start the tool.
        :return: bool
        """
        sqlScriptFile = "packages/database/sql/initialize.sql"
        result = self.executeScript(sqlScriptFile)
        return result


    def createTables(self):
        """
        Creates the database tables that are used in this tool.
        :return: bool
        """
        sqlScriptFile = "packages/database/sql/create.sql"
        result = self.executeScript(sqlScriptFile)
        result = result and self.initializeTables()
        return result


    def cleanTables(self):
        """
        Deletes all records and resets all auto-increment pointers in the database.
        :return: bool
        """
        sqlScriptFile = "packages/database/sql/clean.sql"
        result = self.executeScript(sqlScriptFile)
        result = result and self.initializeTables()
        return result


    def dropTables(self):
        """
        Drops the database tables that are used in this tool.
        :return: bool
        """
        sqlScriptFile = "packages/database/sql/drop.sql"
        result = self.executeScript(sqlScriptFile)
        return result


    def getDbSize(self):
        """
        Calculates the current DB size in MB.
        :return: float
        """
        dbSize = 0.0
        sql = """
            SELECT 
                ROUND(SUM(tables_info.data_length + tables_info.index_length) / 1024 / 1024, 2) AS db_size
            FROM 
                information_schema.tables tables_info
            WHERE
                tables_info.table_schema = "{db}"; 
        """.format(db=self.database)
        result = self.executeSelectQuery(sql)

        if result.rows_count > 0:
            dbSize = float(result.rows[0][0])

        return dbSize
