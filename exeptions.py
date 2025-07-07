def evaluateAge(age):
  if age < 0:
    raise ValueError("The age can't be negative")

  if age < 20:
    return "You are to young"
  elif age < 40:
    return "You are young"
  elif age < 65:
    return "You are old"
  elif age < 100:
    return "You are to old"
  

try:
  print(evaluateAge(-15))
except ValueError as Error:
  print(Error)