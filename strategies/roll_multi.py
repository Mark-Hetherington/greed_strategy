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

class TakeScoresAndDontRollAgainStrategy(PlayerStrategy):
    def select_dice_move(self, rolled_dice: List[DieRoll]) -> Tuple[List[DieRoll], bool]:
        rolled = rolled_dice.copy()
        selected_dice = []
        for score in SCORE_PRIORITY:
            if rolled_dice.count(score[0]) >= score[1]:
                selected_dice.extend([score[0]] * score[1])
                for _ in range(score[1]):
                    rolled.remove(score[0])
        for die in rolled:            
            if die in [DieRoll.diamond, DieRoll.gold]:
                selected_dice.append(die)
        return selected_dice, False

class TakeScoresAndAlwaysRollAgainStrategy(PlayerStrategy):
    def select_dice_move(self, rolled_dice: List[DieRoll]) -> Tuple[List[DieRoll], bool]:
        rolled = rolled_dice.copy()
        selected_dice = []
        for score in SCORE_PRIORITY:
            if rolled_dice.count(score[0]) > score[1]:
                selected_dice.extend([score[0]] * score[1])
                for _ in range(score[1]):
                    rolled.remove(score[0])
        for die in rolled:            
            if die in [DieRoll.diamond, DieRoll.gold]:
                selected_dice.append(die)
        return selected_dice, True

class TakeScoresAndRollAtLeastThreeAgainStrategy(PlayerStrategy):
    def select_dice_move(self, rolled_dice: List[DieRoll]) -> Tuple[List[DieRoll], bool]:
        rolled = rolled_dice.copy()
        selected_dice = []
        for score in SCORE_PRIORITY:
            if rolled_dice.count(score[0]) > score[1]:
                selected_dice.extend([score[0]] * score[1])
                for _ in range(score[1]):
                    rolled.remove(score[0])
        for die in rolled:            
            if die in [DieRoll.diamond, DieRoll.gold]:
                selected_dice.append(die)
                rolled.remove(die)
        return selected_dice, len(rolled) >= 3