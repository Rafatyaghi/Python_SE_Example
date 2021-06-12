from db_model import DbModel
class UserSearch(DbModel):
            _dbTable = 'user_searchs'
            _fields = ["id", "user_id", "search_text"]

            def __init__(self):
                super(UserSearch, self).__init__()
                self.id = None
                self.user_id = None
                self.search_text = None

            @classmethod
            def create(cls, self, fieldsValuesDict={}):
                """
                Creates an instance of the calling class.
                :return:
                """
                instance = UserSearch()

                for (field, value) in fieldsValuesDict:
                    setattr(instance, field, value)

                return instance