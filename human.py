from player import Player

class Human(Player):

    def __init__(self) -> None:
        super().__init__()
        pass

    def move_choice(self):
        input(f'Which move would you like to perform?')



human_player_one = Human()

human_player_one.move_choice()