from collections import Counter
from typing import List, Tuple

from game.common import DieRoll

of_a_kind_scores = [
    (DieRoll.silver, 3, 600),
    (DieRoll.gold, 3, 500),
    (DieRoll.ruby, 3, 400),
    (DieRoll.ebony, 3, 300),
    (DieRoll.emerald, 3, 300),
    (DieRoll.diamond, 4, 1000)
]


def has_six_of_a_kind(dice: List[DieRoll]) -> Tuple[int, List[DieRoll]]:
    """ If six of a kind is rolled, it is worth 5,000 points """
    if len(dice) < 6:
        return 0, dice
    for die in dice:
        if die != dice[0]:
            return 0, dice
    return 5000, []
        

def has_greed(dice: List[DieRoll]) -> Tuple[int, List[DieRoll]]:
    """ If one of each die face is rolled it is worth 1,000 points """
    for face in [DieRoll.silver, DieRoll.gold, DieRoll.ruby, DieRoll.ebony, DieRoll.emerald, DieRoll.diamond]:
        if face not in dice:
            return 0, dice
    return 1000, []


def calculate_of_a_kind_score(dice: List[DieRoll]) -> Tuple[int, List[DieRoll]]:
    remaining_dice = dice.copy()
    counts = Counter(dice)
    score = 0
    for key, count in counts.items():
        _, kind_score_threshold, kind_score_value = next(kind for kind in of_a_kind_scores if kind[0] == key)
        if count >= kind_score_threshold:
            # Set aside the matching dice
            for _ in range(count):
                remaining_dice.remove(key)
            score += kind_score_value
    return score, remaining_dice

def individual_dice_score(dice: List[DieRoll]) -> Tuple[int, List[DieRoll]]:
    remaining_dice = []
    score = 0
    for die in dice:
        if die == DieRoll.diamond:
            score += 100
        elif die == DieRoll.gold:
            score += 50
        else:
            remaining_dice.append(die)
    return score, remaining_dice

def calculate_score(dice: List[DieRoll]):
    """ Given a list of dice that are to be set aside, calculate the score """    
    score = 0
    remaining_dice = dice.copy()
    for score_possibility in [has_six_of_a_kind, has_greed, calculate_of_a_kind_score, individual_dice_score]:
        if remaining_dice:
            combo_score, remaining_dice = score_possibility(remaining_dice)
            score += combo_score
    return score
