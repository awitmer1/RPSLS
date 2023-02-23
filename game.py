from human import Human
from computer import Computer
from time import sleep



class Game():

    def __init__(self) -> None:
        self.player_one = None
        self.player_two = None

    def choose_game_type(self):

        user_input = input("What type of game would you like to play?: PvP || PvAI || AIvAI - ")
        if user_input == 'PvP':
            self.player_one = Human()
            self.player_two = Human()
        elif user_input == "PvAI":
            self.player_one = Human()
            self.player_two = Computer()
        elif user_input == "AIvAI":
            self.player_one = Computer()
            self.player_two = Computer()
        else:
            print("Sorry, please choose a correct game mode.")
            self.choose_game_type()

    def display_rules (self):
        print("""\nHere are the rules: \n
        Rock crushes Scissors
        Scissors cuts Paper 
        Paper covers Rock
        Rock crushes Lizard
        Lizard poisons Spock
        Spock smashes Scissors
        Scissors decapitates Lizard
        Lizard eats Paper
        Paper disproves Spock
        Spock vaporizes Rock
        """)

    def run_game (self):

        self.choose_game_type()
        self.display_rules()

        while self.player_one.games_won < 2 and self.player_two.games_won < 2:

            sleep(1.5)
            self.player_one.throw()
            sleep(1.5)
            self.player_two.throw()

            ### Rock Crushes Scissors ###
            if self.player_one.chosen_move == "Rock" and self.player_two.chosen_move == "Scissors":
                self.player_one.games_won += 1
                print(f'Rock crushes Scissors - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Rock" and self.player_one.chosen_move == "Scissors":
                self.player_two.games_won += 1
                print(f'Rock crushes Scissors - Player two wins the round!\n')

            ### Scissors cut Paper ###
            elif self.player_one.chosen_move == "Scissors" and self.player_two.chosen_move == "Paper":
                self.player_one.games_won += 1
                print(f'Scissors cut Paper - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Scissors" and self.player_one.chosen_move == "Paper":
                self.player_two.games_won += 1
                print(f'Scissors cut Paper - Player two wins the round!\n')

            ### Paper covers Rock ###
            elif self.player_one.chosen_move == "Paper" and self.player_two.chosen_move == "Rock":
                self.player_one.games_won += 1
                print(f'Paper covers Rock - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Paper" and self.player_one.chosen_move == "Rock":
                self.player_two.games_won += 1
                print(f'Paper covers Rock - Player two wins the round!\n')

            ### Rock crushes Lizard ###
            elif self.player_one.chosen_move == "Rock" and self.player_two.chosen_move == "Lizard":
                self.player_one.games_won += 1
                print(f'Rock crushes Lizard - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Rock" and self.player_one.chosen_move == "Lizard":
                self.player_two.games_won += 1
                print(f'Rock crushes Lizard - Player two wins the round!\n')

            ### Lizard poisons Spock ###
            elif self.player_one.chosen_move == "Lizard" and self.player_two.chosen_move == "Spock":
                self.player_one.games_won += 1
                print(f'Lizard poisons Spock - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Lizard" and self.player_one.chosen_move == "Spock":
                self.player_two.games_won += 1
                print(f'Lizard poisons Spock - Player two wins the round!\n')

            ### Spock smashes Scissors ###
            elif self.player_one.chosen_move == "Spock" and self.player_two.chosen_move == "Scissors":
                self.player_one.games_won += 1
                print(f'Spock smashes Scissors - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Spock" and self.player_one.chosen_move == "Scissors":
                self.player_two.games_won += 1
                print(f'Spock smashes Scissors - Player two wins the round!\n')

            ### Scissors decapitates Lizard ###
            elif self.player_one.chosen_move == "Scissors" and self.player_two.chosen_move == "Lizard":
                self.player_one.games_won += 1
                print(f'Scissors decapitates Lizard - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Scissors" and self.player_one.chosen_move == "Lizard":
                self.player_two.games_won += 1
                print(f'Scissors decapitates Lizard - Player two wins the round!\n')

            ### Lizard eats Paper ###
            elif self.player_one.chosen_move == "Lizard" and self.player_two.chosen_move == "Paper":
                self.player_one.games_won += 1
                print(f'Lizard eats Paper - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Lizard" and self.player_one.chosen_move == "Paper":
                self.player_two.games_won += 1
                print(f'Lizard eats Paper - Player two wins the round!\n')

            ### Paper disproves Spock ###
            elif self.player_one.chosen_move == "Paper" and self.player_two.chosen_move == "Spock":
                self.player_one.games_won += 1
                print(f'Paper disproves Spock - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Paper" and self.player_one.chosen_move == "Spock":
                self.player_two.games_won += 1
                print(f'Paper disproves Spock - Player two wins the round!\n')

            ### Spock vaporizes Rock ###
            elif self.player_one.chosen_move == "Spock" and self.player_two.chosen_move == "Rock":
                self.player_one.games_won += 1
                print(f'Spock vaporizes Rock - Player one wins the round!\n')
            elif self.player_two.chosen_move == "Spock" and self.player_one.chosen_move == "Rock":
                self.player_two.games_won += 1
                print(f'Spock vaporizes Rock - Player two wins the round!\n')

        if self.player_one.games_won == 2:
            print("""\n\n\n
            We have a winner! Player one wins the game!\n\n\n""")
        elif self.player_two.games_won == 2:
            print("""\n\n\n
            We have a winner! Player two wins the game!\n\n\n""")


round_one = Game()
round_one.run_game()