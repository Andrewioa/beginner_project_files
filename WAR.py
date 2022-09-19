class Card:
    def __init__(self,v,s):
        self.value=v
        self.suit=s

    values=[None, None, '2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    suits=['cloves','hearts','diamonds','spades']

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value==c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value==c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v= self.values[self.value] + ' of ' + self.suits[self.suit]
        return v


import random

class Deck:

    def __init__(self):
        self.cards=[]
        for i in range(2,14):
            for j in range(4):
                self.cards.append(Card(i,j))
        random.shuffle(self.cards)
    def random_card(self):
        d=Deck()
        a=d.cards[5]
        return a




class Player:
    def __init__(self,n):
        self.win = 0
        self.name=n

class Game:
    def __init__(self):
        player1=input('Player 1 name ')
        player2=input('Player 2 name ')
        self.deck=Deck()
        self.p1 = Player(player1)
        self.p2=Player(player2)


    def play_game(self):
        print('Welcome to WAR! ')
        wins=0

        while wins < 10:

            pl1=self.deck.random_card()
            pl2=self.deck.random_card()
            if pl1 > pl2:
                self.p1.win+=1
                wins+=1

                print('{} drew {}'.format(self.p1.name, pl1))

                print('{} drew {}'.format(self.p2.name, pl2))
                print(self.p1.name + " wins this round! ")
            else:
                self.p2.win+=1
                wins+=1

                print('{} drew {}'.format(self.p1.name, pl1))

                print('{} drew {}'.format(self.p2.name,pl2))
                print(self.p2.name + ' wins this round! ')

            x=0

            while x==0:
                if wins == 10:
                    break

                play_again = input('Press "p" to play again or "q" to quit! ')

                if play_again== 'p':
                    break
                if play_again == 'q':
                    x+=1
                    break

                else:
                    print("Must type 'p' or 'q'! ")
                    continue
            if x==1:
                break
            else:
                continue
        if self.p1.win > self.p2.win:
            print(self.p1.name + ' wins this GAME! ')
        else:
            print(self.p2.name + ' wins this GAME! ')

        print('Thank you for playing WAR! ')


g=Game()
g.play_game()
