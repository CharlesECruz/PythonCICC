""" Guessing Game """
import random


def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    print(answer)
    found= False
    start =1
    end = 1000
    guess_count = 0
    while not found:
        try:
            guess_number = int(input("Enter your guess from %d to %d \n"%(start,end)))
        except ValueError as e:
            print(f"Invalid input:{e}")
            print("Please enter a number!!! The hidden number was changed")
        if guess_number != answer:
            guess_count +=1
            if guess_number< answer:
                start = guess_number+1
            else:
                end = guess_number-1
            print("Wrong!!! Guess count: %d"% guess_count)
        else:
            print("YOU ROCK!!! The hidden number is %d" %answer)
            print("It took you %d guess(es)"%guess_count)
            found = True
            break

    pass


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()



