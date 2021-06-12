import timeit
from xmlElement import XmlElement
from xmlTree import XmlTree
import xml.etree.ElementTree as ET

if __name__ == "__main__":


    inputFilePaths = ['test1.xml', 'test2.xml', 'test3.xml']
    outputFilePath = 'output.xml'

    for t in range(len(inputFilePaths)):
        time1 = 0
        testCases = 10000
        for i in range(testCases):
            start = timeit.default_timer()
            currentTree = XmlTree.createFromFile(inputFilePaths[t])
            stop = timeit.default_timer()
            time1 += (stop - start)

        print("myOwnCode Time on " , inputFilePaths[t], " ==> ", time1/testCases)    

    # if currentTree is not None:
    #     currentTree.saveToFile(outputFilePath)

    
    for t in range(len(inputFilePaths)):
        time2 = 0
        testCases = 1000
        for i in range(testCases):
            start = timeit.default_timer()
            currentTree = ET.TreeBuilder(inputFilePaths[t])
            stop = timeit.default_timer()
            time2 += (stop - start)

        print("Python Time on " , inputFilePaths[t], " ==> ", time2/testCases) 