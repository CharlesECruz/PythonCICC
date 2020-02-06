# Bubble Sort - "Bubbling" the largest element to the right!
# (pseudo-code)
# list = [...]
# for each i from 1 to len(list)
#     compare two adjacent elements
#     if the first element is greater than the second element
#         swap two elements

# Time Complexity
# O(n^2) algorithm


def bubble_sort(alist):
    steps = 0
    for scan in range(len(alist)):
        swapped = False
        for j in range(len(alist) - 1 - scan):
            steps += 1
            if alist[j] > alist[j+1]:
                # alist[j], alist[j+1] = alist[j+1], alist[j]
                swapped = True
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

        if not swapped:
            break

    print("steps:", steps)

a =[3,12,30,5,6,7,1,2,3,11]

bubble_sort(a)
print(a)