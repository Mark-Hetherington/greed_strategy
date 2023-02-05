import logging
from random import choice
from typing import List
from game.common import DieRoll, validate_selected_dice
from game.scoring import calculate_score
from strategies.base import PlayerStrategy


def roll_dice(number_of_dice: int) -> List[DieRoll]:
    return [
        choice(list(DieRoll)) for _ in range(number_of_dice)
    ]

def play_round(player: PlayerStrategy) -> int:
    roll_again = True
    number_of_dice = 6
    round_score = 0
    while roll_again:
        rolled_dice = roll_dice(number_of_dice=number_of_dice)
        logging.info(f"Rolled {rolled_dice}")
        selected_dice, roll_again = player.select_dice_move(rolled_dice=rolled_dice)
        logging.info(f"Selected {selected_dice}, and rolling again is {roll_again}")
        validate_selected_dice(roll=rolled_dice, selection=selected_dice, rolling_again=roll_again)
        move_score = calculate_score(dice=selected_dice)
        if move_score == 0:
            logging.info("Score for this roll was zero, round scores zero")
            return 0
        round_score += move_score
    return round_score
            