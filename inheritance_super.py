class Person():
  def __init__(self, name, age, place_residence):
    self.name = name
    self.age = age
    self.place_residence = place_residence

  def description(self):
    print("Name: ", self.name, "Age: ", self.age, "Residence: ", self.place_residence)

class Employee(Person):
  def __init__(self, salary, position, name_employee, age_employee, residence_employee):
    super().__init__(name_employee, age_employee, residence_employee)

    self.salary = salary
    self.position = position

  def description(self):
    super().description()
    print("Salary:", self.salary, "Position:", self.position)


Alex = Employee(4500, "Cyber security", "Alex", 32, "España")

Alex.description()

print(isinstance(Alex, Person))