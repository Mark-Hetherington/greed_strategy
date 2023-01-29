from typing import List, Tuple
from game.common import DieRoll
from strategies.base import PlayerStrategy


class ChooseOnlyDStrategy(PlayerStrategy):
    def select_dice_move(self, rolled_dice: List[DieRoll]) -> Tuple[List[DieRoll], bool]:
        selected_dice = []
        for die in rolled_dice:
            if die == DieRoll.diamond:
                selected_dice.append(die)
        return selected_dice, False

class ChoosePrimarilyDStrategy(PlayerStrategy):
    def select_dice_move(self, rolled_dice: List[DieRoll]) -> Tuple[List[DieRoll], bool]:
        selected_dice = []
        for die in rolled_dice:
            if die == DieRoll.diamond:
                selected_dice.append(die)
        if not selected_dice:
            for die in rolled_dice:
                if die == DieRoll.gold:
                    selected_dice.append(die)
                    break
        return selected_dice, False