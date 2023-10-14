import random
import math

while True:
    lower = int(input("Enter Lower bound: "))
    upper = int(input("Enter Upper bound: "))

    x = random.randint(lower, upper)
    print("\nYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

    count = 0

    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input("Guess a number: "))

        if x == guess:
            print("Congratulations you did it in ", count, " tries")
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You guessed too high!")

    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("Better Luck Next time!")

    play_again = input("\nGenerate another Game? (yes/y or no/n): ")
    if play_again.lower() not in ["yes", "y"]:
        break
    