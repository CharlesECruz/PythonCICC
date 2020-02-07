""" Bonus Question """
def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1
def gcd_of_strings(str1: str, str2: str):
    """
    For strings S and T, we say "T divides S" if and only if S = T + ... + T
    (T concatenated with itself 1 or more times)
​
    return the largest string that divides both str1 and str2.
​
    e.g.
    gcd_of_strings("ABCABC", "ABC") -> "ABC"
    gcd_of_strings("ABABAB", "ABAB") -> "AB"
    gcd_of_strings("LAMP", "CODE") -> ""
​
    :param str1: string.
    :param str2: string.
    :return: the largest string that divides str1 and str2.
    """
    count = 0
    target = "" # it's the largest string
    if str1.count(str2):
        if len(str1) > len(str2):
            mainword = str2
        else:
            mainword = str1
        for i in mainword:
            target += i
            if str1.count(target)< count:
                return target[:-1]
            else:
                count = str1.count(target)
        return target
    else:
        return ""

print(gcd_of_strings("ABCABC", "ABC"))# -> "ABC"
print(gcd_of_strings("ABABAB", "ABAB"))# -> "AB"
print(gcd_of_strings("LAMP", "CODE")) # -> ""
