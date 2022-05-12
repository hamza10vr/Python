
import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = " "

if fortune_number == 1:
    fortune_text = "You will have a great day"
if fortune_number == 2:
    fortune_text = "Today will be tough... but worth it"
if fortune_number == 3:
    fortune_text = "You will get married this year"    

print(f"{fortune_text} your lucky number is {lucky_number}")

light_is_on = False

if light_is_on:
    print("Ligh is on")
    print("statement was set to True")
else:
    print("light is off")

weight = 190.4

if weight < 190.5 :
    print(f"you're weight is, {weight} , which is under weight :)")



print(random.randint(1,10))
print(random.random())


answer = random.randint(1,3)

if answer == 1:
    print ("YES!")
if answer == 2:
    print("NO")
if answer == 3:
    print("Maybe")




