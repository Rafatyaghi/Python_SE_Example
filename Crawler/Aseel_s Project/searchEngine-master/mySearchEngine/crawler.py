import requests as req
from bs4 import BeautifulSoup
from db import Database
import logging


class Crawler:
    def __init__(self, database = Database()):
        """
        Creates a Crawler object.
        """
        self.database = database


    def readPage(self, url):
        """
        Tries to request a url to get and return its HTML document.
        :param url: string
        :return: BeautifulSoupObject or None
        """
        try:
            resp = req.get(url, timeout = 8)
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup
        except Exception as exception:
            msg = "FAILED REQUEST: ", str(exception)
            logging.basicConfig(filename='logFile.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.info(msg)
            return None


    def getPageURLs(self, url, soup):
        """
        Retrieves all URLs apppeared in a given HTML document.
        :param url: string
        :param soup: BeautifulSoupObject
        :return: set
        """
        urls = {""} 
        urls.pop()
        
        href_tags = soup.find_all('a', href=True)
        for a in href_tags:
            # to avoid circular refrencing
        
            if (a['href'] == "" or a['href'][0] == "#" or a['href'] == "/" or a['href'] == url): 
                continue

            # a['href'] = a['href'].split('#')[0]

            # if start with slash then add url at the beginning
            if (a['href'][0] == '/'):
                a['href'] = url + a['href']

            urls.add(a['href'])
        return urls


    def getWebsiteID(self, url):
        """
        Retrieves from the database an ID for the given url.
        :param url: string
        :return: integer
        """
        query = "SELECT websiteID FROM website WHERE websiteURL = '{0}'".format(url)
        websiteID = self.database.executeSelectQuery(query)
        return websiteID


    def insertWebsite(self, url):
        """
        Inserts the given url to `website` database table.
        :param url: string
        :return: bool
        """
        query = "INSERT INTO website (websiteURL) VALUES ('{0}')".format(url)
        result = self.database.executeInsertQuery(query)
        return result


    def getTagContentID(self, tagContent):
        """
        Retrieves from the database ID for the given tag content.
        :param tagContent: string
        :return: integer
        """
        query = "SELECT tagContentID FROM tagContent WHERE tagContent = '{0}'".format(tagContent)
        tagContentID = self.database.executeSelectQuery(query)
        return tagContentID


    def insertTagContent(self, tagContent):
        """
        Inserts the given tag content to `tagContent` database table.
        :param tagContent: string
        :return: bool
        """
        query = "INSERT INTO tagContent (tagContent) VALUES ('{0}')".format(tagContent)
        result = self.database.executeInsertQuery(query)
        return result


    def insertHyperLink(self, fromWebsiteID, toWebsiteID):
        """
        Inserts the given fromWebsiteID and toWebsiteID values to `hyperlink` database table.
        :param fromWebsiteID: string
        :param toWebsiteID: string
        :return: bool
        """
        query = "INSERT INTO hyperlink (fromWebsiteID, toWebsiteID) VALUES ('{0}', '{1}')".format(fromWebsiteID, toWebsiteID)
        result = self.database.executeInsertQuery(query)
        return result 


    def getTags(self):
        """
        Retrieves all HTML tags from `htmlTag` database table.
        :return: list
        """
        query = "SELECT * FROM htmlTag"
        tags = self.database.executeSelectQuery(query)
        return tags


    def getSpecificTag(self, soup, url, tag):
        """
        Retrieves all tags appeared in the given soup object. 
        :param soup: BeautifulSoupObject
        :parm url: string
        :parm tag: string
        :return: list
        """
        all = soup.find_all(tag)
        return all


    def getIgnoredWords(self):
        """
        Retrieves all ignored words from `ignoredWord` database table. 
        :param soup: BeautifulSoupObject
        :return: list
        """
        query = "SELECT ignoredWord FROM ignoredword" #limited
        ignoredWords = self.database.executeSelectQuery(query)
        result = []
        for word in ignoredWords:
            result.append(word[0].lower())
        return result


    def filterTagContent(self, content):
        """
        Filters a given content from some ignored words and returns the filtered one. 
        :param content: string
        :return: string
        """
        ignoredWords = self.getIgnoredWords()
        filteredContent = ""
        contentWords = content.split()
        #add regEx for azAZ
        for word in contentWords:
            word = word.lower()
            if word not in ignoredWords:
                # replace ' with \'  => escape sequence
                word = word.replace("'", "\\'").lower()
                filteredContent += word
                filteredContent += " "
            
        filteredContent = filteredContent.strip()
        return filteredContent


    def insertWebsiteTag(self, WebsiteID, tagContentID, tagID):
        """
        Inserts the given WebsiteID, tagContentID, tagID values to `website_tag` database table.
        :param WebsiteID: string
        :param tagContentID: string
        :param tagID: string
        :return: bool
        """
        query = "INSERT INTO website_tag (WebsiteID, tagContentID, tagID) VALUES ('{0}', '{1}', '{2}')".format(WebsiteID, tagContentID, tagID)
        result = self.database.executeInsertQuery(query)
        return result


    def crawl(self, url):
        """
        Crawls a given URL and fills the database tables with suitable data about the URL and its links.
        :param url: string
        """
        document = self.readPage(url)
        if document is not None:
            currentWebsiteID = self.getWebsiteID(url)
            if (currentWebsiteID == []): 
                if( self.insertWebsite(url) == True):
                    currentWebsiteID = self.getWebsiteID(url)
                else:
                    return
            currentWebsiteID = currentWebsiteID[0][0]
            urls = self.getPageURLs(url, document)
        
            for u in urls:
                uID = self.getWebsiteID(u)
                if (uID == []):
                    if( self.insertWebsite(u) == True):
                        uID = self.getWebsiteID(u)
                    else:
                        continue
                uID = uID[0][0]
                self.insertHyperLink(currentWebsiteID, uID)

            tags = self.getTags()
            for tag in tags:
                all = self.getSpecificTag(document, url, tag[1])
                for a in all:
                    filteredContent = self.filterTagContent(a.text)
                    if filteredContent == "":
                        continue
                    currentContentID = self.getTagContentID(filteredContent)
                    if (currentContentID == []):
                        if( self.insertTagContent(filteredContent) == True):
                            currentContentID = self.getTagContentID(filteredContent)
                    else:
                        continue
                    currentContentID = currentContentID[0][0]
                    self.insertWebsiteTag(currentWebsiteID, currentContentID, tag[0])