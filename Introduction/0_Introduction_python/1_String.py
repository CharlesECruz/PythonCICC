"""
String
"""
# To use REGULAR EXPRESSION you've to use the library reg CHECK THE DOCUMENTATION
# Methods-> String as a class has also some methods like:
# 1. Capitalise -> change the fisrt letter
city = "vancouver"
print(city)
print(city.capitalize())
# 2. find -> return the index of the first coincidence
print(city.find("ver"))
print(city.find("x")) #if you try to find something tht does't exist it gonna return -1 (if you try with the method index it gonna return error)
# 3. count -> return the number of coincidences that had the string
print(city.count('v')) # you're looking for 'v' so you've 2 'v' in "vancouver"
# 4. in -> you looking if A contain B (B in A)
A = "hello world"
B = "hello"
print(B in A)


message = "Ahoy, \n ako sa mas? \n Ja som OK"
#slovak     Hi, how are you? I'm OK


name = "Carlos"
temp = 8.58746
message = "Hello, my name is %s and I live in %s and also the temp is %d " %(name,city, temp)
print(message)
# other way to tho this is
country= "Canada"
message2 = f"{country} is my current country"
print(message2)

temp2 = 8.58746
temperature = round(temp2,2)
print(temperature)
# otrher way to round a number this one don't use a method
print("The averaga point is %.1f"% temp2)


