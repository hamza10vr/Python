#----------------------------------------------
# Introducing `Type Hinting` - Optional Static type Checking in Python Using `Mypy`
# pip install mypy
#-----------------------------------------------

food :str = "Milk"
print(f"Louis is going to drink: {food}")

food = "eggs"
print(f"Louis is going to eat: {food}")

food = 10 # BUG: show up as warning but the code sill works b/c python is dynamic typing
print(f"Louis is going to drink: {food}")