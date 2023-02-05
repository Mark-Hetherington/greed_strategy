import matplotlib.pyplot as plt

from game.round import play_round
from strategies.choose_d import ChoosePrimarilyDStrategy
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

strategy = ChoosePrimarilyDStrategy()
scores = []
for i in range(1000):
    score = play_round(strategy)
    scores.append(score)
    logging.info(f"Scored {score}")

plt.hist(scores, bins=10)
plt.show()