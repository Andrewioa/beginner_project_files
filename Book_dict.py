import random


class Player():
    def __init__(self, name):
        self.name = name


class Game():

    def rules(self, player, machine, x, y):    # Grabs the input of the user and the random machine input
        # and decides based on the  game's rules, if he wins, loses or ties.

        if x == 'rock' and y == 'paper':
            print(f'{player} drew {x} and {machine} drew {y}')
            print(f'{machine} wins!')
        elif x == y:
            print(f'{player} drew {x} and {machine} drew {y}')
            print("It's a tie!")
        elif x == 'rock' and y == 'scissors':
            print(f'{player} drew {x} and {machine} drew {y}')
            print(f'{player} wins!')
        elif x == 'paper' and y == 'rock':
            print(f'{player} drew {x} and {machine} drew {y}')
            print(f'{player} wins!')
        elif x == 'paper' and y == 'scissors':
            print(f'{player} drew {x} and {machine} drew {y}')
            print(f'{machine} wins!')
        elif x == 'scissors' and y == 'rock':
            print(f'{player} drew {x} and {machine} drew {y}')
            print(f'{machine} wins!')
        elif x == 'scissors' and y == 'paper':
            print(f'{player} drew {x} and {machine} drew {y}')
            print(f'{player} wins!')

    def play_game(self):
        list_game = ['paper', 'rock', 'scissors']
        person = input('what is your name?\n').capitalize()
        print(f'Welcome to Rock, Paper, Scissors {person}!')
        print('Type "q" to quit!')

        while True:

            choice = input('Rock, paper or scissors?\n').lower()

            if choice == 'rock':
                rock = choice
            elif choice == 'paper':
                paper = choice
            elif choice == 'q':
                break
            elif choice == 'scissors':
                scissors = choice
            else:
                print('Please choose only rock, paper or scissors!')

            c = Player(person)
            machine_choice = random.choice(list_game)
            m = 'machine'

            Game.rules(self, c.name, m, choice, machine_choice)


g = Game()
g.play_game()
