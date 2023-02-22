from player import Player

class Human(Player):

    def __init__(self) -> None:
        super().__init__()
        pass


    def throw(self):
        index = 0
        for move in self.move_list:
            print(f'{index}:{move}')
            index += 1
        user_input = int(input("Select number corelating to move: "))

        self.choosen_move = self.move_list[user_input]
        print(f" you have choosen {self.choosen_move}")



# human_player_one = Human()

# print(human_player_one.games_won)
# human_player_one.throw()
# print("Testing")