import random

class Player():

    def __init__(self) -> None:
        self.games_won = 0
        self.move_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass


player_one = Player()

print(player_one.games_won)
print(player_one.move_list)

choice = random.choice(player_one.move_list)
print(choice)