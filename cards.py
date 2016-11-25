#module cards

<<<<<<< HEAD:cards.py
if __name__ == "__main__":
    print("This is a module with classes for playing cards.")
    input("\n\nPress the enter key to exit.")
=======

>>>>>>> 9ef18e71ce6ac1cd22628c79fe6fd53dd9843d55:Cards.py

class Card(object):
    """ card """
    NOMINAL = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, nominal, suit):
        self.nominal = nominal
        self.suit = suit

    def __str__(self):
        ns = self.nominal + self.suit
        return ns
      
class Hand(object):
    """  """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
           ns = ""
           for card in self.cards:
               ns += str(card) + "\t"
        else:
            ns = "<empty>"
        return ns

    def clear_card(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def give_card(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add_card(card)

class Deck(Hand):
    """ A deck of playing cards. """
    def home(self):
        for suit in Card.SUITS:
            for nominal in Card.NOMINAL: 
                self.add_card(Card(nominal, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give_card(top_card, hand)
                else:
                    print("Out of cards!")



