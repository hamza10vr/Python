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

