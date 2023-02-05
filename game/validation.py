from typing import List

from game.common import DieRoll, InvalidMoveError
from game.scoring import calculate_score


def validate_selected_dice(roll: List[DieRoll], selection: List[DieRoll], rolling_again:bool):
    print(f"Selected {selection}")
    remaining_dice = roll.copy()
    for selected in selection:
        try:
            remaining_dice.remove(selected)
        except ValueError:
            raise InvalidMoveError(f"Could not find {selection} in remaining dice {remaining_dice} from roll {roll}")
    
    if not rolling_again and (DieRoll.diamond in remaining_dice or DieRoll.gold in remaining_dice):
        raise InvalidMoveError(f"You must select all scoring dice on your last roll. {remaining_dice}")
    if not rolling_again and calculate_score(remaining_dice):        
        raise InvalidMoveError(f"You must select all scoring dice on your last roll. {remaining_dice}")