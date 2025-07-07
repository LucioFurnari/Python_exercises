def generateOddsFunction(limit):
  num=1

  listOdd=[]

  while num <= limit:
    listOdd.append(num*2)
    num+=1

  return listOdd

# newList = generateOddsFunction(5)

# print(newList)

def generatorOdds(limit):
  num=1
  while num<limit:
    yield num*2
    num+=1

# newList2 = generatorOdds(5)
# for num in newList2:
#   print(num)

def get_cities(*cities):
  for elem in cities:
    yield elem

cities_list = get_cities("Madrid", "Argentina", "Chile")
print(next(cities_list))
print(next(cities_list))