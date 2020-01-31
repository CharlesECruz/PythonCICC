""" Guessing Game """
import random
def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    # your code goes here.
    start = 1
    end = 1000
    # print(answer)
    try:
        guess = int(input("Enter your guess for %d to %d: " % (start, end)))
    except ValueError as err:
        print(f"Invalid input: {err}")
        print("Enter a Number")
    counter = 0
    while answer != guess:
        counter += 1
        if guess < answer:
            start = guess
            print("Wrong! Guess count: %d" % counter)
        elif guess > answer:
            end = guess
            print("Wrong! Guess count: %d" % counter)
        guess = int(input("Enter your guess for %d to %d: " % (start, end)))
    print("You got it! The hidden number is %d" % answer)
pass
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    while True:
        guessing_game()