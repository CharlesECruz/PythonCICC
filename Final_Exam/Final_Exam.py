""" Final Exam V1 """
# please submit your python file upon completion.
def binary_search(l: list, target: int, start: int, end: int):
    """
    Write the binary search algorithm recursively without using loops.
    It returns location(index) of target in given list l[start:end] is present,
    otherwise return -1
​
    :param l: collection of elements
    :param target: element we are searching for
    :param start: start index for searching range
    :param end: end index for searching range
    :return: the index of target in the list or -1 (if target is not in the list)
    """
    # base
    if start <= end:
        middle = (start + end) // 2
        # base
        if l[middle] == target:
            return middle
        elif l[middle] > target:
            # recursion
            return binary_search(l, target, start, middle - 1)
        else:
            # recursion
            return binary_search(l, target, middle + 1, end)
    return -1
def reverse_vowels(s: str):
    """
    Write an algorithm to remove all vowels from a string without replace() built-in method.
    You can write iteratively or recursively.
​
    e.g.
    reverse_vowels("hello") -> "holle"
    reverse_vowels("world") -> "world"
    reverse_vowels("awihatu") -> "uwahita"
    reverse_vowels("hello world") -> "hollo werld"
    reverse_vowels("") -> ""
    reverse_vowels("a") -> "a"
​
    :param s: string
    :return: string with vowels in reversed order.
    """
    vowels = ["a", "e", "i", "o", "u","A","E","I","O","U"]
    changes = []
    for i in s:
        if i in vowels:
            changes.append(i)
    print(changes)
    word_answer = ""
    while len(changes) >= 1:
        for i in s:
            if i in vowels:
                # use of FILO to reverse
                word_answer += changes.pop()
            else:
                word_answer += i

    return word_answer


