""" Primes, GCD, LCM """
import math

def is_prime(num):
    """ Check if n is prime """
    if num <= 1:
        return  False
    for i in range(2,int(math.sqrt(num))+1):
        if num% i == 0:
            return  False
    return True


def gcd(a, b):
    """ GCD of a and b """
    if b == 0:
        return a
    else:
        return gcd(b,a % b)


def lcm(a, b):
    """ LCM of a and b """
    if a>b:
        maximum = a
    else:
        maximum = b
    while True:
        if maximum % a ==0 and maximum % b ==0:
            return maximum
        else:
            maximum += 1



def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    a = []
    for i in range(0,n + 1):
        if is_prime(i):
            a.append(i)
    return a
