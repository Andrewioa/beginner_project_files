import random  # import random to use the shuffle method to shuffle our deck.


class Cards:  # create a class Cards, to create the objects for a deck
    def __init__(self):
        self.cards = []
        for i in range(1, 13):  # put two decks of cards into our list to use.
            self.cards.append(i)
            self.cards.append(i)
        random.shuffle(self.cards)  # shuffle the deck


class Dealer:
    d_deck = []  # the Dealer's hand

    def first_draw(self):  # First draw is by default, two cards
        self.d_deck.append(random.choice(Cards().cards))
        self.d_deck.append(random.choice(Cards().cards))
        print(f"Dealers hand --> {self.d_deck}")
        print(f"Sum of dealer's hand --> {sum(self.d_deck)}")

    def draw(self):  # method to draw a card, show it and add it to their hand.
        self.d_deck.append(random.choice(Cards().cards))
        print(f"Dealer pulls {self.d_deck[-1]}")
        # print(f"Dealers hand --> {self.d_deck}")
        # print(f"Sum of dealer's hand --> {sum(self.d_deck)}")

    def show(self):  # show their hand and add their cards to return their total sum so far
        print(f"Dealers hand --> {self.d_deck}")
        print(f"Sum of dealer's hand --> {sum(self.d_deck)}")
        return self.d_deck

    def d_sum(self):  # returns the sum of their hand
        return sum(self.d_deck)


class Player:  # The class for the player/user.
    p_deck = []

    # all the Player methods do the same as the Dealer's methods.
    def first_draw(self):
        self.p_deck.append(random.choice(Cards().cards))
        self.p_deck.append(random.choice(Cards().cards))
        print(f"Player hand --> {self.p_deck}")
        print(f"Sum of player's hand --> {sum(self.p_deck)}")

    def draw(self):
        self.p_deck.append(random.choice(Cards().cards))
        print(f"Player pulls {self.p_deck[-1]}")
        # print(f"Player hand --> {self.p_deck}")
        # print(f"Sum of player's hand --> {sum(self.p_deck)}")

    def show(self):
        print(f"Player hand --> {self.p_deck}")
        print(f"Sum of player's hand --> {sum(self.p_deck)}")
        return self.p_deck

    def p_sum(self):
        return sum(self.p_deck)


class BlackJack:
    # Start the game of BlackJack. Break when either one burns, or if they both hold.
    def play_game(self):
        hold = False
        Dealer().first_draw()
        Player().first_draw()
        while Player().p_sum() or Dealer().d_sum() < 21:
            if Dealer().d_sum() < 17:
                Dealer().draw()
                Dealer().show()
                if Dealer().d_sum() > 21:
                    print(f"Dealer has burned!\nYou win!")
                    break
            elif Dealer().d_sum() >= 17:
                print(f"Dealer holds!\t {Dealer().show()}\nSum of dealer's hand --> {sum(Dealer().d_deck)}")
            else:
                Dealer().show()
            if Player().p_sum() > 21:
                Player().show()
                print("You have burned! You lose!")
                break
            if hold is False:
                ask = input("Would you like to draw a card?")
                if ask == "y":
                    Player().draw()
                    if Player().p_sum() > 21:
                        Player().show()
                        print("You have burned! You lose!")
                        break
                    Player().show()
                else:
                    print("Player holds!")
                    hold = True
                    Player().show()
                    Dealer().show()
                    if Dealer().d_sum() < 17:
                        continue
                    elif Dealer().d_sum() > Player().p_sum():
                        print("Dealer wins!")
                        break
                    else:
                        print("Player wins! ")
                        break
        print("Thank you for playing Blackjack!")


deck = Cards()
dealer = Dealer()
game = BlackJack()
game.play_game()
