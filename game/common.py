from enum import Enum
from collections import Counter
from typing import List, Tuple

class InvalidMoveError(Exception):
    pass

class DieRoll(Enum):
    silver = "$"
    gold = "g"
    ruby = "r"
    ebony = "e"
    emerald = "E"
    diamond = "d"

def validate_selected_dice(roll: List[DieRoll], selection: List[DieRoll], rolling_again:bool):
    remaining_dice = roll.copy()
    for selected in selection:
        try:
            remaining_dice.remove(selected)
        except ValueError:
            raise InvalidMoveError(f"Could not find {selection} in remaining dice {remaining_dice} from roll {roll}")
    
    if not rolling_again and (DieRoll.diamond in remaining_dice or DieRoll.gold in remaining_dice):
        raise InvalidMoveError("You must select all scoring dice on your last roll.")


