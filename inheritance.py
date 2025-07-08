class Vehicles():
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.running = False
    self.accelerate = False
    self.brake = False
  
  def startUp(self):
    self.running = True
  
  def accelerate(self):
    self.accelerate = True
  
  def brake(self):
    self.brake = True
  
  def state(self):
    print("Brand: ", self.brand, "\nModel: ", self.model, "\nIs Running: ", self.running, "\nAccelerating: ", self.accelerate, "\nBraking: ", self.brake)


class Motorcycle(Vehicles):
  pass

myMotorcycle = Motorcycle("Honda", "CBR")

myMotorcycle.state()