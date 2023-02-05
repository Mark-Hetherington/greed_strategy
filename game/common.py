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


