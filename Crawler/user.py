from db_model import DbModel
from userClick import UserClick
from page import Page
from userSearch import UserSearch

class User(DbModel):
    _dbTable = 'users'
    _fields = ["id", "email", "fname", "lname", "country", "phone"]

    def __init__(self):
        super(User, self).__init__()

        self.id = None
        self.email = None
        self.fname = None
        self.lname = None
        self.country = None
        self.phone = None
        self.clicks = []
        self.searchs = []
       
    @classmethod
    def create(cls, self, fieldsValuesDict={}):
        """
        Creates an instance of the calling class.
        :return:
        """
        instance = User()

        for (field, value) in fieldsValuesDict:
            setattr(instance, field, value)

        return instance

    def getClicks(self):
        userClicksObj = UserClick()
        clicks = userClicksObj.get({"user_id": self.id})
        for click in clicks:
            page = Page().get({"id": click[2]})
            self.clicks.append(page)

    def getSearchs(self):
        userSearchsObj = UserSearch()
        searchs = userSearchsObj.get({"page_id": self.id})
        for search in searchs:
            self.searchs.append(search)

    def addClick(self, page_id):
        userClickObj = UserClick()
        userClickObj.user_id = self.id
        userClickObj.page_id = page_id
        userClickObj.save()
        self.clicks.append(userClickObj)

    def addSearch(self, search_text):
        userSearchObj = UserSearch()
        userSearchObj.user_id = self.id
        userSearchObj.search_text = search_text
        userSearchObj.save()
        self.searchs.append(userSearchObj)


