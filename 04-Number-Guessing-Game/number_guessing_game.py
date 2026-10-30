
import random

print("==============================")
print("     NUMBER GUESSING GAME     ")
print("==============================")

# The computer chooses a random number
secret_number = random.randint(1, 100)

attempts = 0

print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")

while True:

    guess = int(input("Enter your guess: "))

    attempts = attempts + 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("Congratulations! You guessed the number!")
        print("The secret number was:", secret_number)
        print("Number of attempts:", attempts)
        break

print("Thanks for playing!")
