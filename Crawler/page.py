from db_model import DbModel
from pageKeyword import PageKeyword
class Page(DbModel):
    _dbTable = 'pages'
    _fields = ["id", "title", "description", "link", "domain_id"]

    def __init__(self):
        super(Page, self).__init__()
        self.id = None
        self.title = None
        self.description = None
        self.link = None
        self.domain_id = None
        self.keywords = []
       
    @classmethod
    def create(cls, self, fieldsValuesDict={}):
        """
        Creates an instance of the calling class.
        :return:
        """
        instance = Page()

        for (field, value) in fieldsValuesDict:
            setattr(instance, field, value)

        return instance

    def getKeywords(self):
        pageKeywordsObj = PageKeyword()
        keywords = pageKeywordsObj.get({"page_id": self.id})
        for key in keywords:
            self.keywords.append(key)

    def addKeyword(self, keyword):
        pageKeywordObj = PageKeyword()
        pageKeywordObj.page_id = self.id
        pageKeywordObj.keyword = keyword
        pageKeywordObj.save()
        self.keywords.append(pageKeywordObj)


        

