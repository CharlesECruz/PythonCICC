items =[3,12,30,5,6,7,1,2,3,11]
def bubble_sort(items):
    steps = 0
    for scan in range(len(items)):
        swapped = False
        for j in range(len(items) - 1 - scan):
            steps += 1
            if items[j] > items[j + 1]:
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
                #temp = alist[j]
                #alist[j] = alist[j + 1]
                #alist[j + 1] = temp

        if not swapped:
            break

    print("steps:", steps)
bubble_sort(items)
print(items)