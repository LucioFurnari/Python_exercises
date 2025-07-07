class Car():

  def __init__(self):
    self.__lengthChassis = 250
    self.__widthChassis = 120
    self.__wheels = 4
    self.__carRunning = False

  def start(self, starting):
    self.__carRunning = starting

    if(self.__carRunning):
      return "The car is running"
    else:
      return "The car is stopped"
  
  def state(self):
    print("The car have ", self.__wheels, " wheels.")
    print("An width of ", self.__widthChassis, " and a length of ", self.__lengthChassis)

myCar = Car()

print(myCar.lengthChassis)
print(myCar.state())