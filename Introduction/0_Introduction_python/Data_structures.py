"""
MATRIX
"""
A=[[1,2],[3,4]]
print(A)
for x in range(2):
    for y in range(2):
        print(A[x][y])
A[1][1] = 0
print(A)
"""
WHAT ABOUT THE MAPS

In python we don't have maps we use dictionary to meet it... it's the same 

"""
country = {"Name":"Canada","pupulation": 10000}
dictionary_Example = {1: "Stuff", 2:country}
print(dictionary_Example)
# the key of this map it's the first value that's means that in our current map the keys are 1,2
print(dictionary_Example.get(2))   # tha value for the key 2 is the country dictionary
# how to add a new entry in the dictionary
dictionary_Example["poperty"] = {"name": "Colombia", "population":5000}
print(dictionary_Example)
print("next methods")
print(dictionary_Example.fromkeys())
"""
Vectors
"""
# to made vectors we use np.array it is the same array or list work with the same logic

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print("sort a list/array")
print(cars)