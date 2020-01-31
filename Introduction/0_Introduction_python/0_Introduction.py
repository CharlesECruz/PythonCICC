# this is the way to comment in python (just the line)
# 1. 10//3 it's gonna give you a int the // always divide and take the integer
# ** (power),* times
# leetcode.com
"""
this is like we comment in block in python
"""
"""
def plus(nume, num2):
    return int(nume + num2)


words = ['cat', 'window', 'defenestrate']
for x in range(2, 4):
    print(x)
print("Firs loop")
numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10]
for num in range(0,len(numbers),2):
    print(num)
print("Secont loop")
for i in range(0,20,2):
    print(i)"""

# method in strings!!!
address = "192.168.1.0"
ret = ""
print(address.replace('.',"[.]")) # find the substring and change for new one... in this example you change all '.' to '[.]'

# index in string <str> example
actor = "Will Smith"
print(actor[0:4])
print(actor[2:6])
print(actor[-3:-1])

# short cut
# if I don't put the start we gonna take the start in 0

print(actor[:]) # this take all the characters from the first one to the last one
print(actor[:5]) # from 0 to 5

#take in  mind
# string are immutable  you can't change a single little if you  
