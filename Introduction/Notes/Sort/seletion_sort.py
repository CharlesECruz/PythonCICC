items =[3,12,30,5,6,7,1,2,3,11]
def selection_sort(items):
    steps=0
    for scan in range(len(items)-1):
        min_index=scan
        for i in range(scan+1,len(items)):
            steps += 1
            if items[i]<items[min_index]:
                min_index=i
        if min_index != scan:
            items[scan],items[min_index] = items[min_index],items[scan]
    return steps
print(selection_sort(items))
print(items)