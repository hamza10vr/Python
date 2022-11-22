"""
Save Zortan:
------------

The war has just intensified, Thanos army has reached Zortan and are going to
fight along with him. With his army, this time Thanos is going to atttack Avengers
and the battler is going to be intense!!!

Since, everything is going in real-time, we don't have control over character,
instead our character will choose their own fight

this time each character get its own structure and defined parameters, so as you
can see our code getting better and certainly we are going to make is awesome
as we progress with future modules.
"""
#A special typing construct to indicate to type checkers that a name cannot be re-assigned or overridden in a subclass.
from typing import Final
from random import randint

#Typing alias
Character = dict[str, str | int]

#Superheros
IRONMAN: Final[Character] = {"name": "Ironman", "attack_power": 250, "life": 1000}
BLACKWIDOW: Final[Character] = {"name": "BlackWidow", "attack_power": 180, "life": 800}
SPIDERMAN: Final[Character] = {"name": "Spiderman", "attack_power": 190, "life": 700}
HULK: Final[Character] = {"name": "Hulk", "attack_power": 300, "life": 1100}

#Super Villains
THANOS: Final[Character] = {"name": "thanos", "attack_power": 1500, "life": 1500 }
REDSKULL: Final[Character] = {"name": "Redskull", "attack_power": 300, "life": 800 }
PROXIMA: Final[Character] = {"name": "Proxima", "attack_power": 320, "life": 800 }

# All Super Heros & Super Villains
superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
supervillains: list[Character] = [THANOS, REDSKULL, PROXIMA]

#Helper Variables
choice: int = 0
attack_number: int = 0
WIN_MSG: Final[str] = "\n######  You successfully saved Zortan!!!  #####\n"
LOST_MSG: Final[str] = "\n#####  Thanos killed Avengers and captured Zortan!!  #####\n"

#logic for creating attack
for attack in range(3):
    # each iteration get a new hero & villain
    hero_index = randint(0,3)
    villain_index = randint(0,2)
    # helper variables
    current_superhero = superheros[hero_index]
    current_supervillain = supervillains[villain_index]

    print(f"Attack: {attack + 1} => {current_superhero['name']} is going to fight with {current_supervillain['name']} ")