class Car():
  def displacement(self):
    print("It moves using 4 wheels")

class Motorbike():
  def displacement(self):
    print("It moves using 2 wheels")

class Truck():
  def displacement(self):
    print("It moves with 6 wheels")

def howItMoves(vehicle):
  vehicle.displacement()

myCar = Car()

howItMoves(myCar)