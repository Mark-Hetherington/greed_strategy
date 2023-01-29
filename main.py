from game.round import play_round
from strategies.choose_d import ChoosePrimarilyDStrategy
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

strategy = ChoosePrimarilyDStrategy()
score = play_round(strategy)
logging.info(f"Scored {score}")