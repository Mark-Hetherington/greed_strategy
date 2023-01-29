from abc import ABC, abstractmethod
from typing import List, Tuple

from game.common import DieRoll


class PlayerStrategy(ABC):
    @abstractmethod
    def select_dice_move(self, rolled_dice: List[DieRoll]) -> Tuple[List[DieRoll], bool]:
        pass
