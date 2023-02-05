from typing import List, Tuple
from game.common import DieRoll
from strategies.base import PlayerStrategy


SCORE_PRIORITY = [
    (DieRoll.diamond, 4),
    (DieRoll.silver, 3),
    (DieRoll.ruby, 3),
    (DieRoll.ebony, 3),
    (DieRoll.emerald, 3)
]

class TakeAtLeastOneStrategy(PlayerStrategy):
    def select_dice_move(self, rolled_dice: List[DieRoll]) -> Tuple[List[DieRoll], bool]:
        selected_dice = []
        for score in SCORE_PRIORITY:
            if rolled_dice.count(score[0]) > score[1]:
                return [score[0]] * score[1], False
        for die in rolled_dice:            
            if die in [DieRoll.diamond, DieRoll.gold]:
                return [die], False
        return [], False