from user import User
from page import Page
from extractor import Extractor
from performanceCal import PerformanceCal

import re
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from multiprocessing import Process

def crawl(url, filePath):
    p = PerformanceCal()
    p.startTimer()
    temp = Page().get({"link": url})
    temp2 = Page().get({"link": url[:-1]})
    if temp or temp2:
        return
    else:
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        page = Page()
        page.link = url
        domainLink = re.match("(http://|https://)([A-Za-z0-9_\.-]+)", url)
        domain = Page().get({"link": domainLink.group(0)})
        if domain:
            page.domain_id = domain[0].id
        else:
            page.domain_id = None
        returnMessage = None
        try:
            page.title = soup.find("title").text
        except Exception as ex:
            returnMessage = "Error :" + str(ex)

        try:
            metas = soup.find_all('meta')
            for meta in metas:
                if 'name' in meta.attrs and meta.attrs['name'] == 'description':
                    page.description = meta.attrs['content']
        except Exception as ex:
            returnMessage = "Error :" + str(ex)
        
        try:
            page.save()
            for meta in metas:
                if 'name' in meta.attrs and meta.attrs['name'] == 'keyword':
                    keywords = re.split(",", meta.attrs['content'])
                    for key in keywords:
                        
                        page.addKeyword(key)
        except Exception as ex:
            returnMessage = "Error :" + str(ex)

        try:
            t = ['h1','h2','h3', 'h4', 'h5', 'h6', 'h7', 'p', 'li']
            for i in t:
                otherTags = soup.find_all(i)
                for tag in otherTags:
                    tagText = re.split("In\s|\sin\s|At\s|\sat\s|\s|The\s|\sthe\s|On\s|\son\s|Even\s|\seven\s|Because\s|\sbecause\s|Or\s|\sor\s|Above\s|\sabove\s|Across\s|\sacross\s|After\s|\safter\s|For\s|\sfor\s|From\s|\sfrom\s|To\s|\sto\s|Until\s|\suntil\s", tag.text)
                    for key in tagText:
                        if key:
                            page.addKeyword(key)
        except Exception as ex:
            returnMessage = "Error :" + str(ex)


        if returnMessage:
            print(returnMessage)
        else:
            with open (filePath, 'a', newline='',encoding="utf-8" ) as f:
                f.write(str(page.link)+ '\n')
                f.write(str(page.title) + '\n')
                f.write(str(page.description) + '\n')
                f.write("Keywords:\n")
                for keyword in page.keywords:
                    f.write(str(keyword.keyword) + '\n')
            p.endTimer()
            p.getStatus()
            print("Status:")
            print("page avg CPU Usage:\t" , p.getAvgCpuUsage())
            print("page avg CPU Frequency:\t" , p.getAvgCpuFreq(), "Hz")
            print("page avg RAM Usage:\t" , p.getAvgRamUsage(), " MB")
            print("page avg Execution Time:\t" , p.getAvgExecutionTime(), " Sec")
        time.sleep(1)
        tags = []
        for tag in soup.findAll('a'):
            try:
                if re.findall(tag["href"], url):
                    raise Exception("Already Crawled")
                isFullPath = re.match("(http://|https://)([A-Za-z0-9_\.-]+)", tag["href"])
                isChildPage = re.match("^/[a-zA-Z0-9_.\s/\-]*$", tag["href"])
                beforeHash = re.findall("^(.*?)#.*$", url)
                if not beforeHash:
                    beforeHash = [url]

                if isFullPath:
                    tags.append(tag["href"])
                elif isChildPage:
                    if url[len(url)-1] == "/":
                        url = url[:-1]
                    thisUrl = url + isChildPage.group(0)
                    tags.append(thisUrl)
                elif tag["href"][0] == "#":
                    raise Exception("Already Crawled")
                else:
                    parent = re.findall("^(.*?)[a-zA-Z0-9_.\-\s]*$", url)
                    thisUrl = parent[0] + tag["href"]
                    tags.append(thisUrl)
            except:
                continue

            for link in tags:
                crawl(link, filePath)




if __name__ == "__main__":
    websites = ["https://www.microsoft.com/en-us/",
    "https://www.apple.com/uk/",
    "http://www.aljazeera.com/",
    "http://www.msn.com/",
    "http://www.python.org/",
    "https://www.mi.com/global/",
    "http://www.blogger.com/",
    "http://adobe.com/",
    "http://europa.eu/",
    "http://mozilla.org/",
    "http://es.wikipedia.org/",
    "http://istockphoto.com/",
    "http://medium.com/",
    "http://creativecommons.org/",
    "http://bbc.co.uk/",
    "http://amazon.com/",
    "http://line.me/",
    "http://forbes.com/",
    "http://feedburner.com/",
    "http://ok.ru/",
    "http://wikimedia.org/",
    "http://cnn.com/",
    "http://w3.org/"]

    filePath = "output.txt"
    mainPerformance = PerformanceCal()
    performance = PerformanceCal()
    mainPerformance.startTimer()

    p = list()
    for i in range(len(websites)):
        p.append(Process(target= crawl, args=(websites[i], filePath)))

    for process in p:
        performance.startTimer()
        process.start()
        performance.endTimer()
        performance.getStatus()
        print("Status:")
        print("website avg CPU Usage:\t" , performance.getAvgCpuUsage())
        print("website avg CPU Frequency:\t" , performance.getAvgCpuFreq(), "Hz")
        print("website avg RAM Usage:\t" , performance.getAvgRamUsage(), " MB")
        print("website avg Execution Time:\t" , performance.getAvgExecutionTime(), " Sec")

    for process in p:
        process.join()
        
    mainPerformance.endTimer()
    print("Total Execution Time:\t" , mainPerformance.getAvgExecutionTime(), " Sec")
    numbers = Extractor.extractNumeric(filePath)
    dates = Extractor.extractDateTime(filePath)
    questions = Extractor.extractQuestions(filePath)
    numberOfSymbols = Extractor.extractSpecialCharCount(filePath)
    