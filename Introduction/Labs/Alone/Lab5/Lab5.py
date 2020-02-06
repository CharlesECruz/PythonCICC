""" Sorting Practice Problems """
def bubble_sort(items):
    for scan in range(len(items)):
        swapped = False
        for j in range(len(items) - 1 - scan):
            if items[j] > items[j + 1]:
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
                #temp = alist[j]
                #alist[j] = alist[j + 1]
                #alist[j + 1] = temp

        if not swapped:
            break
# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.


def sort_half(alist):
    middle = len(alist) // 2
    a = alist[:middle]
    b = alist[middle:]
    bubble_sort(a)
    bubble_sort(b)
    b.reverse()
    return a.__add__(b)


# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    new_list=[]
    new_list=A
    new_list.extend(B)
    bubble_sort(new_list)
    return new_list


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    newlist=[]
    for i in mylist:
        if i >0:
            newlist.append(i)
        else:
            newlist.append(0)
    return newlist