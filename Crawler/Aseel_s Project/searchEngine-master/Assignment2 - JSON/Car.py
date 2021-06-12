import string
import random

class Car:

    brand = ""
    productionYear = ""
    fuelType = ""
    colour = ""
    numberOfSeats = ""

    def __init__(self, brand="", productionYear="", fuelType="", colour="", numberOfSeats=""):
        self.brand = brand
        self.productionYear = productionYear
        self.fuelType = fuelType
        self.colour = colour
        self.numberOfSeats = numberOfSeats

    # setter and getter

    def fillRandomly(self):
        self.brand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.productionYear = ''.join(random.choices(string.digits, k=4))
        self.fuelType = ''.join(random.choices(string.ascii_uppercase, k=5))
        self.colour = ''.join(random.choices(string.ascii_uppercase, k=5))
        self.numberOfSeats = ''.join(random.choices(string.digits, k=1))


    def toString(self):
        print("Brand: " + self.brand + "\n" + "Production Year: " + self.productionYear + "\n" + "Fuel Type: " +
              self.fuelType + "\n" + "Colour: " + self.colour + "\n" + "Number of Seats: " + self.numberOfSeats + "\n")


    def asdict(self):
        return {'Brand': self.brand, 'Production Year': self.productionYear, 'Fuel Type': self.fuelType, 'Colour': self.colour, 'Number of Seats': self.numberOfSeats}