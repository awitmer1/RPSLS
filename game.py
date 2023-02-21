from human import Human
from computer import Computer

class Game():

    def __init__(self) -> None:
        pass


    def display_rules (self):
        pass

    def run_game (self):
        while player_one.games_won < 2 or opponent.games_won <2:

            player_one_throw = player_one.throw()
            player_two_throw = opponent.throw()

            ### Rock Crushes Scissors ###
            if player_one_throw == "Rock" and player_two_throw == "Scissors":
                player_one.games_won += 1
                print(f'Rock crushes Scissors - Player one wins the round!')
            elif player_two_throw == "Rock" and player_one_throw == "Scissors":
                opponent.games_won += 1
                print(f'Rock crushes Scissors - Player two wins the round!')

            ### Scissors cut Paper ###
            elif player_one_throw == "Scissors" and player_two_throw == "Paper":
                player_one.games_won += 1
                print(f'Scissors cut Paper - Player one wins the round!')
            elif player_two_throw == "Scissors" and player_one_throw == "Paper":
                opponent.games_won += 1
                print(f'Scissors cut Paper - Player two wins the round!')

            ### Paper covers Rock ###
            elif player_one_throw == "Paper" and player_two_throw == "Rock":
                player_one.games_won += 1
                print(f'Paper covers Rock - Player one wins the round!')
            elif player_two_throw == "Paper" and player_one_throw == "Rock":
                opponent.games_won += 1
                print(f'Paper covers Rock - Player two wins the round!')

            ### Rock crushes Lizard ###
            elif player_one_throw == "Rock" and player_two_throw == "Lizard":
                player_one.games_won += 1
                print(f'Rock crushes Lizard - Player one wins the round!')
            elif player_two_throw == "Rock" and player_one_throw == "Lizard":
                opponent.games_won += 1
                print(f'Rock crushes Lizard - Player two wins the round!')

            ### Lizard poisons Spock ###
            elif player_one_throw == "Lizard" and player_two_throw == "Spock":
                player_one.games_won += 1
                print(f'Lizard poisons Spock - Player one wins the round!')
            elif player_two_throw == "Lizard" and player_one_throw == "Spock":
                opponent.games_won += 1
                print(f'Lizard poisons Spock - Player two wins the round!')

            ### Spock smashes Scissors ###
            elif player_one_throw == "Spock" and player_two_throw == "Scissors":
                player_one.games_won += 1
                print(f'Spock smashes Scissors - Player one wins the round!')
            elif player_two_throw == "Spock" and player_one_throw == "Scissors":
                opponent.games_won += 1
                print(f'Spock smashes Scissors - Player two wins the round!')

            ### Scissors decapitates Lizard ###
            elif player_one_throw == "Scissors" and player_two_throw == "Lizard":
                player_one.games_won += 1
                print(f'Scissors decapitates Lizard - Player one wins the round!')
            elif player_two_throw == "Scissors" and player_one_throw == "Lizard":
                opponent.games_won += 1
                print(f'Scissors decapitates Lizard - Player two wins the round!')

            ### Lizard eats Paper ###
            elif player_one_throw == "Lizard" and player_two_throw == "Paper":
                player_one.games_won += 1
                print(f'Lizard eats Paper - Player one wins the round!')
            elif player_two_throw == "Lizard" and player_one_throw == "Paper":
                opponent.games_won += 1
                print(f'Lizard eats Paper - Player two wins the round!')

            ### Paper disproves Spock ###
            elif player_one_throw == "Paper" and player_two_throw == "Spock":
                player_one.games_won += 1
                print(f'Paper disproves Spock - Player one wins the round!')
            elif player_two_throw == "Paper" and player_one_throw == "Spock":
                opponent.games_won += 1
                print(f'Paper disproves Spock - Player two wins the round!')

            ### Spock vaporizes Rock ###
            elif player_one_throw == "Spock" and player_two_throw == "Rock":
                player_one.games_won += 1
                print(f'Spock vaporizes Rock - Player one wins the round!')
            elif player_two_throw == "Spock" and player_one_throw == "Rock":
                opponent.games_won += 1
                print(f'Spock vaporizes Rock - Player two wins the round!')



    def display_winner ():
        if player_one.games_won == 2:
            print("Player one wins the game!")
        elif opponent.games_won == 2:
            print("Player two wins the game!")

player_one = Human()
opponent = Computer()
round_one = Game()

round_one.run_game()
round_one.display_winner


print("Testing")