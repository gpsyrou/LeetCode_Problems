'''
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
 

'''

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_left = big
        self.medium_left = medium
        self.small_left = small

    def addCar(self, carType: int) -> bool:
        if (carType == 1) and (self.big_left > 0) :
            self.big_left -= 1
            return True
        elif (carType == 2) and (self.medium_left > 0):
            self.medium_left -= 1
            return True          
        elif (carType == 3) and (self.small_left > 0):
            self.small_left -= 1
            return True   
        else: 
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)