def gcd(a:int, b:int):
    """ GCD of a and b """
    #print(a,b)
    if b == 0:
        return a
    else:
        return gcd(b,a % b)
number =gcd(24, 18)
print(number)