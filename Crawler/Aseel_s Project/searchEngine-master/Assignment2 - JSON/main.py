from Car import Car
import json


def creatCarList(numOfItems):
    resultedlist = []
    while numOfItems > 0:
        car = Car()
        car.fillRandomly()
        resultedlist.append(car.asdict())
        numOfItems -= 1
    return resultedlist


if __name__ == "__main__":

    carsList = creatCarList(10)
    
    jsonFile = open("jsonFile.json", "w")
    jsonFormat = json.dumps(carsList)
    jsonFile.write(jsonFormat)

    jsonFile = open("jsonFile.json", "r")
    jsonFormat = jsonFile.read()
    stringFormat = json.loads(jsonFormat)
    
    for item in stringFormat:
        print(item)