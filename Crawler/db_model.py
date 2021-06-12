from db_manager import DbManager


class DbModel(object):

    _dbManager = DbManager()
    _dbTable = None
    _fields = []



    def __init__(self):
        pass


    @classmethod
    def create(cls, self, fieldsValuesDict={}):
        """
        Creates a new instance of the calling class.
        :return: DbModel
        """
        return DbModel()


    def get(self, criteria={}):
        """
        Retrieves records from database that match the criteria passed within criteria dictionary.
        :param criteria: dict
        :return: list of (self)
        """
        # Basic select statement.
        sql = "SELECT * FROM `{0}`".format(self._dbTable)

        # If any criteria are passed.
        if len(criteria) > 0:
            # Create the conditions segment.
            conditions = []
            for (field, value) in criteria.items():
                conditions.append(" `{0}`.`{1}` = '{2}' ".format(self._dbTable, field, value))

            # Add the where-clause and the conditions.
            sql += " WHERE {0}".format("AND ".join(conditions))

        # Execute the query and get the result set.
        resultSet = self._dbManager.executeSelectQuery(sql)
        records = []

        # Set the properties of the objects.
        for row in resultSet.rows:
            # Create an object of the caller.
            record = self.create(criteria)

            # Set values of the fields.
            for i in range(0, len(self._fields)):
                setattr(record, self._fields[i], row[i])

            # Add the record to the records list.
            records.append(record)

        return records


    @classmethod
    def getFirst(cls, self, criteria={}):
        """
        Retrieves the first record only from database that matches the criteria passed within criteria dictionary.
        :param criteria: dict
        :return: list of (self)
        """
        # Basic select statement.
        sql = "SELECT * FROM `{0}`".format(self._dbTable)

        # If any criteria are passed.
        if len(criteria) > 0:
            # Create the conditions segment.
            conditions = []
            for (field, value) in criteria.iteritems():
                conditions.append(" `{0}`.`{1}` = '{2}' ".format(self._dbTable, field, value))

            # Add the where-clause and the conditions.
            sql += " WHERE {0}".format("AND ".join(conditions))

        sql += " LIMIT 1"

        # Execute the query and get the result set.
        resultSet = self._dbManager.executeSelectQuery(sql)
        # Create an empty object of the caller.
        record = self.create()

        if resultSet.rows_count > 0:
            # Read the first row.
            row = resultSet.rows[0]

            # Set values of the fields.
            for i in range(0, len(self._fields)):
                setattr(record, self._fields[i], row[i])

        return record


    def exists(self, wrtField="id"):
        """
        Checks if there is a record in the database whose value for the given wrtField matches this object's.
        :param wrtField: string
        :return: bool
        """
        value = getattr(self, wrtField)
        records = self.get({wrtField: value})
        return len(records) > 0


    def save(self, wrtField="id"):
        """
        Saves the current object status to the database, or creates a new record if the calling object does not exist
        in the database with respect to the wrtField provided.
        :param wrtField: string
        :return: bool
        """
        # Default result of the function.
        result = True
        # List of fields that will be used in insertion or update.
        fieldsToAffect = list(self._fields)
        # Remove the ID because it should normally be auto-incremented, and is rarely updated.
        if "id" in fieldsToAffect:
            fieldsToAffect.remove("id")

        # If the record exists, update.
        if self.exists(wrtField):
            # Also remove the wrtField from the update list because it won't be updated, we rather use it as a ref.
            if wrtField in fieldsToAffect:
                fieldsToAffect.remove(wrtField)

            # If we still have fields to update.
            if len(fieldsToAffect) > 0:
                sql = "UPDATE `{0}` SET ".format(self._dbTable)

                # Loop over the fields to update them.
                for field in fieldsToAffect:
                    value = self.getSqlValue(getattr(self, field))
                    sql += "`{0}` = {1}, ".format(field, value)

                # Get rid of the last comma.
                sql = sql[:-2]

                # Add the condition with respect to the wrtField.
                wrtValue = getattr(self, wrtField)
                sql += " WHERE `{0}` = '{1}'".format(wrtField, wrtValue)

                result = self._dbManager.execute(sql)

            # Reload the fields values from the database.
            self.refresh(wrtField)

        # Otherwise, create a new record.
        else:

            for i in range(0, len(fieldsToAffect)):
                fieldsToAffect[i] = "`" + fieldsToAffect[i] + "`"

            sql = "INSERT INTO `{0}` ({1})".format(self._dbTable, ", ".join(fieldsToAffect))
            # Add the values-clause.
            sql += " VALUES ("

            # Add the value of all fields to be inserted.
            for field in fieldsToAffect:
                attribute = field.replace("`", "")
                value = self.getSqlValue(getattr(self, attribute))
                sql += "{0}, ".format(value)

            # Get rid of the last comma and add a closing parenthesis.
            sql = sql[:-2] + ")"

            # Execute the insert, and update the record id.
            recordId = self._dbManager.execute(sql)
            setattr(self, "id", recordId)
            result = recordId > 0

        return result


    def refresh(self, wrtField):
        """
        Reloads the data of the calling object from the database.
        :param wrtField: string
        :return: bool
        """
        result = False
        # Get the "get" method to be called from the suitable object type.
        method = getattr(self, "get")
        # The reference value to retrieve the record.
        wrtValue = getattr(self, wrtField)
        # Get the records, usually should be one record.
        records = method({wrtField: wrtValue})

        # Make sure the result set is not empty.
        if len(records) > 0:
            # Set the result to true.
            result = True

            # Update the fields of the calling object.
            for field in self._fields:
                value = getattr(records[0], field)
                setattr(self, field, value)

        return result

        
    def delete(self, wrtField="id"):
        """
        Deletes the record(s) from the database whose values of wrtField is similar to the caller's.
        :param wrtField: string
        :return: bool
        """
        # The reference value to retrieve the records.
        value = getattr(self, wrtField)
        # Query to delete the records.
        sql = "DELETE FROM `{0}` WHERE {1} = '{2}'".format(self._dbTable, wrtField, value)
        # Execute query and get the result.
        result = self._dbManager.execute(sql)

        return result


    @classmethod
    def getDbInfo(cls):
        """
        Retrieves the config information used to connect to the current database.
        :return: dict
        """
        dbInfo = {"host": cls._dbManager.host, "user": cls._dbManager.user,
                  "password": cls._dbManager.password, "database": cls._dbManager.database}

        return dbInfo


    @classmethod
    def getSqlValue(cls, rawValue):
        """
        Handles the conversion between Python values and SQL values like None --> NULL
        """
        sqlValue = None

        if rawValue is None:
            sqlValue = "NULL"
        elif rawValue is True:
            sqlValue = "1"
        elif rawValue is False:
            sqlValue = "0"
        else:
            sqlValue = "'" + cls.handleSpecialChars(rawValue) + "'"

        return sqlValue


    @classmethod
    def handleSpecialChars(cls, value):
        """
        Handles the special characters to avoid unexpected results in queries.
        """
        text = str(value)
        text = text.replace("\"", "\\\"")
        text = text.replace("'", "\\'")
        return text


    def dumpMe(self):
        """
        Builds a string that holds the type, and all the fields and their corresponding values of the caller.
        :return: string
        """
        dump = str(self.__class__) + ": \r\n"
        dump += "{\r\n"

        for field in self._fields:
            dump += "   {0} -> {1} \r\n".format(field, getattr(self, field))

        dump += "}\r\n"

        return dump
