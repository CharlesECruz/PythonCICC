""" group exercises 2 """
# Write a recursive function printBinary that accepts integer and
# prints that number's representation in binary (base 2)
#
# Examples:
# print_binary(2)    prints 10
# print_binary(7)    prints 111
# print_binary(12)   prints 1100
# print_binary(42)   prints 101010
# print_binary(-500) prints -111110100
# add one more digit to what we have so far
# 0 --> 0 00
# 1 --> 0 01
# 2 --> 0 10
# 3 --> 0 11
# 4 --> 1 00
# 5 --> 1 01
# 6 --> 1 10
# 7 --> 1 11
def print_binary(num):
    if num < 0:
        return  "-" + print_binary(num*-1)
    if num == 0:
        return ""
    #
    if num % 2 == 0:
        return print_binary(num//2) + "0"
    else:
        return print_binary(num//2) + "1"
print(print_binary(-500))
# Write a recursive function evaluate that accepts a string
# representing a math expression and computes its value.
# - The expression will be "fully parenthesized" and will
#   consist of + and * on single-digit integers only.
# - You can use a helper function. (Do not change the original function header)
# - Recursion
#
# evaluate("7")                 -> 7
# evaluate("(2+2)"              -> 4
# evaluate("(1+(2*4))"          -> 9
# evaluate("((1+3)+((1+2)*5))") -> 19
def evaluate_helper(expr: str, i: int):
    if expr[i].isdigit():
        return int(expr[i]), i
    else:
        i += 1
        left, i = evaluate_helper(expr, i)
        i += 1
        op = expr[i]
        i += 1
        right, i = evaluate_helper(expr, i)
        i += 1
        if op == "+":
            return left + right, i
        else:
            return left * right, i
def evaluate(expr: str):
    res = evaluate_helper(expr, 0)
    return res[0]
print(evaluate("7"))
print(evaluate("((1+3)+((1+2)*5))"))
# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 10 to 99 (two digits)
# print_decimal(3)  prints from 100 to 999 (three digits)
def print_decimal(digits):
    end = 10**digits
    start = 10**(digits-1)
    if digits == 1:
        print("0")
    for _ in range(start, end):
        print(_)
print_decimal(1)