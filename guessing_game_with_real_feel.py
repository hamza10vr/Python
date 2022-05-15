user_guess = int (input("Guess a number: "))
number = 5

while user_guess != number:
    user_guess = int (input("please guess again: "))

print(f"you have guessed correctly, number was {user_guess} ")

