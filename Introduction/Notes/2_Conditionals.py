working = True


def continue_working():
    value = int(input("Would you like continue?(write 1 to ""yes"" and 2 to ""no"")"))
    switcher = {
        1: True,
        2: False
    }
    return switcher.get(value, "Invalid input")


while continue_working():
    age = int(input("Enter your age: "))

    if age >= 21:
        print("you can drink")
    elif 13 <= age <= 21:
        print("study hard")

    else:
        print("play videogames")
print("End of the program")