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


def additon(a, sum,j):

    if a == 0:
        return sum == 0
    if sum < 0 or 6*a < sum or a > sum:
        return 0
    answer = 0
    for i in range(1,7):
        if i+sum == j:
            print(i,sum)
        answer += additon(a-1, sum - i,j)
    return answer
print(additon(2,7,7))