class DbResultSet:

    _rows = []
    _rowsCount = 0

    def __init__(self):
        pass


    def fill(self, rowsList):
        """
        Fills the result set's rows and sets the related variables like rowsCount.
        :param rowsList: list
        """
        self._rows = rowsList
        self._rowsCount = len(rowsList)


    @property
    def rows(self):
        return self._rows


    @property
    def rows_count(self):
        return self._rowsCount
