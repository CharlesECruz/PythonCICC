# Tuples can not  add(append),change(replace) or delete

# Tuples are Immutavle lists
vowels = ("a","e","i","o","u")

# 1. you can return a tuple as a value from a function

def a():
    return 1,"Mark" #Tuple (here the parenthesis is optional)

# 2. check if an item is in a tuple

print("a" in vowels)
print("k" in vowels)

# 3. multiple assignments

year, country = (2020, "Canada")
print(year)
print(country)

x = 10
y = 20
print(x,y)
#you can swap it!!!
x,y = y,x
print(x,y)
