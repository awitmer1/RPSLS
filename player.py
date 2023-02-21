import random

class Player():

    def __init__(self) -> None:
        self.games_won = 0
        self.move_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass

    def throw(self):
        player_throw = input("What move would you like to perform?")
        print(f'Player throws {player_throw}')
        return player_throw
    
    def ruleset (player_throw):
            if player_throw == "Rock" and input == "Paper":

                


player_one = Player()
opponent = Player()

print(player_one.games_won)
print(player_one.move_list)
player_one.throw()
print("Testing")



