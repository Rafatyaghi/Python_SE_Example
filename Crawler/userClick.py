from db_model import DbModel
from page import Page
class UserClick(DbModel):
            _dbTable = 'user_clicks'
            _fields = ["id", "user_id", "page_id"]

            def __init__(self):
                super(UserClick, self).__init__()

                self.id = None
                self.user_id = None
                self.page_id = None

            @classmethod
            def create(cls, self, fieldsValuesDict={}):
                """
                Creates an instance of the calling class.
                :return:
                """
                instance = UserClick()

                for (field, value) in fieldsValuesDict:
                    setattr(instance, field, value)

                return instance

            def getPage(self):
                page = Page().get({"page_id": self.page_id})
                return page
