import random
from player import Player

class Computer(Player):

    def __init__(self) -> None:
        super().__init__()
        pass

    def throw (self):
        comp_move = random.choice(self.move_list)
        self.chosen_move = comp_move
        print(f'Computer throws {comp_move}\n')
        return comp_move
