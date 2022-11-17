"""
While traveling to Zortan, Louis packed lots of stuff. Let's see if he has anything that matches your favorite color.
"""

fav_color = input("Enter your favorite color: ")
print(fav_color)

match fav_color:
  case "black":
    print("Louis has a BLACK T-Shirt")
  case "red":
    print("Louis has a RED car")
  case "green":
    print("Louis has a GREEN T-Shirt")
  case _:
    print(f"Louis has nothing in {fav_color}")