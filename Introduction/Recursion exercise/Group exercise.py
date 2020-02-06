# Write a recursive function printBinary that accepts integer and
# prints that number's representation in binary (base 2)
#
# Examples:
# print_binary(2)    prints 10
# print_binary(7)    prints 111
# print_binary(12)   prints 1100
# print_binary(42)   prints 101010
# print_binary(-500) prints -111110100
def print_binary(num):
    if num < 0:
        return "-" + print_binary(num * -1)
    # base case
    if num == 0:
        return ""
    #
    if num % 2 == 0:
        return print_binary(num // 2) + "0"
    else:
        return print_binary(num // 2) + "1"


# print(print_binary(-500))


# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 10 to 99 (two digits)
# print_decimal(3)  prints from 100 to 999 (three digits)
def print_decimal(digits):
    end = 10 ** digits
    start = 10 ** (digits - 1)
    if digits == 1:
        print("0")
    for _ in range(start, end):
        print(_)
    pass


# print_decimal(2)
