"""
Zortan is under attack!!! Thanos has arrived!
---------------------------------------------
Since Zortan is under attack, Louis calls his Avenger friends from earth.
Avengers receive his call and sends 4 avengers to save Zortan.
1. Ironman
4. Black Widow
2. Spiderman
3. Hulk
Each avenger has its attacking power and they have to fight Thanos
to save Zortan.
Avengers can attack only in pairs and get only 3 chances to kill Thanos,
or else Thanos will kill avengers and we loose the game.
"""
from typing import Final

IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life: int = 1500
choice: int = 0
attack_number: int = 0
WIN_MSG: Final[str] = "\n######  You successfully saved Zortan!!!  #####\n"
LOST_MSG: Final[str] = "\n#####  Thanos killed Avengers and captured Zortan!!  #####\n"
# declare helper messages
MSG = """
____________________________________________________________________
Zortan is under attack, choose the pairs no,. that will attack Thaos

1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman
____________________________________________________________________
"""

while True:
    if thanos_life <= 0 and attack_number <= 3:
        print(WIN_MSG)
        break
    elif attack_number >= 3:
        print(LOST_MSG)
        break
    print(MSG)
    choice = int(input("Enter your attack number: "))

    if choice ==1:
        print("Ironman & Black widow are attacking Thanos....")
        thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
    elif choice == 2:
        print("Black widow & spiderman are attacking Thanos....")
        thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
    elif choice == 3:
        print("Spiderman & Hulk are attacking Thanos....")
        thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
    elif choice == 4:
        print("Hulk & Ironman are attacking Thanos....")
        thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER

    attack_number += 1
    print(f"Thanos_life:{thanos_life}\nNumber of Attacks {attack_number}")
