import random
from player import Player

class Computer(Player):

    def __init__(self) -> None:
        super().__init__()
        pass

    def random_choice (self):
        comp_move = random.choice(self.move_list)



player_one = Computer(Player)

print(player_one.games_won)
print(player_one.move_list)
