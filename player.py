

class Player():

    def __init__(self) -> None:
        self.games_won = 0
        self.move_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass

    def throw(self):
        player_throw = input("What move would you like to perform?")
        print(f'Player throws {player_throw}')
        


# player_one = Player()
# opponent = Player()

# print(player_one.games_won)
# print(player_one.move_list)
# player_one.throw()
# print("Testing")



