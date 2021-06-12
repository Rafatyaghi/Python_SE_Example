from db_model import DbModel
class PageKeyword(DbModel):
            _dbTable = 'page_keywords'
            _fields = ["id", "page_id", "keyword"]

            def __init__(self):
                super(PageKeyword, self).__init__()
                self.id = None
                self.page_id = None
                self.keyword = None

            @classmethod
            def create(cls, self, fieldsValuesDict={}):
                """
                Creates an instance of the calling class.
                :return:
                """
                instance = PageKeyword()

                for (field, value) in fieldsValuesDict:
                    setattr(instance, field, value)

                return instance