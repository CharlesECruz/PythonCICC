""" Group Lab 2 (in-class) Exhaustive search, Back Tracking """

def permutation_helper(word: str):
    # base case
    if len(word) == 1:
        return word
    # recursion case
    else:
        new_list = [] # temp list
        for i in range(len(word)):
            part = word[:i] + word[i + 1:]
            for j in permutation_helper(part):
                new_list.append(word[i:i + 1] + j)
        return new_list
def permutation(word: str):
    """
    Write a recursive function permutation that accepts a string as a parameter
    and outputs all possible rearrangements of the letters in the string.
    The arrangements may be output in any order.
    example)
    permutation("park")
    output: park, pakr, pkar, prak, arpk, aprk, akrp, ...
    :param word: word to permute
    :return: display permutations of a given word
    """
    answer =[]
    letter = ""
    answer = permutation_helper(word)
    for i in answer[:-1]:
        letter += (i+",")
    print(letter[:-1])
permutation('park')
def additon(a, sum, j):
    """
    it's a help function that look how many ways we have to sum a dice
    :param a: the number of dice
    :param sum: desired sum
    :param j: desired sum (like global variable)
    :return: display all possible ways as String
    """
    if a == 0:
        return ""
    if sum < 0 or 6 * a < sum or a > sum:
        return ""
    answer = ""
    for i in range(1, 7):
        if i + sum == j:
            return "{" + str(i) + "," + str(sum) + "},"
        answer += additon(a - 1, sum - i, j)
    return answer
def sum_of_dice(dice: int, desired_sum: int):
    """
    Prints all possible outcomes of rolling the given number of six-sided dice
    that add up to the given desired sum, in {#, #, #} format.
    :param dice: the number of dice
    :param desired_sum: desired sum
    :return: display all possible ways
    example)
    sum_of_dice(2, 7)
    output: {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 1}
    """
    answer = additon(dice,desired_sum,desired_sum)
    print(answer[:-1])
sum_of_dice(2,7)