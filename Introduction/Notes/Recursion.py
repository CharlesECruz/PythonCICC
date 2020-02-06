# it's call the function by itself

def factorial_recur(n):
    if n != 0:
        return n * factorial_recur(n - 1)
    else:
        return 1


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def power(base,n):
    if n == 0:
        return 1
    else:
        return base*power(base,n-1)
def triple_steps(n):
    """
    A child is running up a staircase with n steps and can hop
    either 1 step, 2 steps, or 3 steps at a time.
    Count how many possible ways the child can run up the stairs.
    :param n: the number of stairs
    :return: The number of possible ways the child can run up the stairs.
    """
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return triple_steps(n - 3) + triple_steps(n - 2) + triple_steps(n - 1)

# print(factorial_recur(8))
# print(fibonacci(7))
# print(power(5,2))
# The function below take a long time to finish it
# print(triple_steps(30))