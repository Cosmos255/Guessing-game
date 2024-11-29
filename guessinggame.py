import random


print(f"Python Number Guessing game ")


guessses = 0

is_running = True


lowest_num = int(input(f"What is the lowest num "))
highest_num = int(input(f"What is you highest num "))


def questions():
    global lowest_num
    global highest_num
    lowest_num = int(input(f"What is the lowest num "))
    highest_num = int(input(f"What is you highest num "))


answer = random.randint(lowest_num, highest_num)

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guessses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"The number is out of range the range is {lowest_num} to {highest_num}")
        elif guess < answer:
            print(f"Too low! Try again!")
        elif guess > answer:
            print(f"Too high! Try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses {guessses}")
            is_running = False

    else:
        print("Invalid guess")
        questions()
