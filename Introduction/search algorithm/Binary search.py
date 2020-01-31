items=[1, 2, 3, 4, 5, 6]
def binary_search(items, target):
    start = 0
    end = len(items) - 1
    while start<=end:
        middle= (start+end)//2
        if target == items[middle]:
            return middle
        elif target< items[middle]:
            end = middle - 1
        elif target > items[middle]:
            start = middle + 1

    return -1
print(binary_search(items, 5))