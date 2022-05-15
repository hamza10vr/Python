
import random

user_guess = int (input("Guess a number: "))
number = random.randint(1,100)
print(number)

while user_guess != number:
    if user_guess > number:
        user_guess = int (input("please guess a lower number: "))
    else:
        user_guess = int (input("please guess a higher number: "))

print(f"you have guessed correctly, number was {user_guess} ")

