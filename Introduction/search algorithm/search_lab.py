# In this lab, you will be using two searching algorithms we covered in class to
# search for a word in dictionary. Compare the performance for each algorithm.
# You will have to output the number of steps for both algorithms when used for searching
# for the same word. (case-insensitive)
# Your output should look like this. Try to search for 5 different words of your choice.
#
# ex)
# Searching for "orange"...
# Linear Search: {} steps
# Binary Search: {} steps
#
# Searching for "orangeeeeee"...
# Linear Search: no matching word found
# Binary Search: no matching word found


# Open the dictionary file and read all lines as a list of words.
with open('words') as f:
    lines = f.readlines()

# Strip off the newline character for each word.
lines = [line.strip() for line in lines]

print(lines)

def binary_search(items, target):
    steps = 0
    start = 0
    end = len(items)-1
    while start<=end:
        middle= (start+end)//2
        print(target,items[middle])
        if target == items[middle]:
            return middle,steps
        elif target< items[middle]:
            end = middle-1
        else:
            start = middle+1
        print(start,end)
        steps +=1
    return -1,steps



def linear_search(items,target):
    step = 0
    for i in items:
        if target == i:
            return step,step
        step += 1
    return step,step

search = input("word to search: ")
print("Looking for :",search)
print("Binary search: (index, steps) ",binary_search(lines,search))
print("Linear search: (index, steps) ",linear_search(lines,search))
