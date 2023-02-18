import random
from player import Player

class Computer(Player):

    def __init__(self) -> None:
        super().__init__()
        pass

    def random_choice (self):
        choice = random.choice(self.move_list)
