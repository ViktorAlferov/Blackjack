#module Cards



class Card(object):
    """ card """
    NOMINAL = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
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





deck_1 = Deck()
print("Deck_1:")
print(deck_1)

deck_1.home()
print("Deck_1: ")
print(deck_1)

deck_1.shuffle()
print("Deck_1:")
print(deck_1)

hand_1 = Hand()
hand_2 = Hand()
hands = [hand_1, hand_2]
deck_1.deal(hands, per_hand = 7)
print("hand_1")
print(hand_1)
print("hand_2")
print(hand_2)
print("Deck_1:")
print(deck_1)

deck_1.clear_card()
print("Deck_1:", deck_1)

input("\n\nPress the enter for exit.")

