from human import Human
from computer import Computer



class Game():

    def __init__(self) -> None:
        self.player_one = None
        self.player_two = None

    def choose_game_type(self):
        user_input = input("PVP or PVAI?")
        if user_input == 'PVP':
            self.player_one = Human()
            self.player_two = Human()
        elif user_input == "PVAI":
            self.player_one = Human()
            self.player_two = Computer()


    # def test_logic(self):
    #     while self.player_one.games_won <2 and self.player_two.games_won <2:
    #         self.player_one.throw()
    #         self.player_two.throw()
    #         if self.player_one.choosen_move == 'Rock' and self.player_two.choosen_move == 'Paper':
    #             self.player_two.games_won += 1


    def display_rules (self):
        pass

    def run_game (self):
        while self.player_one.games_won < 2 and self.player_two.games_won < 2:
            
            self.player_one.throw()
            self.player_two.throw()

            ### Rock Crushes Scissors ###
            if self.player_one.choosen_move == "Rock" and self.player_two.choosen_move == "Scissors":
                self.player_one.games_won += 1
                print(f'Rock crushes Scissors - Player one wins the round!')
            elif self.player_two.choosen_move == "Rock" and self.player_one.choosen_move == "Scissors":
                self.player_two.games_won += 1
                print(f'Rock crushes Scissors - Player two wins the round!')

            ### Scissors cut Paper ###
            elif self.player_one.choosen_move == "Scissors" and self.player_two.choosen_move == "Paper":
                self.player_one.games_won += 1
                print(f'Scissors cut Paper - Player one wins the round!')
            elif self.player_two.choosen_move == "Scissors" and self.player_one.choosen_move == "Paper":
                self.player_two.games_won += 1
                print(f'Scissors cut Paper - Player two wins the round!')

            ### Paper covers Rock ###
            elif self.player_one.choosen_move == "Paper" and self.player_two.choosen_move == "Rock":
                self.player_one.games_won += 1
                print(f'Paper covers Rock - Player one wins the round!')
            elif self.player_two.choosen_move == "Paper" and self.player_one.choosen_move == "Rock":
                self.player_two.games_won += 1
                print(f'Paper covers Rock - Player two wins the round!')

            ### Rock crushes Lizard ###
            elif self.player_one.choosen_move == "Rock" and self.player_two.choosen_move == "Lizard":
                self.player_one.games_won += 1
                print(f'Rock crushes Lizard - Player one wins the round!')
            elif self.player_two.choosen_move == "Rock" and self.player_one.choosen_move == "Lizard":
                self.player_two.games_won += 1
                print(f'Rock crushes Lizard - Player two wins the round!')

            ### Lizard poisons Spock ###
            elif self.player_one.choosen_move == "Lizard" and self.player_two.choosen_move == "Spock":
                self.player_one.games_won += 1
                print(f'Lizard poisons Spock - Player one wins the round!')
            elif self.player_two.choosen_move == "Lizard" and self.player_one.choosen_move == "Spock":
                self.player_two.games_won += 1
                print(f'Lizard poisons Spock - Player two wins the round!')

            ### Spock smashes Scissors ###
            elif self.player_one.choosen_move == "Spock" and self.player_two.choosen_move == "Scissors":
                self.player_one.games_won += 1
                print(f'Spock smashes Scissors - Player one wins the round!')
            elif self.player_two.choosen_move == "Spock" and self.player_one.choosen_move == "Scissors":
                self.player_two.games_won += 1
                print(f'Spock smashes Scissors - Player two wins the round!')

            ### Scissors decapitates Lizard ###
            elif self.player_one.choosen_move == "Scissors" and self.player_two.choosen_move == "Lizard":
                self.player_one.games_won += 1
                print(f'Scissors decapitates Lizard - Player one wins the round!')
            elif self.player_two.choosen_move == "Scissors" and self.player_one.choosen_move == "Lizard":
                self.player_two.games_won += 1
                print(f'Scissors decapitates Lizard - Player two wins the round!')

            ### Lizard eats Paper ###
            elif self.player_one.choosen_move == "Lizard" and self.player_two.choosen_move == "Paper":
                self.player_one.games_won += 1
                print(f'Lizard eats Paper - Player one wins the round!')
            elif self.player_two.choosen_move == "Lizard" and self.player_one.choosen_move == "Paper":
                self.player_two.games_won += 1
                print(f'Lizard eats Paper - Player two wins the round!')

            ### Paper disproves Spock ###
            elif self.player_one.choosen_move == "Paper" and self.player_two.choosen_move == "Spock":
                self.player_one.games_won += 1
                print(f'Paper disproves Spock - Player one wins the round!')
            elif self.player_two.choosen_move == "Paper" and self.player_one.choosen_move == "Spock":
                self.player_two.games_won += 1
                print(f'Paper disproves Spock - Player two wins the round!')

            ### Spock vaporizes Rock ###
            elif self.player_one.choosen_move == "Spock" and self.player_two.choosen_move == "Rock":
                self.player_one.games_won += 1
                print(f'Spock vaporizes Rock - Player one wins the round!')
            elif self.player_two.choosen_move == "Spock" and self.player_one.choosen_move == "Rock":
                self.player_two.games_won += 1
                print(f'Spock vaporizes Rock - Player two wins the round!')



    # def display_winner ():
    #     if player_one.games_won == 2:
    #         print("Player one wins the game!")
    #     elif self.player_two.games_won == 2:
    #         print("Player two wins the game!")

# player_one = Computer()
# opponent = Computer()
round_one = Game()

round_one.choose_game_type()
round_one.run_game()
# round_one.test_logic()
# round_one.display_winner()


print("Testing")